### Finding Links to PDF's in a Webpage:
This program does the following:

* Takes the URI of a webpage as a command-line argument
* Extracts all the links from the page
* For each link, request the URI and use the Content-Type HTTP response header to determine if the link references a PDF file
* For all links that reference a PDF file, print the original URI (found in the source of the original HTML), the final URI (after any redirects), and the number of bytes in the PDF file. (Hint: Content-Length HTTP response header)

### To run:
`python3 pdf_counter.py <URL>`
```python
# Michelle Scheuer
# 9/9/2021

import sys
from bs4 import BeautifulSoup
import requests

url = sys.argv[1]
response = requests.get(url, allow_redirects=True)
data = response.text
soup = BeautifulSoup(data, features="html.parser")

for link in soup.find_all('a'):
    all_links = link.get('href')
    my_list = [all_links]

    for i in my_list:
        if i.startswith("http"):
            res = requests.get(i)
            if res.headers['Content-Type'] == 'application/pdf':
                print("URI:", i, "\n",
                      "Final URL:", i, "\n",
                      "Content length:", "{:,}".format(eval(res.headers['Content-Length'])), "bytes \n")


```
### Result Snippet:
Results of `python3 pdf_counter.py https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html`:

![\label{fig:firstURI}](url1.jpg)
