# 🎬 YouTube to Article Pipeline

A simple end-to-end Generative AI pipeline that extracts YouTube transcripts and converts them into short summaries and structured, blog-style Markdown articles.

## ✨ Features

- **Transcript Extraction:** Automatically fetches subtitles from any public YouTube video.
- **AI Summarization:** Condenses long transcripts into a concise 3-4 sentence overview.
- **Structured Formatting:** Converts raw text into a professional Markdown article (includes Title, Headings, Bullet points, and Key Takeaways).
- **Easy Download:** One-click download button to save the generated `.md` file.
- **Web Interface:** Clean UI built with Streamlit.

## ⚙️ How It Works (The Pipeline)

This project follows a 3-step data processing pipeline:

1. **Extract:** The app parses the YouTube URL to get the Video ID, then uses the `youtube-transcript-api` library to pull the raw subtitle text.
2. **Summarize:** The raw transcript (which can be massive) is sent to an LLM (Groq's Llama-3) with a prompt to generate a short summary of the core topic.
3. **Structure:** The summary and the original transcript are sent to the LLM a second time with strict formatting instructions to generate a structured Markdown blog post.

## 🛠️ Tech Stack

- **Language:** Python
- **UI Framework:** Streamlit
- **AI Model:** Groq API (`llama-3.1-8b-instant` for fast, free inference)
- **Data Extraction:** `youtube-transcript-api`

## 🚀 Running Locally

To run this project on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PavanKumarAadelli/youtube-summarizer.git
   cd youtube-summarizer
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API Key:**
   - Get a free API key from [Groq Console](https://console.groq.com/keys).
   - In your project folder, create a folder named exactly `.streamlit`.
   - Inside that folder, create a file named `secrets.toml`.
   - Add your API key to the file like this:
     ```toml
     API_KEY = "gsk_your_actual_api_key_here"
     ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## 🌐 Live Demo

The app is deployed 24/7 on Streamlit Community Cloud: 
[https://youtube-summarizer-99.streamlit.app/]

## Demo

<img width="1057" height="691" alt="Screenshot 2026-03-31 220024" src="https://github.com/user-attachments/assets/4ba14686-6f3a-4859-826c-b0f2639b10c9" />



## 🔮 Future Scope

- **Multiple Languages:** Add support for auto-translating non-English transcripts before summarizing.
- **Audio Fallback:** Integrate OpenAI's Whisper API to generate transcripts for videos that don't have subtitles.
- **Export Options:** Add buttons to export directly to PDF or HTML instead of just Markdown.
- **Chat with Video:** Add a chatbot feature to ask questions specifically about the video's content.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
