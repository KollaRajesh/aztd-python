← [02. Pydantic](./02-pydantic.md) | [Modules](./README.md) | **03. BeautifulSoup4** | [04. python-dotenv →](./04-dotenv.md)

---

# BeautifulSoup4: Web Scraping

**Purpose:** Parse and extract data from HTML/XML.

## Simple: Parse HTML

```python
from bs4 import BeautifulSoup
import requests

html = "<html><body><p class='title'>Hello</p><p>World</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

# Find single element
title = soup.find("p", class_="title")
print(title.text)  # "Hello"

# Find all
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)
```

## Medium: Web Scraping

```python
response = requests.get("https://example.com")
soup = BeautifulSoup(response.content, "html.parser")

# Extract data
titles = [h.text for h in soup.find_all("h2")]
links = [a["href"] for a in soup.find_all("a")]

# CSS selectors
items = soup.select("div.item > p.name")
for item in items:
    print(item.text)
```

## Complex: Scrape with Navigation & Error Handling

```python
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def scrape_page(url, max_depth=2):
    visited = set()
    
    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract data
            data = {"url": url, "title": soup.title.string if soup.title else None}
            
            # Follow links
            for link in soup.find_all("a", href=True):
                next_url = urljoin(url, link["href"])
                if next_url.startswith("https://example.com"):
                    crawl(next_url, depth + 1)
            
            return data
        except Exception as e:
            print(f"Error: {e}")
    
    return crawl(url, 0)
```

**Install:** `pip install beautifulsoup4` | **Use:** Web scraping, data extraction, HTML parsing

---

← [02. Pydantic](./02-pydantic.md) | [Modules](./README.md) | **03. BeautifulSoup4** | [04. python-dotenv →](./04-dotenv.md)
