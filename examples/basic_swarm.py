from a_cli_tool.agents import Agent
from a_cli_tool.orchestrator import Orchestrator

orch = Orchestrator()
orch.register(Agent(name="planner", skills=["plan"]))
orch.register(Agent(name="executor", skills=["execute", "summarize"]))

result = orch.run(goal="Demo workflow")
print(result.summary)
print(result.steps)
