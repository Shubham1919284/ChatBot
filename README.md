# 🤖 DeepSeek Chat – Streamlit UI

A sleek and responsive **Chatbot UI built using Streamlit**, powered by the `DeepSeek` model via **API**. This project mimics a modern ChatGPT-style experience with avatars, markdown rendering, light/dark theme toggle, chat history, and more.

## ✨ Features

- 🧠 **Streamed responses** using API (`deepseek/deepseek-chat`)
- 🤖 **Avatars** and markdown-based message bubbles
- 🌙 **Dark theme enabled by default** with light/dark mode toggle
- 🕒 **Timestamps** for each chat message
- ✍️ **Typing indicator** (`🤔 Thinking...`)
- 📥 **Downloadable chat history** (as `.json`)
- 🧹 **Clear conversation** with one click
- 📦 Minimal, clean UI 

---

## 🚀 Demo

![demo](https://github.com/Shubham1919284/ChatBot/blob/d8a26cc692be4b757688a4efec265b681abdc7dc/Screenshot%202025-07-19%20030314.png)

---

## 🛠️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/deepseek-streamlit-chat.git
cd deepseek-streamlit-chat
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenRouter API Key

There are **two options**:

#### Option A: `.env` file
Create a `.env` file in the root directory:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Then use `python-dotenv` or access it using `os.getenv("OPENROUTER_API_KEY")`.

#### Option B: Set environment variable (temporary)

```bash
export API_KEY=your_api_key_here  # Mac/Linux
API_KEY=your_api_key_here     # Windows
```

> 🔐 *Note: The app has no sidebar and does NOT expose your API key.*

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

Create a `requirements.txt` file using the following (already included):

```txt
streamlit
requests
python-dotenv
```

Or generate it dynamically:

```bash
pip freeze > requirements.txt
```

---

## 🧠 Model Used

- **Model:** `deepseek/deepseek-chat`
- **Streaming Support:** ✅ Enabled

You can replace the model with any other  (like `gpt-3.5-turbo`, `mistral`, etc.) by updating the `MODEL` variable in `app.py`.

---

## 📁 Project Structure

```
📦 deepseek-streamlit-chat
├── app.py                  # Main Streamlit App
├── requirements.txt        # Python dependencies
└── README.md               # You are here
```

---

## 📸 Screenshots

| Theme         | Chat View                           |
|---------------|-------------------------------------|
| Dark (default) | ![dark]([assets/screenshot-dark.png](https://github.com/Shubham1919284/ChatBot/blob/d8a26cc692be4b757688a4efec265b681abdc7dc/Screenshot%202025-07-19%20030314.png)) |
| Light         | ![light]([assets/screenshot-light.png](https://github.com/Shubham1919284/ChatBot/blob/d8a26cc692be4b757688a4efec265b681abdc7dc/Screenshot%202025-07-19%20030350.png)) |

---

## 🔒 Secrets Management (Optional for Streamlit Cloud)

If deploying to **Streamlit Community Cloud**, use `secrets.toml` in `.streamlit/` folder:

```toml
[openrouter]
api_key = "your_openrouter_api_key_here"
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🙋‍♂️ Credits

- UI inspired by ChatGPT-like themes
- Built with ❤️ using [Streamlit] --> https://chatbot-sk.streamlit.app/

---

## 📬 Feedback & Contributions

If you find this project helpful, please ⭐ star the repo and consider contributing or raising issues for enhancements!

---

