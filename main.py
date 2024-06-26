import streamlit as st

from palm_langchian_qa_system import initialize_chroma_vector_store, get_qa_chain
# Streamlit UI
st.title("FAQ QA 🤔 System for Codebasics ")

st.write("This is a question answering system powered by Google Palm and LangChain.")
# Displaying the brain icon


if st.button('Initialize Vector Store'):
    initialize_chroma_vector_store()
    st.success("Chroma vector store initialized and persisted successfully.")

question = st.text_input("Enter your question:")


if st.button('Get Answer'):
    chain = get_qa_chain()
    if question:
        response = chain({"query": question})
        #  or --> response = chain(question)

        answer = response['result']
        st.subheader("Answer")
        st.write( answer)
        #st.write("Source Documents:", response['source_documents'])
    else:
        st.warning("Please enter a question.")

