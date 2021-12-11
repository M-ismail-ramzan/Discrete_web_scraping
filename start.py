import requests
from bs4 import BeautifulSoup

# 1. The HTTP request
url = "http://nu.edu.pk/"
webpage = requests.get(url, 'html.parser')

# 2. Turn the website into a soup object
soup = BeautifulSoup(webpage.content,features="html.parser")

# 2 get all the data from url
#1.3 find_all() with attributes
data_list = soup.find_all("div")
# Once u got the data from the fast webpage now print them for me
for data in data_list:
    if data != "None":
        print(data.string)
    
