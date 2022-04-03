from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def inventory_type(data, type):
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_data(cls, path, type):
        if path.endswith('.csv'):
            data = CsvImporter.import_data(path)
        elif path.endswith('.json'):
            data = JsonImporter.import_data(path)
        elif path.endswith('.xml'):
            data = XmlImporter.import_data(path)
        return cls.inventory_type(data, type)
