# Multi-Model GLM Assistant with Integrated Code Editor

## 🚀 Enhanced Features

✅ **GLM-Z1 32B model** running locally via Ollama  
✅ **Multi-model system**: GLM-Z1 (reasoning) + Code Llama (FAUST specialist) + DeepSeek (fast coding)  
✅ **Integrated Code Editor** with syntax highlighting for 20+ languages  
✅ **AI-Powered Code Editing** with change highlighting and diff view  
✅ **Project-based organization** with separate chat histories  
✅ **File browser** with include/exclude patterns  
✅ **Direct file editing** - no copy-paste needed!  
✅ **Persistent knowledge base** using ChromaDB  
✅ **FAUST documentation integration** for specialist knowledge  

## 📋 Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed ([Download here](https://ollama.ai/))
3. **Tesseract OCR** for image processing (optional but recommended)

### Installing Tesseract (Optional)
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```

## 🛠️ Installation Steps

### 1. Clone/Download the Project
```bash
git clone <your-repo-url>
cd multi-model-glm-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and Setup Ollama Models

#### Install Required Models
```bash
# Main reasoning model
ollama pull JollyLlama/GLM-Z1-32B-0414-Q4_K_M

# FAUST/DSP specialist
ollama pull codellama:13b

# Fast coding assistant
ollama pull deepseek-coder:6.7b

# Embedding model for knowledge base
ollama pull nomic-embed-text
```

#### Verify Model Installation
```bash
ollama list
```
You should see all four models listed.

### 5. Create Required Directories
```bash
mkdir -p uploads projects knowledge_db faust_documentation
```

## 🎯 Quick Start

### 1. Launch the Application
```bash
streamlit run main.py
```

### 2. First-Time Setup
1. **Check Model Status** - Use the "Check Model Availability" button in the sidebar
2. **Create a Project** - Click "➕ New Project" and create your first project
3. **Upload Documentation** - Go to Knowledge Base tab and upload your files

### 3. Start Coding!
1. **Switch to Code Editor tab**
2. **Create or open files** using the file browser
3. **Ask AI to modify your code** with specific instructions
4. **Review highlighted changes** in the diff viewer
5. **Accept or reject** AI suggestions
6. **Save directly** to your files

## 📝 Usage Examples

### Basic Code Editing Workflow

1. **Open a Python file** in the Code Editor tab
2. **Select your code** and ask AI: "Add docstrings to all functions"
3. **Review the changes** in the highlighted diff view:
   - 🟢 **Green lines** = AI additions
   - 🔴 **Red lines** = AI deletions  
   - 🔵 **Blue lines** = AI modifications
4. **Accept or reject** the changes
5. **Save directly** to your file

### FAUST DSP Development

1. **Create a new .dsp file** 
2. **Ask Code Llama**: "Create a stereo reverb effect with adjustable room size"
3. **Review the FAUST code** with syntax highlighting
4. **Iterate with AI** to refine the algorithm
5. **Save and test** your DSP code

### Project Organization

1. **Create specialized projects** for different codebases
2. **Set include/exclude patterns** to focus on relevant files
3. **Use project-specific chat history** for context
4. **Organize files** with the integrated file browser

## 🔧 Configuration

### File Filtering Patterns

**Default Include Patterns:**
- `*.py` (Python files)
- `*.cpp`, `*.h`, `*.hpp` (C++ files)  
- `*.dsp`, `*.lib`, `*.fst` (FAUST files)
- `*.txt`, `*.md` (Documentation)
- `*.json` (Configuration files)

**Default Exclude Patterns:**
- `__pycache__`, `*.pyc` (Python cache)
- `.git` (Git repository data)
- `node_modules` (Node.js dependencies)
- `*.exe`, `*.dll` (Binaries)

### Editor Settings

- **Theme**: Monokai (dark theme optimized for code)
- **Font Size**: 14px (adjustable per project)
- **Tab Size**: 4 spaces
- **Language Detection**: Automatic based on file extension

## 🎵 FAUST Integration

### Specialized Features for Audio DSP

1. **FAUST Documentation**: Load complete FAUST library documentation
2. **Code Llama Specialist**: Trained specifically for FAUST syntax and DSP concepts
3. **Quick Actions**: Pre-built prompts for common FAUST patterns:
   - Basic oscillators
   - Filter designs  
   - Effect chains
4. **Syntax Support**: Full highlighting for `.dsp` and `.lib` files

### Loading FAUST Documentation
```bash
# Run the documentation downloader
python download_faust_docs_complete.py
```

Then use the "📥 Load FAUST Docs" button in the Knowledge Base tab.

## 🔍 Troubleshooting

### Model Loading Issues

**Problem**: "❌ Model Missing" errors  
**Solution**: 
```bash
# Re-pull the missing model
ollama pull <model-name>

# Restart Ollama service
ollama serve
```

### Code Editor Not Loading

**Problem**: Blank editor or loading issues  
**Solution**:
1. Clear browser cache
2. Restart Streamlit: `Ctrl+C` then `streamlit run main.py`
3. Check console for JavaScript errors

### File Permission Errors

**Problem**: Cannot save files  
**Solution**:
```bash
# Fix permissions (Unix/Linux/macOS)
chmod -R 755 projects/
chmod -R 755 uploads/

# On Windows, run as administrator if needed
```

### Memory Issues with Large Models

**Problem**: System running slow or out of memory  
**Solutions**:
1. **Use smaller models**:
   ```bash
   ollama pull codellama:7b  # Instead of 13b
   ```
2. **Increase system swap space**
3. **Close other applications** while running GLM-Z1

## 📊 System Requirements

### Minimum Requirements
- **RAM**: 16GB (for GLM-Z1 32B model)
- **Storage**: 50GB free space (for models and data)
- **CPU**: Modern multi-core processor
- **GPU**: Optional but recommended for faster inference

### Recommended Requirements  
- **RAM**: 32GB+ 
- **GPU**: NVIDIA RTX 4070+ or AMD equivalent
- **Storage**: SSD with 100GB+ free space

## 🚀 Advanced Usage

### Custom Model Integration

Add new models to `multi_model_system.py`:

```python
self.models = {
    "GLM-Z1 (Reasoning & General)": "JollyLlama/GLM-Z1-32B-0414-Q4_K_M",
    "Code Llama (FAUST Specialist)": "codellama:13b", 
    "DeepSeek Coder (Fast DSP)": "deepseek-coder:6.7b",
    "Your Custom Model": "your-model-name"  # Add this
}
```

### Extending File Type Support

Modify `editor_ui.py` to add new language modes:

```python
language_map = {
    '.py': 'python',
    '.your_ext': 'your_language_mode',  # Add this
    # ... existing mappings
}
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Test your changes** thoroughly
4. **Submit a pull request**

## 📚 Additional Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [FAUST Documentation](https://faustdoc.grame.fr/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)

## 🐛 Reporting Issues

If you encounter problems:

1. **Check the console** for error messages
2. **Verify model installation** with `ollama list`
3. **Create an issue** with:
   - System information
   - Error messages
   - Steps to reproduce
   - Screenshots (if applicable)

---

**Happy Coding with AI! 🤖✨**

The integrated code editor makes it seamless to iterate on your projects with AI assistance while maintaining full control over your codebase.