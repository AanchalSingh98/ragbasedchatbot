def retrieve(
    query,
    db
):

    docs = db.similarity_search(
        query,
        k=10
    )

    context = []

    pages = []

    for d in docs:

        context.append(
            d.page_content
        )

        pages.append(
            str(
                d.metadata.get(
                    "page",
                    0
                ) + 1
            )
        )

    return (
        "\n\n".join(context),
        list(set(pages))
    )