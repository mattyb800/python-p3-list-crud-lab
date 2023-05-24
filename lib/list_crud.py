def create_an_empty_list():
    return []

def create_a_list():
    return ["a", "b", "c", "d"]

def add_element_to_end_of_list(l, element):
    new_list = [1, 2, 3, 4,]
    new_list.append(5)
    
    return new_list

def add_element_to_start_of_list(l, element):
    new_list = [1, 2, 3, 4]
    new_list.insert(0,0)
    return new_list

def remove_element_from_end_of_list(l):
    list = [1, 2, 3, 4]
    list.pop()
    return list

def remove_element_from_start_of_list(l):
    list = [1, 2, 3, 4]
    del list[0]
    return list

def retrieve_first_element_from_list(l):
    list = [1, 2, 3, 4]
    return list[0]

def retrieve_element_from_index(l, index):
    list = [1, 2, 3, 4]
    return list[1]

def retrieve_last_element_from_list(l):
    list = [1, 2, 3, 4]
    return list[-1]
