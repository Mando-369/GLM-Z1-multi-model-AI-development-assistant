# Create: download_python_docs.py
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time

def download_python_documentation():
    docs_dir = Path("./python_documentation")
    docs_dir.mkdir(exist_ok=True)
    
    print("🐍 Downloading Python documentation...")
    
    # Key Python documentation URLs
    python_urls = [
        "https://docs.python.org/3/tutorial/",
        "https://docs.python.org/3/library/",
        "https://docs.python.org/3/reference/",
        "https://docs.python.org/3/howto/",
        
        # Popular Python libraries
        "https://numpy.org/doc/stable/user/",
        "https://pandas.pydata.org/docs/user_guide/",
        "https://matplotlib.org/stable/users/index.html",
        "https://docs.scipy.org/doc/scipy/tutorial/",
        "https://scikit-learn.org/stable/user_guide.html",
        
        # Web frameworks
        "https://docs.djangoproject.com/en/stable/",
        "https://flask.palletsprojects.com/en/stable/",
        "https://fastapi.tiangolo.com/tutorial/",
    ]
    
    for i, url in enumerate(python_urls):
        try:
            print(f"📥 [{i+1}/{len(python_urls)}] Downloading: {url}")
            
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
            response = requests.get(url, timeout=15, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Clean content
            for element in soup(["nav", "header", "footer", "aside", "script", "style"]):
                element.decompose()
            
            content = soup.find('main') or soup.find('div', class_='body') or soup.find('body')
            
            if content:
                filename = url.split('//')[-1].replace('/', '_').replace('.', '_') + ".txt"
                filepath = docs_dir / filename
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Source: {url}\n{'='*80}\n\n")
                    f.write(content.get_text(separator='\n', strip=True))
                
                print(f"✅ Saved: {filename}")
            
            time.sleep(2)
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    return docs_dir

if __name__ == "__main__":
    download_python_documentation()
