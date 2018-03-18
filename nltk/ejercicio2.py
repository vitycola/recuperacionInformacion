import nltk
import string

# Abrimos el archivo.
with open('./Textos/Data_Science.txt', 'r', encoding="utf8") as f:
    sample = f.read()
f.close()

#sentences = nltk.tokenize.sent_tokenize(sample)



# for sentence in sentences:
no_punctuation = []
tokens = nltk.word_tokenize(sample.lower())
for token in tokens:
    punct_removed = ''.join([letter for letter in token if not letter in string.punctuation])
         # Si no es un símbolo de puntuación lo añadimos al resultado.
    if punct_removed != '':
        no_punctuation.append(punct_removed)

   # print(no_punctuation)


frecuencia_all = nltk.FreqDist(tokens)
print(frecuencia_all.most_common(10))

frecuencia_np = nltk.FreqDist(no_punctuation)
frecuencia_np.most_common(10)

print("El número de recurrencias de la palabra 'data' es ", frecuencia_np['data'])




