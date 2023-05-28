
def relation_between_files(list_of_sub_files):

    relationships = {}

    for name in list_of_sub_files:
        common_part = name[0:3]  # Extract the common part of the name
        
        if common_part not in relationships:
            relationships[common_part] = []
        
        relationships[common_part].append(name)
    return relationships


def find_closest(key, list_of_keys):

    closest_number = None
    minimum_difference = float('inf')

    for num in list_of_keys:
        difference = abs(key - num)
        if difference < minimum_difference:
            minimum_difference = difference
            closest_number = num
    print("Closest Number:", closest_number)
    return closest_number

def relation_between_texts(eng, pt):
    final_relation = []
    eng_key_list = []
    for key in eng.keys():
        eng_key_list.append(int(key[:-1]))
    
    for pt_key, pt_text in pt.items():
        pt_key = int(pt_key[:-1])
        eng_key = find_closest(pt_key, eng_key_list)
        final_relation.append((pt_text, eng[str(eng_key) + "t"]))
    print(final_relation)
    return final_relation
