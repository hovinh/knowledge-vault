#### Langchain

```python
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import VertexAIEmbeddings
from difflib import SequenceMatcher
from neo4j import GraphDatabase
from langchain.vectorstores import FAISS, Chroma
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


def neo4j_check_data_uploaded():
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            result = session.run("MATCH (c:CSFA_Chunk) RETURN COUNT(c) AS count")
            count = result.single()["count"]
            return count > 0

def neo4j_inject_vector(text, embedding, order):
    chunk_query = """
        CREATE (chunk:CSFA_Chunk {text:$text, embedding:$embedding, order:$order})
    """
    graph.execute_query(chunk_query, text=text, embedding=text_embedding, order=order)

def neo4j_search(search_count=5):
    # returns the most similar text to the prompt from the database
    search_query = """
        CALL db.index.vector.queryNodes('chunk_embedding', $count, $query_vector) YIELD node, score
        RETURN node ORDER BY score DESC
    """
    results, _, _ = graph.execute_query(search_query, count=search_count, query_vector=prompt_query_embedding)
    _results = []
    for result in results:
        _results.append({
            "text": result["node"]["text"].replace("\n", " ")
        })
    combined_text = ' '.join(result["text"] for result in _results)
    return combined_text


```

#### RAG

