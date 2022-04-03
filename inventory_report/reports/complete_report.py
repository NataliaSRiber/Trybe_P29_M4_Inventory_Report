from inventory_report.reports.simple_report import SimpleReport


text1 = "Produtos estocados por empresa: "


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        companies_string = ""
        simple_report = SimpleReport.generate(data)
        names_list = []
        for product in data:
            names_list.append(product["nome_da_empresa"])
        count_names = SimpleReport.count_names_dict(names_list)
        # retorna um dicionario
        tupla_count_names = list(count_names.items())
        # transforma em tupla
        for name in tupla_count_names:
            companies_string += f'- {name[0]}: {name[1]}\n'
        return (
            f'{simple_report}\n'
            f'{text1}\n'
            f'{companies_string}'
        )
