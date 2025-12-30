import os
from chromadb.config import Settings as ChromaSettings
kb_client = Client(ChromaSettings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_db"))
if kb_collection is None:
try:
kb_collection = kb_client.get_collection("agentic_kb")
except Exception:
kb_collection = kb_client.create_collection("agentic_kb")
return kb_collection




def run_agent(query: str, timeout: int = 20) -> Dict[str, Any]:
"""A small coordinator routine that:
- retrieves context
- calls LLM with a clear system message + tool invocations
- returns structured response
"""
with tracer.start_as_current_span("run_agent"):
start = time.time()
kb = get_kb()
# Retrieval
retrieval = search_knowledgebase(query, kb)
logger.info("retrieval done", extra={"query": query})


# Build a short prompt
system = SystemMessagePromptTemplate.from_template(
"You are AgenticAssistant: answer concisely and, when appropriate, call tools."
)
human = HumanMessagePromptTemplate.from_template("User asked: {query}\nUse retrieval: {retrieval}")
prompt = ChatPromptTemplate.from_messages([system, human])
inp = prompt.format_prompt(query=query, retrieval=retrieval).to_messages()


# Call LLM with a timeout
try:
resp = llm(inp)
except Exception as e:
logger.error("LLM call failed: %s", e)
return {"error": f"llm_error: {e}"}


# For demo: naive tool detection (in prod use a proper tool-invocation protocol)
text = resp.content if hasattr(resp, "content") else str(resp)


# Simple heuristic: if message contains `CALC:` run calculator tool
if "CALC:" in text:
expr = text.split("CALC:", 1)[1].strip()
calc_res = run_calc(expr)
else:
calc_res = None


elapsed = time.time() - start
return {
"query": query,
"llm_response": text,
"calc": calc_res,
"elapsed": elapsed,
"retrieval_preview": retrieval["top_hits"] if retrieval else [],
}
