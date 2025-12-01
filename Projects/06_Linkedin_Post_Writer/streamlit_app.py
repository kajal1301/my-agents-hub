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
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .post-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #0077b5;
        margin: 1rem 0;
    }
    .key-point {
        background-color: #e8f4f8;
        padding: 0.8rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border-left: 3px solid #0077b5;
    }
    .stButton>button {
        width: 100%;
        background-color: #0077b5;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #005885;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">💼 LinkedIn Post Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Content Creation for Professional Networking</p>', unsafe_allow_html=True)

# Sidebar for additional options
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("---")
    
    tone_options = [
        "Professional",
        "Formal",
        "Inspirational",
        "Educational",
        "Humorous",
        "Casual",
        "Conversational"
    ]
    
    default_tone = st.selectbox(
        "Select Tone",
        tone_options,
        index=0,
        help="Choose the tone for your LinkedIn post"
    )
    
    target_audience_options = [
        "General",
        "Tech Professionals",
        "Business Leaders",
        "Entrepreneurs",
        "Students",
        "Job Seekers",
        "Industry Experts",
        "Startups",
        "Investors"
    ]
    
    default_audience = st.selectbox(
        "Target Audience",
        target_audience_options,
        index=0,
        help="Select your target audience"
    )
    
    st.markdown("---")
    st.markdown("### 📝 How it works:")
    st.markdown("""
    1. Enter your topic
    2. Choose tone and audience
    3. Click Generate
    4. Get your optimized post!
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Tips:")
    st.markdown("""
    - Be specific with your topic
    - Choose appropriate tone
    - Review and customize the output
    - Add personal touches before posting
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Create Your Post")
    
    # Topic input
    topic = st.text_area(
        "Enter your topic:",
        placeholder="e.g., The future of AI in healthcare, Tips for remote work productivity, Building a strong professional network...",
        height=100,
        help="Describe what you want to write about"
    )
    
    # Generate button
    generate_button = st.button("🚀 Generate Post", type="primary", use_container_width=True)

with col2:
    st.header("📊 Post Stats")
    if topic:
        word_count = len(topic.split())
        st.metric("Topic Words", word_count)
        st.info("💡 Tip: Be specific and clear about your topic for better results!")

# Processing and results
if generate_button:
    if not topic or not topic.strip():
        st.error("❌ Please enter a topic to generate a post.")
    else:
        # Show progress
        with st.spinner("🤖 Generating your LinkedIn post... This may take a moment."):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Simulate progress updates
                status_text.text("📋 Analyzing topic...")
                progress_bar.progress(20)
                time.sleep(0.5)
                
                status_text.text("🎯 Extracting key points...")
                progress_bar.progress(40)
                time.sleep(0.5)
                
                status_text.text("✍️ Drafting post...")
                progress_bar.progress(60)
                time.sleep(0.5)
                
                status_text.text("✨ Optimizing for engagement...")
                progress_bar.progress(80)
                
                # Generate the post
                result = create_agent(
                    topic=topic.strip(),
                    tone=default_tone,
                    target_audience=default_audience
                )
                
                progress_bar.progress(100)
                status_text.text("✅ Post generated successfully!")
                time.sleep(0.5)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Store results in session state
                st.session_state['result'] = result
                st.session_state['topic'] = topic.strip()
                st.session_state['tone'] = default_tone
                st.session_state['audience'] = default_audience
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.exception(e)

# Display results
if 'result' in st.session_state:
    result = st.session_state['result']
    
    st.markdown("---")
    st.header("✨ Generated Content")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["📄 Final Post", "📋 Key Points", "📊 Details"])
    
    with tab1:
        st.subheader("🎯 Optimized LinkedIn Post")
        
        final_post = result.get("final_post", result.get("draft_post", "No post generated"))
        
        # Display post in a styled container
        st.markdown(f'<div class="post-container">{final_post.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
        
        # Copy button
        st.markdown("---")
        col_copy, col_download = st.columns(2)
        
        with col_copy:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(final_post, language=None)
                st.success("✅ Post copied! You can now paste it on LinkedIn.")
        
        with col_download:
            # Download as text file
            st.download_button(
                label="💾 Download as .txt",
                data=final_post,
                file_name=f"linkedin_post_{int(time.time())}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # Post statistics
        st.markdown("---")
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        
        word_count = len(final_post.split())
        char_count = len(final_post)
        hashtag_count = final_post.count('#')
        
        with col_stats1:
            st.metric("Word Count", word_count)
        with col_stats2:
            st.metric("Character Count", char_count)
        with col_stats2:
            st.metric("Hashtags", hashtag_count)
    
    with tab2:
        st.subheader("🔑 Key Points")
        
        key_points = result.get("key_points", [])
        
        if key_points:
            for i, point in enumerate(key_points, 1):
                st.markdown(f'<div class="key-point"><strong>{i}. {point}</strong></div>', unsafe_allow_html=True)
        else:
            st.info("No key points generated.")
    
    with tab3:
        st.subheader("📊 Generation Details")
        
        col_detail1, col_detail2 = st.columns(2)
        
        with col_detail1:
            st.markdown("### Topic Information")
            st.write(f"**Topic:** {st.session_state.get('topic', 'N/A')}")
            st.write(f"**Tone:** {st.session_state.get('tone', 'N/A')}")
            st.write(f"**Target Audience:** {st.session_state.get('audience', 'N/A')}")
        
        with col_detail2:
            st.markdown("### Post Information")
            st.write(f"**Draft Generated:** {'Yes' if result.get('draft_post') else 'No'}")
            st.write(f"**Final Post Generated:** {'Yes' if result.get('final_post') else 'No'}")
            st.write(f"**Key Points Count:** {len(result.get('key_points', []))}")
        
        # Show draft post if available
        if result.get('draft_post'):
            with st.expander("📝 View Draft Post"):
                st.text_area("Draft Post", result.get('draft_post'), height=200, disabled=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>💼 LinkedIn Post Generator | Powered by AI & LangGraph</p>
        <p><small>Remember to review and personalize your post before publishing!</small></p>
    </div>
    """,
    unsafe_allow_html=True
)

