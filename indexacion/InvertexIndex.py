from indexacion.ProcessText import TextProcessor

class BuildIndex:
	# Se crea el índice conteniendo el procesador de texto, los ficheros a procesar y el contenido ya procesado.
	def __init__(self, files):
		self.filenames = files
		self.processor = TextProcessor()
		self.terms_per_file = self.process_files()

        # Se procesa el contenido de los ficheros y se almacenan las palabras procesadas para cada texto.
    def process_files(self):
        file_to_terms = {}
        for file in self.filenames:
            text = open(file, encoding='utf8',mode='r').read()
            words = self.processor.process_text(text)
            for word in words:
                file_to_terms[str(word)].append(file)
        return file_to_terms

class BasicQuery:
	# Se crea la consulta conteniendo el índice y el procesador de texto.
	def __init__(self, index):
		self.index = index
		self.basicIndex = self.index.terms_per_file
		self.processor = TextProcessor()

	# Se consulta por una palabra en el índice.
	def one_word_query_basic_index(self, word):
		result = []
		for filename in self.basicIndex.keys():
			if word in self.basicIndex[filename]:
				result.append(filename)
		return result

	# Se consulta un texto completo en el índice.
	def free_text_query_basic_index(self, text):
		result = {}
		tokens = self.processor.process_text(text)
		for token in tokens:
			# Para cada token se busca en cuales textos aparece.
			result[token] = self.one_word_query_basic_index(token)
		return result

if __name__  == "__main__":
    filenames = ['./corpus/pg135.txt', './corpus/pg76.txt', './corpus/pg5200.txt']
    index = BuildIndex(filenames)
    q = BasicQuery(index)
    print(q.free_text_query_basic_index('house'))
    print(q.free_text_query_basic_index("The house was in England"))