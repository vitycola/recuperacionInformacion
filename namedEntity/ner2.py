import nltk

# Abrimos para lectura el fichero que queremoc tratar.
with open('../data/Data_Science.txt', 'r', encoding="utf8") as f:
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


# Obtenemos las etiquetas de cada uno de los tokens (nombres, adjetivos, verbos, ...)
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
#named_ent = [nltk.ne_chunk(tagged_sentences) for sentence in tokenized_sentences]
print("Etiquetas de cada frase: ")
print(tagged_sentences)


# Obtenemos las etiquetas de cada uno de los tokens (nombres, adjetivos, verbos, ...)
named_ent = [nltk.ne_chunk(nltk.pos_tag(sentence)) for sentence in tokenized_sentences]
#named_ent = [nltk.ne_chunk(tagged_sentences) for sentence in tokenized_sentences]
#print("Etiquetas de cada frase: ")
#print(tagged_sentences)
print("Etiquetas ext")
print(named_ent)

# Lo mismo pero obteniendo etiquetas universales.
universal_tagged_sentences = [nltk.pos_tag(sentence, tagset='universal') for sentence in tokenized_sentences]
print("Etiquetas universales de cada frase: ")
print(universal_tagged_sentences)

# Las frases chunked devuelven la estructura de cada frase en forma de árboles.
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

# Función recursiva que recorre el arbol.
def extract_entity_names(t):
    entity_names = []
    # Se comprueba que el token tenga etiqueta.
    if hasattr(t, 'label') and t.label:
        # Si es un entity name entonces lo agregamos con los que ya hemos identificado.
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        # En caso contrario obtenemos todos los hijos del token para continuar con la búsqueda.
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

# Inicializamos el resultado.
entity_names = []

# Recorremos cada árbol correspondiente a cada frase.
for tree in chunked_sentences:
    print (tree)
    entity_names.extend(extract_entity_names(tree))

# Mostramos todos los entity names.
print("All entities...")
print(entity_names)

# Mostramos los entity names únicos.
print("Unique entities...")
print (set(entity_names))
