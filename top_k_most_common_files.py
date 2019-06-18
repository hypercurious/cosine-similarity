import numpy as np

documents_name = []
discrete_words = []
documents_dictionary = {}
common_words = {}
counter_list = []

def cosine_similarity(document1, document2):
  norm_doc1 = np.linalg.norm(document1)
  norm_doc2 = np.linalg.norm(document2)
  dot_product = np.dot(document1, document2)
  vector_length_product = norm_doc1 * norm_doc2
  cos = dot_product / vector_length_product
  return cos

x = 0
while x!=1:
  try:
    number_of_documents = int(input("Enter the number of documents: "))      
    if number_of_documents < 2:
      number_of_documents = 2
    x = 1
  except ValueError:
    print("Invalid option, please type an integer!")

for i in range(number_of_documents):
  x = 0
  while x!=1:
    try:
      temp = input("Enter the name (including file type) of document #" + str(i+1) + ": ")
      current_document = open(temp, "r")
      documents_name.append(temp)
      document_content = current_document.read().lower().split()
      for word in document_content:
        if word not in discrete_words:
          discrete_words.append(word)
      documents_dictionary.update({documents_name[i]: document_content})
      current_document.close()
      x = 1
    except FileNotFoundError:
      print("Invalid option, file not found, try again!")

for document in documents_dictionary:
  for word in discrete_words:
    counter_list.append(documents_dictionary[document].count(word))
  common_words.update({document: counter_list})
  counter_list = []

cosine_result_dictionary = {}
for doc1 in range(len(documents_dictionary)):
  for doc2 in range(doc1+1, len(documents_dictionary)):
    cosine_result = cosine_similarity(common_words.get(documents_name[doc1]), common_words.get(documents_name[doc2]))
    temp = ". <" + str(documents_name[doc1])+ "> <" + str(documents_name[doc2]) + "> : "
    cosine_result_dictionary[temp] = cosine_result

max_k = len(cosine_result_dictionary)
k = int(input("Enter the number(k) of most similar documents, you want to view: "))
if k < 1:
  k = 1
if k > max_k:
  k = max_k
for i in range(k):
  key = sorted(cosine_result_dictionary, key=cosine_result_dictionary.get, reverse=True)
  value = cosine_result_dictionary.get(key[i])
  print(str(i+1)+key[i]+str(value))