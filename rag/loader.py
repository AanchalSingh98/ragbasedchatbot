from langchain_community.document_loaders import PyPDFLoader

def load_documents(files):

    docs = []

    for file in files:

        loader = PyPDFLoader(file)

        docs.extend(
            loader.load()
        )

    return docs