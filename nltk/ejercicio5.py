import re
import nltk.corpus

# Abrimos el archivo.
with open('./Textos/Data_Science.txt', 'r', encoding="utf8") as f:
    sample = f.read()
f.close()


#    no_punctuation = []
tokens = nltk.word_tokenize(sample.lower())
pattern = 'd[a-z]*'
for p in tokens:
    if re.search(pattern, str(p)):
        print(re.search(pattern, str(p)).group(0))

print(tokens)

