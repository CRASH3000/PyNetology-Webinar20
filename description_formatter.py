class DescriptionFormatter:
    @staticmethod
    def format_description(customer_data):

        gender = 'мужского' if customer_data['sex'] == 'male' else 'женского'
        device = 'компьютера' if customer_data['device_type'] == 'desktop' else 'мобильного устройства'
        return (f"Пользователь {customer_data['name']} {gender} пола, "
                f"{customer_data['age']} лет совершил(а) покупку на {customer_data['bill']} у.е. с "
                f"{device} браузера {customer_data['browser']}. "
                f"Регион, из которого совершалась покупка: {customer_data['region']}.")
