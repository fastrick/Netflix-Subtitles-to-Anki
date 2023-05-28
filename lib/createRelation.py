

def relation(eng, pt):
    final_relation = []
    
    for eng_key, eng_text in eng.items():
        for pt_key, pt_text in pt.items():
            if eng_key == pt_key:
                final_relation.append((eng_text, pt_text))

    print(final_relation)
    return final_relation
