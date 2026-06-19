from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    for i, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = i

    return chunks