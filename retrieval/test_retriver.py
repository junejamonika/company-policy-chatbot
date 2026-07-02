from retrieval.retriever import get_retriever


def main():

    retriever = get_retriever()

    while True:

        question = input("\nQuestion: ")

        if question.lower() == "exit":
            break

        docs = retriever.invoke(question)

        print("\nRetrieved Documents")
        print("=" * 80)

        for i, doc in enumerate(docs, start=1):

            print(f"\nChunk {i}")
            print("-" * 40)

            print(doc.page_content[:500])

            print("\nMetadata")

            print(doc.metadata)


if __name__ == "__main__":
    main()