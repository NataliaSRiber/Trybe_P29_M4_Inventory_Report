from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith('.csv'):
            with open(path) as file:
                csv_file = list(csv.DictReader(file))
            return csv_file
        else:
            raise ValueError("Arquivo inválido")
