import numpy as np

document_content = ""
discrete_words = []
documents_name = []
documents_dictionary = {}
common_words = {}
words_counter = 0
number_of_documents = 0

def cosine_similarity(document1, document2):
  norm_doc1 = np.linalg.norm(document1)
  norm_doc2 = np.linalg.norm(document2)
  dot_product = np.dot(document1, document2)
  vector_length_product = norm_doc1 * norm_doc2
  cos = dot_product / vector_length_product
  return cos

number_of_documents = int(input("Enter the number of documents: "))
for i in range(number_of_documents):
  documents_name.append(input("Enter the name (including file type) of document #" + str(i+1) + ": "))
  current_document = open(documents_name[i], "r")
  document_content = current_document.read().lower().split()
  for word in document_content:
    if word not in discrete_words:
      discrete_words.append(word)
  documents_dictionary.update({documents_name[i]: document_content})
  current_document.close()

