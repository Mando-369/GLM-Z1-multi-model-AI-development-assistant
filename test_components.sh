# Create test_components.sh
#!/bin/bash

case "$1" in
    "ollama")
        echo "Testing Ollama models..."
        echo "What is FAUST?" | ollama run codellama:13b
        ;;
    "chromadb")
        echo "Testing ChromaDB..."
        python test_chromadb_safe.py
        ;;
    "hrm")
        echo "Testing HRM..."
        python -c "import torch; print(f'MPS available: {torch.backends.mps.is_available()}')"
        ;;
    "streamlit")
        echo "Testing Streamlit..."
        streamlit run main.py --server.headless true
        ;;
    *)
        echo "Usage: $0 {ollama|chromadb|hrm|streamlit}"
        ;;
esac