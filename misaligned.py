def print_color_map():
    list_color_pairs_console_print = list()
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            list_color_pairs_console_print.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors), list_color_pairs_console_print

def test_ColorMap_numerical_values(list_color_pairs_console_print):
    #Lets Calculate the length of numerical seperation for all elements in list
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    list_received_color_pairs_numerical_values  = [int(color_pair_print.split('|')[0].strip()) for color_pair_print in list_color_pairs_console_print]
    
    list_actual_color_pairs_numerical_values = [(i * 5 + j)+1 for i in range(len(major_colors)) for j in range(len(minor_colors))]
    return list_received_color_pairs_numerical_values, list_actual_color_pairs_numerical_values

def test_ColorMap_seperator_allignment(list_color_pairs_console_print):
    #Lets Calculate the length of numerical seperation for all elements in list
    list_color_pairs_seperation_values  = [len(color_pair_print.split('|')[0]) for color_pair_print in list_color_pairs_console_print]

    #We will return the length of the set(unique values) of the list.
    return len(set(list_color_pairs_seperation_values))
    
result, list_color_pairs_console_print = print_color_map()
assert(result == 25)

list_received_color_pairs_numerical_values, list_actual_color_pairs_numerical_values = test_ColorMap_numerical_values(list_color_pairs_console_print)
number_of_different_seperations = test_ColorMap_seperator_allignment(list_color_pairs_console_print)

assert(list_received_color_pairs_numerical_values == list_actual_color_pairs_numerical_values)

#We will assert if the return value is 1 which means all the seperation values are same. Then they are of same length
assert(number_of_different_seperations == 1) 

print("All is well (maybe!)\n")
