# 🧑‍💻 CoderBuddy

Agentic AI app builder inspired by Lovable. It takes your idea, asks clarifying questions, plans the architecture, and generates a runnable project you can download as a ZIP — all inside a Streamlit UI.

Built with Streamlit, LangGraph, LangChain, and Groq (model: `openai/gpt-oss-120b`).

---

## ✨ Features

- **Smart Prompt Verification** - Ensures your input is an engineering/app-building task
- **Interactive Q&A** - Clean, numbered clarifying questions with organized answer fields
- **Multi-Agent Workflow** - Verifier → Requirements → Planner → Architect → Coder
- **Code Generation** - Generates complete, runnable projects with all necessary files
- **One-Click Download** - Download your generated project as a ZIP file
- **Live Preview** - Renders README or HTML files directly in the interface
- **Conversation Memory** - Maintains context across interactions
- **Memory Management** - Clear conversation history with one click

---

## 📋 Requirements

- **Python 3.10+** (recommended)
- **Groq API Key** - Get your free API key from [console.groq.com](https://console.groq.com)
- **Internet Connection** - Required for AI model access

---

## 🚀 Quick Setup

### 1. Clone and Navigate
```bash
cd Projects/04_CoderBuddy
```

### 2. Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

**Note**: If you encounter `ModuleNotFoundError`, ensure you're using the correct Python environment. The app requires Python 3.10+ with all dependencies installed.

### 3. Configure API Key
Create a `.env` file in the project directory:
```bash
echo "GROQ_API_KEY=your_actual_groq_api_key_here" > .env
```

Replace `your_actual_groq_api_key_here` with your real Groq API key.

### 4. Run the Application
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501` (or another port if 8501 is busy).

---

## 🎯 How to Use

1. **Describe Your App** - Enter your app idea in the prompt box
2. **Run CoderBuddy** - Click "Run CoderBuddy 🚀" to start the AI workflow
3. **Answer Questions** - Respond to any clarifying questions (now with clean, numbered interface)
4. **Review Plan** - Check the generated plan and architecture
5. **Download Project** - Use "Download Project ZIP 📦" to get your complete app

### 💡 Pro Tips
- Be specific about your app requirements for better results
- Answer clarifying questions thoroughly
- The generated ZIP contains all files needed to run your app locally
- Use the "Clear Memory" button to start fresh conversations

---

## 📁 Project Structure

```
Projects/04_CoderBuddy/
├─ app.py                # Main Streamlit application
├─ requirements.txt       # Python dependencies
├─ pyproject.toml        # Project configuration
├─ .env                  # Environment variables (API keys)
├─ Readme.md            # This file
├─ streamlit.log        # Application logs
└─ agents/              # AI agent modules
   ├─ __init__.py
   ├─ filewriter.py     # Project file generation & ZIP creation
   ├─ graph.py          # LangGraph workflow definition
   ├─ model.py          # Groq LLM client configuration
   ├─ nodes.py          # Individual agent nodes (Verifier, Planner, etc.)
   └─ state.py          # Graph state management
```

---

## 🔧 Environment Configuration

### Required Environment Variables
Create a `.env` file with:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

### Getting a Groq API Key
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Generate an API key
4. Copy the key and add it to your `.env` file

---

## 🛠️ Troubleshooting

### Common Issues

**❌ `ModuleNotFoundError: No module named 'openai'`**
- **Solution**: Ensure you're using Python 3.10+ and install dependencies with the correct Python version
- **Fix**: `python3.10 -m pip install -r requirements.txt`

**❌ `GROQ_API_KEY not set`**
- **Solution**: Create a `.env` file with your Groq API key
- **Fix**: `echo "GROQ_API_KEY=your_key_here" > .env`

**❌ Port already in use**
- **Solution**: Streamlit will automatically use the next available port (8502, 8503, etc.)
- **Fix**: Check the terminal output for the correct URL

**❌ LangChain deprecation warnings**
- **Solution**: These are just warnings and don't affect functionality
- **Fix**: The app includes fallback memory handling for compatibility

### Performance Optimization
```bash
# Install Watchdog for better file monitoring (macOS)
xcode-select --install
pip install watchdog
```

### Dependency Conflicts
If you encounter dependency conflicts:
```bash
# Create a fresh virtual environment
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔄 Recent Updates

- **✅ Fixed UI Issues** - Improved question/answer interface with numbered questions
- **✅ Enhanced Error Handling** - Better dependency management and environment setup
- **✅ Cleaner Interface** - Organized answer fields and better visual hierarchy
- **✅ Improved Documentation** - Updated setup instructions and troubleshooting guide
