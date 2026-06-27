"""
Identity Governance RAG Assistant - Streamlit application.
"""

import os
import datetime
import json

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from rag import RAGEngine

FEEDBACK_LOG = os.path.join(os.path.dirname(__file__), "feedback_log.jsonl")

st.set_page_config(
    page_title="Identity Governance RAG Assistant",
    page_icon="🛡️",
    layout="wide",
)

@st.cache_resource(show_spinner="Loading knowledge base and connecting to Bedrock...")
def load_engine():
    return RAGEngine()

def log_feedback(question: str, answer: str, rating: str):
    record = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "question": question,
        "answer": answer,
        "rating": rating,
    }
    with open(FEEDBACK_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

with st.sidebar:
    st.title("🛡️ Identity Governance Assistant")
    st.markdown(
        "Grounded question answering over approved identity governance "
        "standards, NIST frameworks, CyberArk documentation, and audit templates."
    )
    st.divider()
    st.subheader("How it works")
    st.markdown(
        "- Answers drawn **only** from the approved knowledge base\n"
        "- Every answer **cites its source document**\n"
        "- If no relevant policy exists, the assistant says so\n"
        "- The assistant **does not make access decisions**\n"
        "- Responses follow: Recommendation → Why → Standards → Business Impact"
    )
    st.divider()
    st.subheader("Example questions")
    st.markdown(
        "- Can a contractor receive AdministratorAccess?\n"
        "- What evidence is required for a SOX privileged access review?\n"
        "- What is the dormancy threshold for a service account?\n"
        "- How do we prevent AI agents from taking unauthorized actions?\n"
        "- What approval is required for AWS AdministratorAccess?\n"
        "- What happens when an NHI owner departs the organization?"
    )
    st.divider()
    st.caption(
        f"Region: `{os.environ.get('AWS_REGION', 'us-east-1')}`  \n"
        f"Model: `{os.environ.get('BEDROCK_LLM_MODEL', 'claude-haiku-4-5')}`"
    )

st.title("🛡️ Identity Governance RAG Assistant")
st.warning(
    "**AI assists, humans decide.** This assistant provides policy guidance "
    "grounded in approved governance documentation. It does not approve, deny, "
    "or grant access. All access decisions remain with authorized human reviewers.",
    icon="⚠️",
)

if "messages" not in st.session_state:
    st.session_state.messages = []

try:
    engine = load_engine()
    engine_ready = True
except Exception as e:
    engine_ready = False
    st.error(
        f"Could not initialize the RAG engine. "
        f"Ensure the FAISS index has been built by running: python3 ingest.py\n\n"
        f"Details: {e}"
    )

for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and msg.get("sources"):
            with st.expander("📄 Source Documents"):
                for src in msg["sources"]:
                    st.markdown(f"- `{src}`")
        if msg["role"] == "assistant":
            cols = st.columns([1, 1, 10])
            if cols[0].button("👍", key=f"up_{i}"):
                log_feedback(msg.get("question", ""), msg["content"], "up")
                st.toast("Feedback recorded.")
            if cols[1].button("👎", key=f"down_{i}"):
                log_feedback(msg.get("question", ""), msg["content"], "down")
                st.toast("Feedback recorded. Flagged for review.")

if engine_ready:
    prompt = st.chat_input("Ask about identity governance policy, controls, or standards...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Retrieving grounded answer..."):
                try:
                    result = engine.generate(prompt)
                    answer = result["answer"]
                    sources = result["sources"]
                except Exception as e:
                    answer = f"Error generating answer: {e}"
                    sources = []

            st.markdown(answer)
            if sources:
                with st.expander("📄 Source Documents"):
                    for src in sources:
                        st.markdown(f"- `{src}`")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources,
            "question": prompt,
        })
        st.rerun()
