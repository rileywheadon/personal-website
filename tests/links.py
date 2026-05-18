import requests
from html.parser import HTMLParser
from urllib.parse import urljoin

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs_dict = dict(attrs)

            if "href" in attrs_dict:
                href = attrs_dict["href"]
                full_url = urljoin(self.base_url, href)
                self.links.append(full_url)

# Queue has the structure (origin, url)
seen = []
queue = [("", "http://localhost:5000")]

def enqueue_links(seen, queue, parser):
    for link in parser.links:
        if link not in seen:
            seen.append(link)
            queue.append((parser.base_url, link))

    return seen, queue

def check_link(seen, queue):
    base, link = queue.pop(0)

    if link.startswith("mailto:"):
        return seen, queue

    response = requests.get(link)
    code = response.status_code

    # Status code 403 is okay as this indicates we encountered bot protection
    # Status code 999 is returned specifically by LinkedIn to discourage bots
    if code in [403, 999]:
        print(f"Warning: link {link} from {base} returned {code}")
    elif code >= 400:
        raise ValueError(f"Error: link {link} from {base} returned {code}")

    # Enqueue any internal links
    if link.startswith("http://localhost"):
        parser = LinkParser(response.url)
        parser.feed(response.text)
        seen, queue = enqueue_links(seen, queue, parser)

    return seen, queue

while len(queue) > 0:
    seen, queue = check_link(seen, queue)
