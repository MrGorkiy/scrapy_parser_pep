import csv

from pep_parse.constants import FILE_DIR, FIELDS_NAME


class PepParsePipeline:
    def open_spider(self, spider):
        """Создание словаря для подсчета."""
        self.results = {}

    def process_item(self, item, spider):
        """Подсчет количества статусов."""
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] += 1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        with open(FILE_DIR, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow((FIELDS_NAME))
            for key, val in self.results.items():
                writer.writerow([key, val])
            writer.writerow(['Total', sum(self.results.values())])
