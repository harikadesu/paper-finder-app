import requests
import xml.etree.ElementTree as ET

def search_arxiv(query, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    query_url = f"search_query=all:{query}&start=0&max_results={max_results}"

    response = requests.get(base_url + query_url)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    papers = []
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
        link = None
        for link_elem in entry.findall('atom:link', ns):
            if link_elem.attrib.get('type') == 'application/pdf':
                link = link_elem.attrib.get('href')
                break
        if not link:
            # fallback to entry id if no PDF link found
            link = entry.find('atom:id', ns).text.strip()
        papers.append({'title': title, 'summary': summary, 'link': link})

    return papers
