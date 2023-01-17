# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(string):
    compressed_string = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        compressed_string += str(count) + string[i]
        i += 1
    return compressed_string

def decompression(string):
    decompressed_string = ''
    i = 0
    while i < len(string)-1:
        count = int(string[i])
        decompressed_string += count*string[i+1]
        i += 2
    return decompressed_string

def main():
    text = input('Enter a text: ')
    print()
    print('Compressed text: ', compression(text))
    print('Recovered text: ', decompression(compression(text)))
 
if __name__ == '__main__':
    main()

