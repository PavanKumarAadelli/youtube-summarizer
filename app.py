import streamlit as st
from groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi

# --- setup api stuff ---
# We will load the API key from Streamlit's hidden secrets (we set this up in Phase 2)
client = Groq(api_key=st.secrets["API_KEY"])
# --- web page setup ---
st.set_page_config(page_title="YouTube Summarizer", page_icon="🎬")
st.title("YouTube to Article Pipeline")
st.write("Paste a YouTube link below and get a structured blog article.")

# --- functions ---
def get_youtube_text(url):
    try:
        vid_id = url.split("v=")[1]
        if "&" in vid_id:
            vid_id = vid_id.split("&")[0]

        api = YouTubeTranscriptApi()
        data = api.fetch(vid_id)
        
        text = ""
        for item in data:
            text = text + " " + item.text
        return text
        
    except Exception as e:
        st.error(f"Couldn't get subtitles. Error: {e}")
        return None

def make_summary(text):
    prompt = "summarize this youtube video transcript in 3-4 sentences. just give the main points.\n\n" + text
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def make_article(summary, original_text):
    prompt = """you are a blogger. take this summary and the transcript and write a nice markdown article.
give it a # title, a short intro, some ## headings for main topics, and a ## Key Takeaways section with bullet points.

summary: """ + summary + "\n\ntranscript for extra details: """ + original_text
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- main web logic ---
# 1. get input from the user
youtube_url = st.text_input("YouTube Link:")

# 2. create a button
if st.button("Generate Article"):
    if youtube_url:
        with st.spinner("Fetching transcript..."):
            raw_text = get_youtube_text(youtube_url)
        
        if raw_text is not None:
            with st.spinner("Contacting AI for summary..."):
                short_summary = make_summary(raw_text)
            
            with st.spinner("Writing the final article..."):
                final_md = make_article(short_summary, raw_text)
            
            st.success("Done!")
            
            # show the article on the website
            st.markdown(final_md)
            
            # add a download button
            st.download_button(
                label="Download as Markdown File",
                data=final_md,
                file_name="article_output.md",
                mime="text/markdown"
            )
    else:
        st.warning("Please enter a YouTube link first.")