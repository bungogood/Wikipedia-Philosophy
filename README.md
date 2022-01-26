# Its all Philosophy
This is a wikipedia webcrawler which selects the first link in a given wikipedia page. It continues to select the first link until it reaches philosophy or a loop.

## Installation
```bash
git clone git@github.com:Bungogood/Wikipedia-Philosophy.git
cd Wikipedia-Philosophy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running
```bash
python crawl.py [wikipage]
```