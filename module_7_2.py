def custom_write(file_name, strings):
    fp = open(file_name, mode='w', encoding='utf-8', newline='\n')
    dict_ = {}

    for elem_ in strings:
        dict_.update({(strings.index(elem_)+1, fp.tell()): str(elem_)})
        fp.write(str(elem_) + ' \n')
    fp.close()
    return dict_

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
