
import nltk.corpus

# Abrimos el archivo.
with open('./Textos/Ciencia_de_datos.txt', 'r', encoding="utf8") as f:
    sample = f.read()
f.close()

sentences = nltk.tokenize.sent_tokenize(sample)


pal_vacias = nltk.corpus.stopwords.words('spanish')


for sentence in sentences:
#    no_punctuation = []
    tokens = nltk.word_tokenize(sentence.lower())
    words = [w for w in tokens if w not in pal_vacias]
    print(words)
