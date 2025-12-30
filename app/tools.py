from typing import Dict


# Tools are small functions that the agent can call. Keep them minimal and well-sandboxed.


def search_knowledgebase(query: str, kb) -> Dict:
"""Simple retrieval function that queries the vector store (kb) and returns top hits."""
results = kb.similarity_search(query, k=3)
return {"query": query, "top_hits": [r.page_content for r in results]}




def run_calc(expression: str) -> Dict:
"""Very small calculator tool. Do not use eval on raw user input in prod — this is a demo.
In production, parse expressions safely.
"""
try:
# limited namespace
allowed = {"__builtins__": {}}
result = eval(expression, allowed, {})
return {"expression": expression, "result": result}
except Exception as e:
return {"error": str(e)}
