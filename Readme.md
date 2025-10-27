# 🤖 My Agents Hub

A comprehensive collection of AI-powered applications and intelligent agents built with modern technologies. This hub showcases various real-world solutions leveraging AI, machine learning, and automation.

## 🚀 Overview

My Agents Hub is a portfolio of AI applications designed to solve practical problems across different domains. Each project demonstrates different aspects of AI implementation, from document processing to code generation.

## 📁 Project Structure

```
my-agents-hub/
├── Home.py                    # Main landing page
├── README.md                  # This file
├── requirements.txt           # Global dependencies
└── Projects/                  # Individual AI projects
    ├── 01_invoice_auditor/    # Invoice processing and auditing
    ├── 02_text_to_sql/        # Natural language to SQL conversion
    ├── 03_resume_matcher/     # Resume analysis and matching
    └── 04_CoderBuddy/         # AI-powered app builder
```

## 🛠️ Projects

### 1. 📄 Invoice Auditor (`01_invoice_auditor`)
**Status**: In Development  
**Purpose**: Automated invoice processing and auditing system  
**Tech Stack**: Streamlit, AI/ML libraries  
**Features**: 
- Document extraction and analysis
- Automated auditing workflows
- Error detection and reporting

### 2. 🔍 Text to SQL (`02_text_to_sql`)
**Status**: ✅ Complete   
**Purpose**: Convert natural language queries to SQL statements  
**Tech Stack**: Streamlit, NLP libraries  
**Features**:
- Natural language query processing
- SQL generation and validation
- Database schema understanding

### 3. 📋 Resume Matcher (`03_resume_matcher`)
**Status**: ✅ Complete  
**Purpose**: Intelligent resume analysis and job matching  
**Tech Stack**: Streamlit, ML libraries  
**Features**:
- Resume parsing and analysis
- Skill extraction and matching
- Job compatibility scoring

### 4. 🧑‍💻 CoderBuddy (`04_CoderBuddy`)
**Status**: ✅ Complete  
**Purpose**: AI-powered application builder  
**Tech Stack**: Streamlit, LangGraph, LangChain, Groq  
**Features**:
- Prompt verification for engineering tasks
- Clarifying questions with conversation memory
- Multi-agent workflow (Verifier → Requirements → Planner → Architect)
- Code artifact generation
- One-click ZIP download
- Live preview capabilities

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd my-agents-hub
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main hub**
   ```bash
   streamlit run Home.py
   ```

### Running Individual Projects

Each project in the `Projects/` folder can be run independently:

```bash
# Example: Run CoderBuddy
cd Projects/04_CoderBuddy
pip install -r requirements.txt
streamlit run app.py
```

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: LangChain, LangGraph, OpenAI, Groq
- **Document Processing**: PyPDF, ChromaDB
- **Environment Management**: Python-dotenv
- **Text Processing**: Tiktoken

## 📋 Dependencies

Core dependencies include:
- `streamlit` - Web application framework
- `langchain` - LLM application framework
- `openai` - OpenAI API client
- `tiktoken` - Text tokenization
- `chromadb` - Vector database
- `pypdf` - PDF processing
- `python-dotenv` - Environment variable management

## 🔐 Environment Setup

Most projects require API keys. Create a `.env` file in the project directory:

```env
# Example for CoderBuddy
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## 📊 Project Status

| Project | Status | Description |
|---------|--------|-------------|
| Invoice Auditor | 🚧 Development | Document processing and auditing |
| Text to SQL | 🚧 Development | Natural language to SQL conversion |
| Resume Matcher | 🚧 Development | Resume analysis and matching |
| CoderBuddy | ✅ Complete | AI-powered app builder |

## 🤝 Contributing

This is a personal portfolio project showcasing AI applications. Each project demonstrates different aspects of AI implementation and can serve as learning examples.

## 📝 License

MIT License - Feel free to use these projects for learning and inspiration.

## 🔗 Connect

- LinkedIn: [Your LinkedIn Profile]
- Portfolio: [Your Portfolio Website]

---

**Note**: This hub is continuously evolving with new projects and improvements. Check back regularly for updates!
