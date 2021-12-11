import urllib.request as ur
import time
from textblob import TextBlob
from bs4 import BeautifulSoup

ori_url = "http://nu.edu.pk/"
#Open the url and save it
url = ur.urlopen(ori_url).read()
soup = BeautifulSoup(url,features="html.parser")

# Remove all the scripts and style tags
for script in soup(["script"]):
    script.extract() #Remove them 

for style in soup(["style"]):
    style.extract() #Remove them    

# get strings
strings = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = []
for line in strings.splitlines():
    lines.append(line.strip())

# break multi-headlines into a line each

pieces = []
for line in lines:
    for phrase in line.split("  "):
        pieces.append(phrase.strip()) 

# Remove the empty lines
text = ' ' . join(chunk for chunk in pieces if chunk)
print(text.encode('utf-8'))
final_text = text.encode('utf-8')


# Now finding the Noun phases
blob = TextBlob(str(final_text))
print(blob.noun_phrases)