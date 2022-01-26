import requests
from bs4 import BeautifulSoup

prefix = "https://en.wikipedia.org"

def isValid(ref,paragraph):
    if not ref or "#" in ref or "//" in ref or ":" in ref:
        return False
    if "/wiki/" not in ref:
        return False
    if ref not in paragraph:
        return False
    prefix = paragraph.split(ref,1)[0]
    if prefix.count("(")!=prefix.count(")"):
        return False
    return True

def validateTag(tag):
    return tag.name == "p" or tag.name == "ul"

def getFirstLink(wikipage):
    page = requests.get(prefix+wikipage)
    soup = BeautifulSoup(page.text, "html.parser")
    soup = soup.find(class_="mw-parser-output")
    for paragraph in soup.find_all(validateTag, recursive=False):
        for link in paragraph.find_all("a"):
            ref = link.get("href")
            if isValid(str(ref),str(paragraph)):
                return ref
    return False

wikipage = "/wiki/Python_(programming_language)"
target = "/wiki/Philosophy"
counter = 0

while wikipage != target:
    old = wikipage
    wikipage = getFirstLink(wikipage)
    counter += 1
    print("{}: {} -> {}".format(counter, old, wikipage))
