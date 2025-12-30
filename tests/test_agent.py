from app.agent import Agent

def test_agent_response():
    agent = Agent()
    response = agent.run("Hello")
    assert response is not None
