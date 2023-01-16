# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input('Enter text: ')
text_list = []
for i in text:
    text_list.append(i)
    
packed_list, unpacked_list = list(), list()
for index, element in enumerate(text_list[:-1]):
    counter = 0
    ind = 0
    while text_list[ind] == text_list[ind+1]:
        # counter = text_list.count(element)
        counter+=1
        ind+=1
        packed_list.append(str(counter)+text_list[ind])
        # unpacked_list.append(counter*element)
packed_text = ''.join(packed_list)
# unpacked_text = ''.join(unpacked_list)
print(packed_text)

# unpacked_text = ''

# for i, el in enumerate(packed_list):
#     for i in el:
#         num = int(i)
#         new_el = el.replace(str(num), '')
#         unpacked_text += str(num*new_el)
# print(unpacked_text)


packed_list, unpacked_list = list(), list()
counter = 0
index = 0
ind=0
while text_list[index] == text_list[ind+1]:
    # counter = text_list.count(element)
    counter+=1
    ind+=1
    packed_list.append(str(counter)+text_list[index])
    # unpacked_list.append(counter*element)
packed_text = ''.join(packed_list)
# unpacked_text = ''.join(unpacked_list)
print(packed_text)