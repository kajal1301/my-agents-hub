from keys import llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from typing import Annotated, Literal
from typing_extensions import TypedDict
import operator
from langgraph.graph import StateGraph
from langgraph.constants import START, END
from langchain_core.messages import HumanMessage

import json
import sys

# Linkedin Post Generator Agent State
class PostGeneratorState(TypedDict):
    topic: str
    tone: str
    target_audience: str
    key_points: list[str]
    draft_post: str
    final_post: str
    messages: Annotated[list, operator.add]

def extract_topic(state: PostGeneratorState) -> dict:
    """Extract the topic from the state"""
    message = HumanMessage(content=f"""Analyze the topic for Linkedin Post and provide:
    1. Main Topic
    2. Suggested Tone: Professional, Formal, Inspirational, educational, humerous, etc)
    3. Suggested Target Audience

    Topic: {state['topic']}
    Return the JSON with keys: main_topic, tone, target_audience
        """)
    response = llm.invoke([message])
    try:
        result = json.loads(response.content)
        return {
            "messages": [message, response],
            "topic": result.get("main_topic", state['topic']),
            "tone": result.get("tone", "Professional"),
            "target_audience": result.get("target_audience", "General"),
        }
    except json.JSONDecodeError:
        return {
            "messages": [message, response],
            "tone": "Professional",
            "target_audience": "General",
        }

def generate_key_points(state: PostGeneratorState) -> dict:
    """Generate the key points for the post"""
    message = HumanMessage(content=f"""Generate 3-5 key points for the post about {state['topic']}.
    Tone: {state['tone']}
    Target Audience: {state['target_audience']}

    Return the JSON with keys: key_points(array of strings)
    """)
    response = llm.invoke([message])
    try:
        result = json.loads(response.content)
        return {
            "messages": [message, response],
            "key_points": result.get("key_points"),
        }
    except json.JSONDecodeError:
        return {
            "messages": [message, response],
            "key_points": ["No key points generated"],
        }

def draft_post(state: PostGeneratorState) -> dict:
    """Draft the post"""
    key_points_str= '\n'.join(state['key_points'])

    message = HumanMessage(content=f"""Create the linkedin post with these specifications:
    Topic: {state['topic']}
    Tone: {state['tone']}
    Target Audience: {state['target_audience']}
    Key Points: {key_points_str}

    Requirements:
    - 150-300 words
    - Engaging opening line
    - Include relevant hashtags
    - End with a call-to-action
    - Professional but personable tone
    
    Return the complete post ready to publish.
    """
    )
    response = llm.invoke([message])
    return {
        "messages": [message, response],
        "draft_post": response.content,
    }

def optimize_post(state: PostGeneratorState) -> dict:
    """Optimize the post for the target audience"""
    message = HumanMessage(content=f"""Review and optimize this LinkedIn post for maximum engagement:

{state['draft_post']}

Improvements to consider:
- Strengthen the hook/opening
- Improve formatting with line breaks
- Enhance call-to-action
- Ensure proper hashtag usage (5-10 relevant ones)
- Check for professionalism and clarity

Return the optimized final version ready to post.
    """)
    response = llm.invoke([message])
    return {
        "messages": [message, response],
        "final_post": response.content,
    }

def create_agent(topic: str, tone: str = None, target_audience: str = None):
    """Create the agent for the linkedin post generator"""

    # Build the graph
    workflow = StateGraph(PostGeneratorState)

    # Add nodes
    workflow.add_node("extract_topic", extract_topic)
    workflow.add_node("generate_key_points", generate_key_points)
    workflow.add_node("draft_post", draft_post)
    workflow.add_node("optimize_post", optimize_post)

    # Define edges
    workflow.add_edge(START, "extract_topic")
    workflow.add_edge("extract_topic", "generate_key_points")
    workflow.add_edge("generate_key_points", "draft_post")
    workflow.add_edge("draft_post", "optimize_post")
    workflow.add_edge("optimize_post", END)

    # Compile the graph
    agent = workflow.compile()

    # Initial State
    initial_state = {
        "topic": topic,
        "tone": tone or "Professional",
        "target_audience": target_audience or "General",
        "key_points": [],
        "draft_post": "",
        "final_post": "",
        "messages": []
    }

    # Run the agent
    result = agent.invoke(initial_state)
    return result


def main():
    """Main function to run the LinkedIn post generator"""
    print("=" * 80)
    print("LINKEDIN POST GENERATOR AGENT")
    print("=" * 80)
    print()
    
    # Get topic from command line argument or user input
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:]).strip()
    else:
        try:
            topic = input("Enter the topic for your LinkedIn post: ").strip()
        except EOFError:
            print("No input available. Using example topic...")
            topic = "The future of AI in software development"
    
    if not topic:
        print("No topic provided. Exiting.")
        return
    
    print()
    print(f"Topic: {topic}")
    print("Generating LinkedIn post...")
    print()
    
    # Generate the post
    result = create_agent(topic=topic)
    
    # Display the result
    print("=" * 80)
    print("FINAL LINKEDIN POST")
    print("=" * 80)
    print()
    print(result.get("final_post", result.get("draft_post", "No post generated")))
    print()
    print("=" * 80)
    print("KEY POINTS")
    print("=" * 80)
    for i, point in enumerate(result.get("key_points", []), 1):
        print(f"{i}. {point}")


if __name__ == "__main__":
    main()


