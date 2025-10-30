
# %pip install scholarly

from scholarly import scholarly

def search_google_scholar(query, num_results=5):
    search_query = scholarly.search_pubs(query)
    results = []
    
    # Retrieve papers based on the query
    for i in range(num_results):
        paper = next(search_query, None)
        
        if paper:
            bib = paper.get("bib", {})
            results.append({
                "title": bib.get("title"),
                "abstract": bib.get("abstract"),
                "url": paper.get("eprint_url"),
                "year": bib.get("pub_year")
            })
        else:
            print(f"No paper found for result index {i+1}.")
    
    return results

# Comprehensive query for TTP-related papers in ML security
query = (
    "((\"Tactics, Techniques, and Procedures\" OR \"TTP\" OR \"adversarial attack\" OR \"threat\" OR \"vulnerability\") "
    "AND (\"machine learning security\" OR \"ML security\" OR \"AI security\" OR \"deep learning security\") "
    "AND (\"data poisoning\" OR \"evasion attack\" OR \"model tampering\" OR \"model inversion\" OR "
    "\"backdoor attack\" OR \"adversarial example\" OR \"denial of service\" OR \"resource exhaustion\"))"
)

# Search Google Scholar and retrieve papers
scholar_results = search_google_scholar(query, num_results=5)

# Print results to verify
for result in scholar_results:
    print(f"Title: {result['title']}")
    print(f"Abstract: {result['abstract']}")
    print(f"URL: {result['url']}")
    print(f"Year: {result['year']}\n")






### Semantic Scholar API
import requests

def search_semantic_scholar(query, num_results=5):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace with your actual API key
    params = {
        "query": query,
        "limit": num_results,
        "fields": "title,abstract,year,url"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print("Error:", response.status_code)
        return []

query = "Tactics, Techniques, and Procedures in Machine Learning security"
results = search_semantic_scholar(query, num_results=10)
for paper in results:
    print(f"Title: {paper['title']}")
    print(f"Abstract: {paper['abstract']}")
    print(f"URL: {paper['url']}")
    print(f"Year: {paper['year']}\n")


