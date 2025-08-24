import streamlit as st
from multi_model_system import MultiModelGLMSystem
from ui_components import (
    render_project_management,
    render_model_selection,
    render_sidebar,
    render_chat_interface,
)


def main():
    st.set_page_config(
        page_title="Multi-Model GLM Assistant",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("🤖🎵 Multi-Model GLM Assistant: GLM-Z1 + Specialists")

    # Initialize system
    if "multi_glm_system" not in st.session_state:
        with st.spinner("Initializing multi-model system..."):
            st.session_state.multi_glm_system = MultiModelGLMSystem()

    # Render UI components
    selected_project = render_project_management(st.session_state.multi_glm_system)
    selected_model, use_context = render_model_selection(
        st.session_state.multi_glm_system
    )
    render_sidebar(st.session_state.multi_glm_system)
    render_chat_interface(
        st.session_state.multi_glm_system, selected_model, use_context, selected_project
    )

    # Instructions
    with st.expander("ℹ️ How to Use the Enhanced System"):
        st.markdown(
            """
## 📁 **Project Management**
- **Create projects** to organize different coding tasks
- **Switch between projects** to maintain separate chat histories
- **Each project** maintains its own conversation context

## 📂 **Subfolder Organization**
- **Choose a subfolder** before uploading files
- **Files are automatically organized** by subject
- **Enhanced metadata** helps AI models understand context

## 🔄 **Bulk Operations**
- **"Scan All Subfolders"**: Process all existing files in uploads/
- **"Folder Stats"**: See file counts by category

## 🎯 **Subject Categories**
- **🎵 FAUST**: DSP code, examples, libraries
- **💻 C++**: C++ projects, documentation, reference
- **🐍 Python**: Python projects, libraries, tutorials
- **🎵 JUCE**: JUCE framework, audio applications
- **🔊 DSP**: Theory, algorithms, papers
- **📊 General**: Mixed documentation
- **🖼️ Images**: Diagrams, screenshots (with OCR)
- **📝 Documentation**: Technical docs and manuals

## 🤖 **AI Model Benefits**
- **Context-aware responses** based on file organization
- **Project-specific knowledge** accumulation
- **Cross-model collaboration** within projects
- **Persistent learning** from your conversations

## 🔧 **Model Management**
- **Check Model Availability**: Verify which Ollama models are installed
- **Install missing models** with the provided `ollama pull` commands
- **Model status indicators** show loading state
"""
        )


if __name__ == "__main__":
    main()
