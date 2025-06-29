import streamlit as st
from src.utils.arxiv_search import search_arxiv
from src.agents.gemini_summarizer import summarize

st.title("📚 Research Paper Finder & Summarizer")

query = st.text_input("Enter your research topic or keywords:", "")

max_papers = st.slider("Number of papers to fetch:", 1, 10, 5)

if st.button("Search and Summarize") and query:
    with st.spinner("Searching arXiv and summarizing papers..."):
        papers = search_arxiv(query, max_papers)
        if not papers:
            st.warning("No papers found. Try a different query.")
        else:
            for i, paper in enumerate(papers, 1):
                st.subheader(f"Paper {i}: {paper['title']}")
                st.write("**Abstract:**", paper['summary'])
                st.write(f"🔗 [Read Full Paper]({paper['link']})")
                summary = summarize(paper['summary'])
                st.write("**Summary:**", summary)
                st.markdown("---")
