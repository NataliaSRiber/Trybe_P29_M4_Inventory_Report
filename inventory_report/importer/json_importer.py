from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith('.json'):
            with open(path) as file:
                json_file = json.load(file)
            return json_file
        else:
            raise ValueError("Arquivo inválido")
