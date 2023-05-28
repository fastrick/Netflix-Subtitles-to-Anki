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