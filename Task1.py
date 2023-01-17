# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Добавлено сохранение пунктуации


import string
string.punctuation

def main():
    text = 'вапроеалдад абв роло АБВ, абвапро апргшл'

    for i in string.punctuation:
        if i in text:
            text = text.replace(i, f' {i}')
    text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
    text = ' '.join(text)
    
    for i in string.punctuation:
        if i in text:
            text = text.replace(f' {i}', i)
    print(text)

if __name__ == "__main__":
    main()