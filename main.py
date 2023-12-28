from data_reader import DataReader
from data_parser import DataParser
from description_formatter import DescriptionFormatter
from file_writer import FileWriter


def main():
    reader = DataReader('web_clients_correct.csv')
    headers, data = reader.read_csv()

    parser = DataParser()  # Создание экземпляра класса DataParser для преобразования данных из CSV
    # Парсинг данных с использованием заголовков для создания списка словарей
    parsed_data = parser.parse_data(headers, data)

    # Генерация описаний для каждого клиента в списке
    descriptions = [DescriptionFormatter.format_description(customer) for customer in parsed_data]

    writer = FileWriter('descriptions.txt')
    writer.write_to_txt(descriptions)
    print("Файл 'descriptions.txt' успешно создан.")


if __name__ == "__main__":
    main()
