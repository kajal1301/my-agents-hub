from langgraph.graph import StateGraph, START, END
from .state import GraphState
from .nodes import verifier_node, requirements_node, planner_node, architect_node, coder_node

def build_graph():
    g = StateGraph(GraphState)

    g.add_node("verifier", verifier_node)
    g.add_node("requirements", requirements_node)
    g.add_node("planner", planner_node)
    g.add_node("architect", architect_node)
    g.add_node("coder", coder_node)

    # Flow:
    g.add_edge(START, "verifier")
    g.add_edge("verifier", "requirements")
    g.add_edge("requirements", "planner")
    g.add_edge("planner", "architect")
    g.add_edge("architect", "coder")
    g.add_edge("coder", END)

    return g.compile()
