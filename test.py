a_list = ["i","love","u","so","much"]

for index, elem in enumerate(a_list):
    if (index+1 < len(a_list) and index - 1 >= 0) and len(elem) > 3:
        if len(a_list[index+1]) > 3:
            prev_el = str(a_list[index-1])
            curr_el = str(elem)
            next_el = str(a_list[index+1])

            print( curr_el, next_el)