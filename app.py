import streamlit as st
from core.rag_engine import RAGEngine
from core.document_processor import DocumentProcessor
from core.web_search import WebSearch
from core.quiz_generator import QuizGenerator
from core.knowledge_tracer import KnowledgeTracer

st.set_page_config(page_title="AI Study Assistant", layout="wide")

st.title("🤖 Smart AI Study Assistant")

# Initialize modules
rag_engine = RAGEngine()
doc_processor = DocumentProcessor()
web_search = WebSearch()
quiz_gen = QuizGenerator()
knowledge_tracer = KnowledgeTracer()

menu = st.sidebar.selectbox(
    "Navigation",
    ["Ask AI", "Upload Document", "Generate Quiz", "Progress Tracker"]
)

# ---- ASK AI ----
if menu == "Ask AI":
    st.header("Ask a Question")
    question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if question:
            answer = rag_engine.get_answer(question)
            st.success(answer)
        else:
            st.warning("Please enter a question")

# ---- UPLOAD DOCUMENT ----
elif menu == "Upload Document":
    st.header("Upload Study Material")

    uploaded_file = st.file_uploader("Upload file", type=["pdf", "txt", "docx"])

    if uploaded_file is not None:
        doc_processor.process_document(uploaded_file)
        st.success("Document processed successfully!")

# ---- QUIZ GENERATOR ----
elif menu == "Generate Quiz":
    st.header("Quiz Generator")

    topic = st.text_input("Enter topic")

    if st.button("Generate Quiz"):
        quiz = quiz_gen.generate_quiz(topic)
        st.write(quiz)

# ---- PROGRESS TRACKER ----
elif menu == "Progress Tracker":
    st.header("Learning Progress")

    progress = knowledge_tracer.get_progress()
    st.write(progress)
