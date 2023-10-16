def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode = 'w', encoding='utf-8') as file_opened:
        file_opened.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode = 'a', encoding='utf-8') as file_opened:
        file_opened.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', encoding='utf-8') as file_opened:
        return file_opened.read()
