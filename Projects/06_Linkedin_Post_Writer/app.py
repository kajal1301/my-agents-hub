import streamlit as st
from PostGeneratorAgent import create_agent
import time

# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0077b5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #0077b5;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #005885;
    }
    .post-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #0077b5;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">💼 LinkedIn Post Generator</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for inputs
with st.sidebar:
    st.header("📝 Post Configuration")
    
    # Topic input
    topic = st.text_area(
        "Topic",
        placeholder="Enter the topic for your LinkedIn post...",
        height=100,
        help="Describe what you want to write about"
    )
    
    # Tone selection
    tone_options = [
        "Professional",
        "Formal",
        "Inspirational",
        "Educational",
        "Humorous",
        "Casual",
        "Motivational"
    ]
    tone = st.selectbox(
        "Tone (Optional)",
        options=["Auto-detect"] + tone_options,
        help="Select the tone for your post. Choose 'Auto-detect' to let the AI decide."
    )
    
    # Target audience input
    target_audience = st.text_input(
        "Target Audience (Optional)",
        placeholder="e.g., Software Developers, Entrepreneurs, Students",
        help="Specify your target audience or leave empty for general audience"
    )
    
    # Generate button
    generate_button = st.button("🚀 Generate Post", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    This tool uses AI to generate engaging LinkedIn posts based on your topic.
    
    **Features:**
    - Automatic topic analysis
    - Key points generation
    - Post drafting and optimization
    - Ready-to-publish format
    """)

# Main content area
if generate_button:
    if not topic or not topic.strip():
        st.error("⚠️ Please enter a topic for your LinkedIn post!")
    else:
        # Prepare parameters
        tone_param = None if tone == "Auto-detect" else tone
        target_audience_param = target_audience.strip() if target_audience and target_audience.strip() else None
        
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Simulate progress updates
            status_text.text("📊 Analyzing topic...")
            progress_bar.progress(25)
            
            # Generate the post
            result = create_agent(
                topic=topic.strip(),
                tone=tone_param,
                target_audience=target_audience_param
            )
            
            progress_bar.progress(100)
            status_text.text("✅ Post generated successfully!")
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
                
            # Display results
            st.success("🎉 Your LinkedIn post is ready!")
            
            # Create two columns for better layout
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("### 📄 Final Post")
                st.markdown('<div class="post-container">', unsafe_allow_html=True)
                st.markdown(result.get("final_post", result.get("draft_post", "No post generated")))
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Copy button functionality
                post_text = result.get("final_post", result.get("draft_post", ""))
                if post_text:
                    st.code(post_text, language=None)
            
            with col2:
                st.markdown("### 📋 Post Details")
                
                # Topic
                st.markdown("**Topic:**")
                st.info(result.get("topic", topic))
                
                # Tone
                st.markdown("**Tone:**")
                st.info(result.get("tone", "Professional"))
                
                # Target Audience
                st.markdown("**Target Audience:**")
                st.info(result.get("target_audience", "General"))
                
                # Key Points
                key_points = result.get("key_points", [])
                if key_points:
                    st.markdown("**Key Points:**")
                    for i, point in enumerate(key_points, 1):
                        st.markdown(f"{i}. {point}")
                
                # Show draft post in expander
                draft_post = result.get("draft_post", "")
                if draft_post and draft_post != result.get("final_post", ""):
                    with st.expander("📝 View Draft Post"):
                        st.markdown(draft_post)
                
                # Store in session state for potential download
                st.session_state['generated_post'] = result.get("final_post", result.get("draft_post", ""))
                st.session_state['key_points'] = result.get("key_points", [])
                
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

else:
    # Welcome message
    st.info("👈 **Get started:** Enter a topic in the sidebar and click 'Generate Post' to create your LinkedIn post!")
    
    # Example topics
    st.markdown("### 💡 Example Topics")
    st.markdown("Click on any example below to use it as your topic:")
    
    example_topics = [
        "The future of AI in software development",
        "Remote work best practices",
        "Building a personal brand on LinkedIn",
        "Tips for effective networking",
        "Career growth strategies"
    ]
    
    # Display example topics as selectable options
    selected_example = st.selectbox(
        "Choose an example topic (optional):",
        options=["None - I'll write my own"] + example_topics,
        key="example_selector"
    )
    
    if selected_example != "None - I'll write my own":
        st.info(f"💡 **Selected example:** {selected_example}")
        st.markdown("💬 You can copy this to the sidebar or modify it as needed!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; padding: 1rem;'>"
    "Powered by LangGraph & Groq AI | LinkedIn Post Generator"
    "</div>",
    unsafe_allow_html=True
)

