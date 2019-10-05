#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
    #start writing your code here
    sentence_list=[]
    sentence=""
    for el in subjects:
        for el_2 in verbs:
            for el_3 in objects:
                sentence+=el+" "+el_2+" "+el_3
                sentence_list.append(sentence)
                sentence=""

    
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))