#!/usr/bin/env python3
"""Test that reorganization didn't break anything"""

import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    """Test all imports work"""
    try:
        from src.core import MultiModelGLMSystem, ProjectManager, FileProcessor, ContextEnhancer
        from src.ui import EditorUI, FileEditor, FileBrowser
        from src.ui import render_project_management, render_model_selection, render_sidebar, render_chat_interface
        from src.integrations import HRMLocalWrapper, HRMDecomposition, SubTask
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_streamlit_launch():
    """Test if main.py would launch"""
    try:
        # Just test the imports without running streamlit
        import main
        print("✅ main.py imports successful")
        return True
    except Exception as e:
        print(f"❌ main.py failed: {e}")
        return False

def test_system_initialization():
    """Test basic system initialization"""
    try:
        from src.core import MultiModelGLMSystem
        # Don't actually initialize it as it requires ChromaDB
        print("✅ MultiModelGLMSystem can be imported")
        return True
    except Exception as e:
        print(f"❌ System initialization failed: {e}")
        return False

def test_ui_components():
    """Test UI components can be imported"""
    try:
        from src.ui import render_project_management, render_model_selection
        print("✅ UI components can be imported")
        return True
    except Exception as e:
        print(f"❌ UI components failed: {e}")
        return False

def test_integrations():
    """Test HRM integration imports"""
    try:
        from src.integrations import HRMLocalWrapper
        print("✅ HRM integration can be imported")
        return True
    except Exception as e:
        print(f"❌ HRM integration failed: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing reorganization...")
    print("-" * 50)
    
    results = []
    results.append(test_imports())
    results.append(test_streamlit_launch())
    results.append(test_system_initialization())
    results.append(test_ui_components())
    results.append(test_integrations())
    
    print("-" * 50)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 All tests passed! ({passed}/{total})")
        print("✅ Reorganization successful - all imports working correctly")
    else:
        print(f"⚠️  Some tests failed ({passed}/{total})")
        print("❌ Reorganization needs fixes")
    
    sys.exit(0 if passed == total else 1)