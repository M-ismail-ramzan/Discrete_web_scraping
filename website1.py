from header import *

first_website = ["http://nu.edu.pk/","http://isb.nu.edu.pk/","http://khi.nu.edu.pk/","http://lhr.nu.edu.pk/","http://pwr.nu.edu.pk/"]
# Calling the function to go and get the web data
############
first_website_text = [] # Contains the content of the website 
first_website_nouns = [] # Contains the number of nouns in website
first_website_verbs = []  # Contains the verbs of the website
first_website_adj = []  # Contains the adjective of the website
################# Go and show the Graph with Subdomains ################
show_subdomain_graph(first_website_text,first_website_nouns,first_website_verbs,first_website_adj,first_website)
################ Go and count the total number of Parts of speech in doamin ########
first_website_total = []
# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection
first_website_total.append(count_total(first_website_nouns))
first_website_total.append(count_total(first_website_verbs))
first_website_total.append(count_total(first_website_adj))
################ Show the Final Graph of the Website ###############3
print_graph(first_website_total[1],first_website_total[2],first_website_total[0],"Total For this Domain")

