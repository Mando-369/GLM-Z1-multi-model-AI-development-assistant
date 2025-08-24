# Create: download_juce_docs.py
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time

def download_juce_documentation():
    docs_dir = Path("./juce_documentation")
    docs_dir.mkdir(exist_ok=True)
    
    print("🎵 Downloading JUCE documentation...")
    
    juce_urls = [
        "https://docs.juce.com/master/index.html",
        "https://docs.juce.com/master/tutorial_getting_started.html",
        
        # Core JUCE modules
        "https://docs.juce.com/master/group__juce__audio__basics.html",
        "https://docs.juce.com/master/group__juce__audio__devices.html",
        "https://docs.juce.com/master/group__juce__audio__formats.html",
        "https://docs.juce.com/master/group__juce__audio__processors.html",
        "https://docs.juce.com/master/group__juce__audio__utils.html",
        "https://docs.juce.com/master/group__juce__dsp.html",
        "https://docs.juce.com/master/group__juce__gui__basics.html",
        "https://docs.juce.com/master/group__juce__gui__extra.html",
        
        # Tutorials
        "https://docs.juce.com/master/tutorial_audio_processor_graph.html",
        "https://docs.juce.com/master/tutorial_simple_synth_noise.html",
        "https://docs.juce.com/master/tutorial_dsp_introduction.html",
        "https://docs.juce.com/master/tutorial_plugin_examples.html",
    ]
    
    # Same download logic as Python docs
    for i, url in enumerate(juce_urls):
        try:
            print(f"📥 [{i+1}/{len(juce_urls)}] Downloading: {url}")
            
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
            response = requests.get(url, timeout=15, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for element in soup(["nav", "header", "footer", "aside", "script", "style"]):
                element.decompose()
            
            content = soup.find('div', class_='contents') or soup.find('main') or soup.find('body')
            
            if content:
                filename = f"juce_{url.split('/')[-1].replace('.html', '')}.txt"
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
    download_juce_documentation()
