class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_txt(self, descriptions):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for desc in descriptions:  # Перебор всех описаний в предоставленном списке
                file.write(desc + '\n')
                # Запись каждого описания в файл, добавляя символ новой строки после каждого описания
