import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        response.encoding = "utf-8"
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def extract_hyperlinks(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    hyperlinks = set()
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        name = link.get_text(strip=True)  # Get the text within the <a> tag
        if href.startswith('http') or href.startswith('https'):
            hyperlinks.add((name, href))
    return hyperlinks

def write_hyperlinks_to_file(hyperlinks, filename):
    with open(filename, 'w') as file:
        for name, link in sorted(hyperlinks, key=lambda x: x[1]):
            file.write(f"{name}: {link}\n")

def main(url, output_file):
    html_content = fetch_html(url)
    if html_content:
        hyperlinks = extract_hyperlinks(html_content)
        write_hyperlinks_to_file(hyperlinks, output_file)
        print(f"Extracted {len(hyperlinks)} hyperlinks and saved to {output_file}")
    else:
        print("Failed to retrieve or parse the HTML content.")

if __name__ == "__main__":
    url_to_crawl = "http://sanguo.5000yan.com/"  # Replace with the target URL
    output_filename = "hyperlinks.txt"
    main(url_to_crawl, output_filename)
