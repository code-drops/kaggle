# 0
'''what len() would return when passed that string.'''
a = ""
length = 0

b = "it's ok"
length = 7

c = 'it\'s ok'
length = 7

d = """hey"""
length = 3

e = '\n'
length = 1

# 1
''' a valid zip code is any string consisting of exactly 5 digits.'''
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code)!=5:
        return False
    for i in zip_code:
        if i not in [str(i) for i in range(10)]:
            return False
    return True

# 2

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    doc_list = [
        doc.replace(".","").replace(",","").lower().split(' ')
        for doc in doc_list
    ]
    keyword = keyword.lower()
    l = []
    for doc in doc_list:
        if keyword in doc:
            l.append(doc_list.index(doc))
    return l

# 3
""" Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
def word_search(doc_list, keyword):
    doc_list = [
        doc.replace(".","").replace(",","").lower().split(' ')
        for doc in doc_list
    ]
    keyword = keyword.lower()
    l = []
    for doc in doc_list:
        if keyword in doc:
            l.append(doc_list.index(doc))
    return l
def multi_word_search(doc_list, keywords):

    dic = {}
    for key in keywords:
        l = word_search(doc_list,key)
        dic[key] = l
    return dic