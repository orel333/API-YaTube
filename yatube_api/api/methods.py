def to_str(dict):
    str = ''
    for key, value in dict.items():
        print('Извлечение строки')
        str += f"{key}:{value}\n"
    return str


def to_dict(str):
    new_dict = {}
    for i in str.split('\n'):
        try:
            new_dict[i.split(':')[0]] = i.split(':')[1]
        except:
            pass
    return new_dict