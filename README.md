# AI Study Assistant

## 📌 Project Overview

AI Study Assistant is an intelligent learning support system built using Python and Streamlit.
The system helps students learn more effectively by combining document processing, web search, quiz generation, and knowledge tracing with AI-based retrieval techniques.

It uses a Retrieval-Augmented Generation (RAG) approach to analyze study material and provide helpful responses to users.

## 🎯 Features

* AI-powered question answering
* Document upload and processing
* Web search integration
* Quiz generation for learning assessment
* Knowledge tracing to track user progress
* Interactive Streamlit interface

## ⚙️ Technologies Used

* Python
* Streamlit
* Retrieval Augmented Generation (RAG)
* Pandas
* SQLite Database
* Web APIs
* Vector Database (Chroma)

## 📂 Project Structure

```
AIassistant/
│
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── requirements.txt            # Required Python libraries
│
├── core/                       # Core application logic
│   ├── rag_engine.py
│   ├── web_search.py
│   ├── document_processor.py
│   ├── knowledge_tracer.py
│   ├── quiz_generator.py
│   └── __init__.py
│
├── data/
│   ├── uploads/                # Uploaded files
│   ├── cache/                  # Cache storage
│   ├── vector_store/           # Vector database
│   └── user_progress.db        # SQLite database
│
├── logs/                       # Application logs
│
└── tests/                      # Test scripts
```

## ▶️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/AIassistant.git
```

### 2. Go to the project directory

```
cd AIassistant
```

### 3. Install required dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

## 📊 How the System Works

1. User uploads study documents.
2. Documents are processed and stored in a vector database.
3. The RAG engine retrieves relevant information.
4. The system generates answers, quizzes, and tracks learning progress.

## 🚀 Future Improvements

* Integration with more AI models
* Better quiz personalization
* Advanced analytics dashboard
* Cloud deployment support

## 👨‍💻 Author

ME Computer Engineering Project
