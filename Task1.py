# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'вапроеалдад абв роло АБВ, абвапро'

text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))