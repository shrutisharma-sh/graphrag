GRAPH_CONTEXT_PATH = "app/rag/documents/graph_context.txt"


def get_graph_context(query: str):
    """
    Retrieve graph-aware context.

    Later this function will query TigerGraph.
    Currently it loads structured graph knowledge.
    """

    try:
        with open(GRAPH_CONTEXT_PATH, "r", encoding="utf-8") as file:
            graph_context = file.read()

        return graph_context

    except Exception as e:
        return f"Graph retrieval error: {str(e)}"