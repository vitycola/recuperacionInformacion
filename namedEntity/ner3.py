import nltk
import os
from nltk.tag.stanford import StanfordNERTagger
java_path = ""
os.environ['JAVAHOME'] = java_path
# Abrimos para lectura el fichero que queremoc tratar.
with open('../data/Ciencia_de_datos.txt', 'r', encoding="utf8") as f:
    sample = f.read()
f.close()

# Obtenemos las sentencias del texto.
sentences = nltk.sent_tokenize(sample)
print("Frases: ")
print(sentences)

# Obtenemos los tokens de cada sentencia. Es decir cada palabra que forman las mismas.
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
print("Tokens de cada frase: ")
print(tokenized_sentences)