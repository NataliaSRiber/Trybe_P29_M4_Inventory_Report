from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith('.xml'):
            data = []
            xml_file = ET.parse(path).getroot()
            for product in xml_file:
                product_dict = {}
                for attribute in product:
                    product_dict[attribute.tag] = attribute.text
                data.append(product_dict)
            return data
        else:
            raise ValueError("Arquivo inválido")
