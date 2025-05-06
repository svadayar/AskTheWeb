import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    for tag in soup(["script", "style"]):
        tag.decompose()
    
    return ' '.join(soup.stripped_strings)
