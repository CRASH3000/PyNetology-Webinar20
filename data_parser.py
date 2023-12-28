class DataParser:
    @staticmethod
    def parse_data(headers, data):
        parsed_data = []

        # Проходим по каждой строке в исходных данных.
        for row in data:
            parsed_row = {headers[i]: row[i] for i in range(len(row))}
            # Создаем словарь, сопоставляя каждый заголовок с соответствующим значением в строке.
            parsed_data.append(parsed_row)
            # Добавляем словарь в список преобразованных данных.

        return parsed_data
