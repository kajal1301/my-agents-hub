from typing import Dict, List, Optional, TypedDict
from pydantic import BaseModel

# Global graph state for LangGraph
class GraphState(TypedDict, total=False):
    user_prompt: str
    is_engineering: bool
    questions: List[str]
    answers: Dict[str, str]
    plan: Dict  # project plan JSON
    architecture: Dict  # architecture JSON
    files: List[Dict]  # [{path, purpose}]
    code_artifacts: List[Dict]  # [{path, content}]
    status: str  # display status

# Schemas the model will fill
class PlanSchema(BaseModel):
    project_name: str
    description: str
    tech_stack: List[str]
    features: List[str]
    files: List[Dict]  # {path, purpose}

class ArchitectureSchema(BaseModel):
    diagram_uml: str
    components: List[Dict]  # {name, responsibility, depends_on}
    data_models: List[Dict]  # {name, fields}
    build_run_instructions: str

class FileCode(BaseModel):
    path: str
    content: str
