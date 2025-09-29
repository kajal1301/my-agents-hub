"""
Agents package for CoderBuddy
-----------------------------

This package contains all of the agent-related logic for CoderBuddy:

Modules:
    model : Groq API client setup (OpenAI-compatible)
    state        : Shared graph state and Pydantic schemas
    nodes        : Verifier, Requirements, Planner, Architect, Coder nodes
    graph        : LangGraph definition connecting all nodes
    file_writer  : Utilities to write and zip generated projects

Typical usage example:

    from agents import build_graph, GraphState

    graph = build_graph()
    result = graph.invoke(GraphState(user_prompt="Create a Streamlit app"))
"""

from .model import groq_client, MODEL_NAME
from .state import GraphState, PlanSchema, ArchitectureSchema, FileCode
from .nodes import verifier_node, requirements_node, planner_node, architect_node, coder_node
from .graph import build_graph
from .filewriter import write_project

__all__ = [
    "groq_client",
    "MODEL_NAME",
    "GraphState",
    "PlanSchema",
    "ArchitectureSchema",
    "FileCode",
    "verifier_node",
    "requirements_node",
    "planner_node",
    "architect_node",
    "coder_node",
    "build_graph",
    "write_project",
]
