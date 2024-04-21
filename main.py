stopwords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if',
             'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that',
             'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with']

rnd_par = open("random_paragraphs.txt","r").read()
filtered_sentence = [w for w in rnd_par if not w in ["(",")",",",".","\""]]
rnd_par = "".join(filtered_sentence).split()
filtered_sentence = [w for w in rnd_par if not w.lower() in stopwords]

new_filtered_sentence = set(filtered_sentence)
res = {key: 0 for key in new_filtered_sentence}

for i in filtered_sentence:
    res[i] +=1

print(res)
