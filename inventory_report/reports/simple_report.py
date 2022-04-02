from datetime import datetime, date
from collections import Counter


text1 = "Data de fabricação mais antiga:"
text2 = "Data de validade mais próxima:"
text3 = "Empresa com maior quantidade de produtos estocados:"


class SimpleReport():
    def convert_date(date):
        return datetime.strptime(date, "%Y-%m-%d").date()

    @classmethod
    def generate(cls, data):
        oldest_date = cls.convert_date("2022-03-02")
        nearest_date = cls.convert_date("2024-03-02")
        companies_name_list = []
        for product in data:
            converted_date = cls.convert_date(product["data_de_fabricacao"])
            if converted_date < oldest_date:
                oldest_date = converted_date
            converted_validation_date = cls.convert_date(
                product["data_de_validade"])
            if date.today() < converted_validation_date < nearest_date:
                nearest_date = converted_validation_date
            companies_name_list.append(product["nome_da_empresa"])
            count_names = dict(Counter(companies_name_list))
            first_company = max(count_names, key=count_names.get)
        return (
            f'{text1} {oldest_date}\n'
            f'{text2} {nearest_date}\n'
            f'{text3} {first_company}\n'
        )
