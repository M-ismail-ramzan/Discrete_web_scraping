
from textblob.blob import TextBlob
import networkx as nx
import matplotlib.pyplot as plt
import nxviz as nv

text = [b"FAST National University " ]
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
# Adding nodes to the graph
for each in first_website_top_10_nouns:
    G.add_node(each[0])
#Now finding the adjacent element in each Node!


G.add_edge('PHD', 'program')

#plt.show()

text = str(text)
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

plt.show()
