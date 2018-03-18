import nltk
import string

# Abrimos el archivo.
with open('./Textos/Data_Science.txt', 'r', encoding="utf8") as f:
    sample = f.read()
f.close()

# FORMA DE PROCESAMIENTO ELEGANTE.

# Obtenemos las sentencias del texto.
sentences = nltk.tokenize.sent_tokenize(sample)

# Para cada sentencia obtenemos sus tokens y comprobamos que no estén dentro de los símbolos de puntuación.
for sentence in sentences:
    no_punctuation = []
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        punct_removed = ''.join([letter for letter in token if not letter in string.punctuation])
        # Si no es un símbolo de puntuación lo añadimos al resultado.
        if punct_removed != '':
            no_punctuation.append(punct_removed)
    # Para cada sentencia mostramos los tokens antes y después del filtrado.
    print("Antes: ")
    print(tokens)
    print("Después: ")
    print(no_punctuation)

# SI NECESITAMOS SOLO EL TEXTO SIN LOS SÍMBOLOS DE PUNTUACIÓN.

text_cleared = ""
# Para carácter en el texto comprobamos si es un símbolo de puntuación.
for letter in sample:
    if not letter in string.punctuation:
        text_cleared = text_cleared + letter
# Mostramos el texto antes y después del filtrado.
print("Texto antes: ")
print(sample)
print("Texto después: ")
print(text_cleared)