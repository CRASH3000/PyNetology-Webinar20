import csv


class DataReader:
    # Конструктор класса, инициализирующий объект с путем к файлу CSV.
    def __init__(self, file_path):
        self.file_path = file_path # Сохранение пути к файлу в переменную экземпляра класса.

    def read_csv(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader]
        return headers, data
