# Create: download_faust_docs_complete.py
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import re

def clean_filename(filename):
    """Clean filename for safe file saving"""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_faust_documentation():
    docs_dir = Path("./faust_documentation")
    docs_dir.mkdir(exist_ok=True)
    
    print("🎵 Downloading comprehensive FAUST documentation...")
    
    # Site 1: FAUST Libraries (Most Important)
    libraries_urls = [
        "https://faustlibraries.grame.fr/",
        "https://faustlibraries.grame.fr/organization/",
        "https://faustlibraries.grame.fr/contributing/",
        "https://faustlibraries.grame.fr/libs/",  # Library index
        
        # Core Libraries (Essential for DSP)
        "https://faustlibraries.grame.fr/libs/basics/",
        "https://faustlibraries.grame.fr/libs/maths/", 
        "https://faustlibraries.grame.fr/libs/signals/",
        "https://faustlibraries.grame.fr/libs/oscillators/",
        "https://faustlibraries.grame.fr/libs/filters/",
        "https://faustlibraries.grame.fr/libs/envelopes/",
        "https://faustlibraries.grame.fr/libs/delays/",
        "https://faustlibraries.grame.fr/libs/reverbs/",
        "https://faustlibraries.grame.fr/libs/analyzers/",
        "https://faustlibraries.grame.fr/libs/noises/",
        
        # Advanced Libraries
        "https://faustlibraries.grame.fr/libs/physmodels/",
        "https://faustlibraries.grame.fr/libs/compressors/",
        "https://faustlibraries.grame.fr/libs/misceffects/",
        "https://faustlibraries.grame.fr/libs/vaeffects/",
        "https://faustlibraries.grame.fr/libs/phaflangers/",
        "https://faustlibraries.grame.fr/libs/routes/",
        "https://faustlibraries.grame.fr/libs/demos/",
        
        # Specialized Libraries
        "https://faustlibraries.grame.fr/libs/synths/",
        "https://faustlibraries.grame.fr/libs/spats/",
        "https://faustlibraries.grame.fr/libs/hoa/",
        "https://faustlibraries.grame.fr/libs/dx7/",
        "https://faustlibraries.grame.fr/libs/fds/",
        "https://faustlibraries.grame.fr/libs/wdmodels/",
        "https://faustlibraries.grame.fr/libs/webaudio/",
    ]
    
    # Site 2: FAUST Documentation (Syntax and Manual)
    manual_urls = [
        "https://faustdoc.grame.fr/",
        "https://faustdoc.grame.fr/manual/",
        "https://faustdoc.grame.fr/manual/introduction/",
        "https://faustdoc.grame.fr/manual/syntax/",
        "https://faustdoc.grame.fr/manual/primitives/",
        "https://faustdoc.grame.fr/manual/examples/",
        "https://faustdoc.grame.fr/tutorials/",
        "https://faustdoc.grame.fr/workshops/"
    ]
    
    all_urls = libraries_urls + manual_urls
    
    for i, url in enumerate(all_urls):
        try:
            print(f"📥 [{i+1}/{len(all_urls)}] Downloading: {url}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=15, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove navigation, ads, and other non-content
            for element in soup(["nav", "header", "footer", "aside", "script", "style"]):
                element.decompose()
            
            # Try to find main content
            content = (soup.find('main') or 
                      soup.find('article') or 
                      soup.find('div', class_='content') or
                      soup.find('div', id='content') or
                      soup.find('body'))
            
            if content:
                # Create filename from URL
                parsed_url = urlparse(url)
                if parsed_url.path == '/' or parsed_url.path == '':
                    filename = f"{parsed_url.netloc}_index"
                else:
                    filename = f"{parsed_url.netloc}_{parsed_url.path.replace('/', '_').strip('_')}"
                
                filename = clean_filename(filename) + ".txt"
                filepath = docs_dir / filename
                
                # Extract and clean text
                text_content = content.get_text(separator='\n', strip=True)
                
                # Add metadata
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Source URL: {url}\n")
                    f.write(f"Site: {parsed_url.netloc}\n")
                    f.write(f"Documentation Type: {'Library' if 'faustlibraries' in url else 'Manual'}\n")
                    f.write("="*80 + "\n\n")
                    f.write(text_content)
                
                print(f"✅ Saved: {filename} ({len(text_content)} chars)")
            
            # Be respectful to servers
            time.sleep(2)
            
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")
            continue
    
    print(f"\n🎉 FAUST documentation saved to: {docs_dir}")
    print("📊 Summary:")
    print(f"   - Libraries documentation: faustlibraries.grame.fr")
    print(f"   - Language manual: faustdoc.grame.fr") 
    print(f"   - Total files: {len(list(docs_dir.glob('*.txt')))}")
    
    return docs_dir

if __name__ == "__main__":
    download_faust_documentation()
