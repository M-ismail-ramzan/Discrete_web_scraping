import urllib.request as ur
import time
import numpy as np
from textblob import TextBlob
from bs4 import BeautifulSoup
from matplotlib import pyplot

# A simple Function that takes no. of pos and print the graph for it
def print_graph(count_verbs, count_adj , count_nouns, title):
    pof = ('Verb', 'Ajective', 'Nouns')
 
    rank = [count_verbs , count_adj , count_nouns]
    explode = (0.2, 0, 0)  
    colors = ['yellowgreen', 'pink', 'orange']
    pyplot.title(title)
 
    pyplot.pie(rank, explode=explode, labels=pof, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=120)
    pyplot.axis('equal')
    pyplot.show()
#Pass this function the blob from the final text and get the count of nouns
def return_noun_count(blob):
    nouns = [n for n, t in blob.tags if (t == 'NN' or t == 'NNS' or t == 'NNP' or t == 'NNPS')]
    print(nouns)
    count_nouns = 0
    for noun in nouns:
        count_nouns=count_nouns+1
    print("Total Number of Nouns: " + str(count_nouns))
    return int(count_nouns)
#Pass this function the blob from the final text and get the count of verbs
def return_verb_count(blob):
    verbs = [n for n, t in blob.tags if (
    t == 'VB' or t == 'VBD' or t == 'VBG' or t == 'VBN' or t == 'VBP' or t == 'VBN' or t == 'VBZ')]
    print(verbs)
    count_verbs = 0
    for verb in verbs:
        count_verbs=count_verbs+1
    print("Total Number of Verbs: " + str(count_verbs))
    return int(count_verbs)
#Pass this function the blob from the final text and get the count of adjectives
def return_adj_count(blob):
    adjectives = [n for n, t in blob.tags if (
    t == 'JJ' or t == 'JJR' or t == 'JJS')]
    print(adjectives)
    count_adj = 0
    for adjective in adjectives:
        count_adj=count_adj+1
    print("Total Number of Adjectives: " + str(count_adj))
    return int(count_adj)

# This is the function that takes a URL and return the Final Text from the website 

def return_web_text(ori_url):

    # Open the url and save it
    url = ur.urlopen(ori_url).read()
    soup = BeautifulSoup(url, features="html.parser")

    # Remove all the scripts and style tags
    for script in soup(["script"]):
        script.extract()  # Remove them

    for style in soup(["style"]):
        style.extract()  # Remove them

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
    return final_text


#####################################################
## *************** Main Function Calling ********* ##
######################################################
first_website = ["http://nu.edu.pk/","http://isb.nu.edu.pk/","http://khi.nu.edu.pk/","http://lhr.nu.edu.pk/","http://pwr.nu.edu.pk/"]

# Calling the function to go and get the web data
first_website_text = []
first_website_nouns = []
first_website_verbs = []
first_website_adj = []
def show_subdomain_graph(first_website_text,first_website_nouns,first_website_verbs,first_website_adj):
    counting = 0
    for final in first_website:
        # Here we have access to all the website names
        # Call the function to get the text
        first_website_text.append(return_web_text(final))
        #Adding the text to TextBlob library so we can use blob and identify pos
        blob = TextBlob(str(first_website_text[counting]))
        first_website_nouns.append(return_noun_count(blob))
        first_website_verbs.append(return_verb_count(blob))
        first_website_adj.append(return_adj_count(blob))
        print_graph(first_website_verbs[counting],first_website_adj[counting],first_website_nouns[counting],first_website[counting])
        counting = counting + 1
    """
final_text = []
final_text[0] = return_web_text(ori_url[0])
final_text[1] = return_web_text(ori_url[1])
final_text[2] = return_web_text(ori_url[2])
final_text[3] = return_web_text(ori_url[3])
final_text[4] = return_web_text(ori_url[4]
#Adding the text to TextBlob library so we can use blob and identify pos
blob = TextBlob(str(final_text[0]))
blob = TextBlob(str(final_text[1]))
blob = TextBlob(str(final_text[2]))
blob = TextBlob(str(final_text[3]))
blob = TextBlob(str(final_text[4]))
# print(blob.tags)
# Now finding the Noun
(count_nouns) = return_noun_count(blob)
# Finding the verb 
count_verbs = return_verb_count(blob)
# Finding the Adjective 
count_adj = return_adj_count(blob)
# Now let's Print the Graph
print_graph(count_verbs,count_adj,count_nouns,ori_url)

"""
#References
#https://www.geeksforgeeks.org/python-program-to-check-if-a-word-is-a-noun/
#https://matplotlib.org/
