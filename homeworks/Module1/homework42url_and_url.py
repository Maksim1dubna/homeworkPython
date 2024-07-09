import re
import requests

def extract_image_links(html_text):
    # Match the img tag
    img_tags = re.findall(r'<img[^>]*>', html)
    urls = []
    # Extract src attributes
    for img_tag in img_tags:
        url = re.search(r'src\s*=\s*["\']([^"\']+)["\']', img_tag)
        if url:
            urls.append(url.group(1))


    return urls

# Example usage
html = requests.get("https://giphy.com/gifs/kendricklamar-kendrick-lamar-not-like-us-EccELUNNAkmpCb03y9")
html = html.text
image_urls = extract_image_links(html)
for url in image_urls:
    print(url)
