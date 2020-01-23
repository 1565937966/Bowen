import re

frequency = dict()
file_name = "C://Users//15659//Desktop//regular expression.txt"
with open(file_name, 'w') as file:
    file.write("Hello world\nHello Python\nHello C#")

text = open(file_name, 'r').read().lower()

target = "hello"
# pattern = re.search(r"[a-z]", text)
total_words = re.split("\s", text)


for index in range(0, len(total_words)):
    '''
    pattern = r"{0}".format()
    result = re.findall(pattern, text)
    print(result)
    '''
    counter = frequency.setdefault(total_words[index], 0)
    frequency[total_words[index]] += 1
print(frequency)

'''
for word in pattern:
    counter = frequency.setdefault(word, 0)
    frequency[word] += 1


frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])
# print(frequency_list)
# Mutiplye operator
'''
string = "Hello, I love Python, Hello, World"
result = re.split(',|\s', string)
print(result)
for index in range(0, len(result)):
    if result[index] is "":
        result[index].remove()
print(result)
'''
for word in result:
    if word is not " ":
        print(word)
'''