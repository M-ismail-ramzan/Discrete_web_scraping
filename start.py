#import website1
#import website2
#import website3
from website1 import *
from website2 import *
from website3 import *
#Now i need access to the data of the website...
#print (first_website_total[0])
from matplotlib import pyplot
import numpy as np


# first_website_total,second_website_total & third_website_total
# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection

# THIS Function takes 3 values and show the Graph with label for comparison
print("THE MAXIMUM OCCURANCES OF THE FIRST WEBSITE")
print(first_website_max_nouns_list)
print(first_website_max_adjective_list)
print(first_website_max_verbs_list)

print("THE MAXIMUM OCCURANCES OF THE second WEBSITE")
print(second_website_max_nouns_list)
print(second_website_max_adjective_list)
print(second_website_max_verbs_list)

print("THE MAXIMUM OCCURANCES OF THE third WEBSITE")
print(third_website_max_nouns_list)
print(third_website_max_adjective_list)
print(third_website_max_verbs_list)
"""
def comparison_graph_display(first_pof,second_pof,third_pof,labels):
    X = ["FAST","NUST","LUMS"]
    nouns = [first_pof,second_pof,third_pof]
    X_axis = np.arange(len(X))
    pyplot.bar(X_axis + 0.0, nouns, 0.4, label = labels)
    pyplot.xticks(X_axis, X)
    pyplot.xlabel(labels)
    pyplot.ylabel("Counting")
    pyplot.title("Comparison of Three Websites " + labels)
    pyplot.legend()
    pyplot.show()

# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection
comparison_graph_display(first_website_total[0],second_website_total[0],third_website_total[0],"Nouns")
comparison_graph_display(first_website_total[1],second_website_total[1],third_website_total[1],"Verbs")
comparison_graph_display(first_website_total[2],second_website_total[2],third_website_total[2],"Adjective")
"""