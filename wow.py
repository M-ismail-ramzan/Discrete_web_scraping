
from textblob.blob import TextBlob
import networkx as nx
import matplotlib.pyplot as plt
import nxviz as nv

text = [b" Campus in 2009. Currently, He is working as a Senior IT Auditor, KPMG Dublin, Ireland. Previously he worked for Deloitte Islamabad as an Assistant Manager IT Audit. Admissions for FALL 2020 are open! To apply please follow the link: http://pwr.nu.edu.pk/admissions/ Last date to apply: 30th July 2020 Muhammad Batch 10 (BSCS) Hi, I am Farwa Zaki. CS graduate of Batch 12. Currently, I am working as a Data Analyst in Telenor Pakistan. My message for @FASTians is, The best"]

first_website_top_10_nouns = [['courses', 111], ['research', 74], ['student', 59], ['PhD', 57], ['program', 56], ['students', 46], ['degree', 39], ['knowledge', 39], ['credit', 35], ['management', 32]]

other_list = [['courses', 111], ['research', 74], ['student', 59], ['PhD', 57], ['program', 56], ['students', 46], ['degree', 39], ['knowledge', 39], ['credit', 35], ['management', 32], ['research', 13], ['ORIC', 12], ['Campus', 11], ['List', 10], ['FAST', 10], ['Date', 10], ['Home', 9], ['Faculty', 9], ['PhD', 9], ['Islamabad', 9], ['Karachi', 10], ['students', 9], ['Campus', 8], ['University', 6], ['Computer', 6], ['FAST', 6], ['event', 6], ['National', 5], ['Sciences', 5], ['skills', 5], ['Engineering', 13], ['FAST', 10], ['Lahore', 9], ['Department', 9], ['School', 7], ['Campus', 6], ['Electrical', 6], ['Civil', 6], ['Science', 6], ['campus', 6], ['Peshawar', 25], ['Campus', 22], ['FAST', 19], ['Computer', 15], ['University', 14], 
['Batch', 13], ['Science', 11], ['Engineering', 11], ['details', 11], ['Pakistan', 11]]

other_list_=[]
for each in other_list:
    other_list_.append(each[0])
    print((each[0]))
#print(other_list_)

# Now i have the top 10 Nouns of the website let's create it's graph
G = nx.Graph()



text=str(text)
text=TextBlob(text)
#Looping for Each Sentence!
test_list = []
for sentence in text.sentences:
    #Check all the Nouns in the Sentence
    nouns = [n for n, t in text.tags if (
        t == 'NN' or t == 'NNS' or t == 'NNP' or t == 'NNPS')]
    #Check for each of the noun
    for index, elem in enumerate(nouns):
        #Getting all the Nouns next & Previous so we can add them
        if (index+1 < len(nouns) and index - 1 >= 0) and (len(elem) > 4):
            #prev_el = str(nouns[index-1])
            if len(nouns[index+1]) > 4 and nouns[index+1] in other_list_:
                curr_el = str(elem)
                next_el = str(nouns[index+1])
                #Making the nodes of th e
                G.add_node(curr_el)
                G.add_node(next_el)
                #Now adding those Nodes together
                G.add_edge(curr_el,next_el)
               


    #print(sentence)


pos=nx.spring_layout(G, k=0.99 ,iterations=20,scale=2)
nx.draw(G,pos,with_labels=True,node_color='skyblue',font_size = 4)
print(nx.number_connected_components(G))
sorted(G.degree, key=lambda x: x[1], reverse=True)
d = list(G.degree)
print(d)

tup = [('research', 42), ('students', 36), ('program', 34), ('management', 27), ('courses', 24), ('skills', 23), ('knowledge', 22), ('Campus', 21), ('Peshawar', 18), ('degree', 18), ('student', 17), ('Karachi', 16), ('Lahore', 14), ('University', 14), ('Faculty', 13), ('Pakistan', 12), ('Computer', 12), ('Engineering', 12), ('Science', 11), ('Islamabad', 10), ('National', 9), ('campus', 9), ('Electrical', 9), ('Department', 8), ('Batch', 7), ('Civil', 6), ('Sciences', 6), ('Management', 6), ('credit', 5), ('event', 5), ('Vision', 4), ('Student', 3), ('education', 3), ('careers', 3), ('fundamentals', 3), ('School', 3), ('course', 3), ('staff', 3), ('graduate', 3), ('needs', 2), ('university', 2), ('Students', 2), ('level', 2), ('development', 2), ('business', 2), ('Finance', 2)]

count=0
for each in tup:
    if count == 10:
        break
    else:
        print(each)
        count=count+1
plt.show()

