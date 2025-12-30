import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)




def test_run_agent_validation():
r = client.post("/run_agent", json={"query": ""})
assert r.status_code == 400




@pytest.mark.parametrize("q", ["What is 2+2?", "Explain recursion in simple words"])
def test_run_agent_happy(q):
r = client.post("/run_agent", json={"query": q})
assert r.status_code == 200
data = r.json()
assert "llm_response" in data
