from a_cli_tool.agents import Agent

def test_agent_matching() -> None:
    agent = Agent(name="planner", skills=["plan"])
    assert agent.can_handle("plan backlog")
