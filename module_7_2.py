def custom_write(file_name, strings):
    str_pos = {}
    f = open(file_name, 'w', encoding = 'utf-8')
    try:
        for i, j in enumerate(strings, start = 1):
            byte_pos = f.tell()
            f.write(j + '\n' )
            str_pos[(i, byte_pos)] = j
    finally:
        f.close()
    return str_pos

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
