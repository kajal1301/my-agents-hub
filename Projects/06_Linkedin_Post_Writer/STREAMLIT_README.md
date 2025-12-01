# LinkedIn Post Generator - Streamlit App

A beautiful web interface for generating LinkedIn posts using AI-powered LangGraph agents.

## 🚀 Quick Start

### Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## 📋 Features

- **Easy-to-use Interface**: Clean, modern UI with LinkedIn branding
- **Customizable Settings**: 
  - Choose from multiple tones (Professional, Formal, Inspirational, etc.)
  - Select target audience
- **Real-time Generation**: Watch your post being generated with progress indicators
- **Multiple Views**: 
  - Final optimized post
  - Key points breakdown
  - Generation details
- **Export Options**: 
  - Copy to clipboard
  - Download as text file
- **Post Statistics**: Word count, character count, and hashtag count

## 🎯 How to Use

1. **Enter Your Topic**: Type or paste your topic in the text area
2. **Configure Settings** (optional): 
   - Select tone from the sidebar
   - Choose target audience
3. **Generate**: Click the "🚀 Generate Post" button
4. **Review & Export**: 
   - Review the generated post in the "Final Post" tab
   - Check key points in the "Key Points" tab
   - View details in the "Details" tab
   - Copy or download your post

## 📁 Files

- `streamlit_app.py` - Main Streamlit application
- `PostGeneratorAgent.py` - LangGraph agent for post generation
- `keys.py` - API configuration

## 🔧 Requirements

All dependencies are listed in `requirements.txt`. Make sure you have:

- Python 3.8+
- Streamlit
- LangGraph
- LangChain
- Azure OpenAI API credentials (configured in `keys.py`)

## 💡 Tips

- Be specific with your topic for better results
- Review and personalize the generated post before publishing
- Experiment with different tones for different audiences
- Use the key points as talking points for your post

## 🐛 Troubleshooting

If you encounter any issues:

1. Make sure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Verify your API credentials in `keys.py`

3. Check that the `PostGeneratorAgent.py` file is in the same directory

4. Ensure you have an active internet connection for API calls

## 📝 Notes

- The generation process may take 30-60 seconds depending on API response times
- Generated posts are optimized for LinkedIn's format and best practices
- Always review and customize the output before posting

