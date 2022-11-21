import csv
import datetime as dt

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'pep_parse/results'
FIELDS_NAME = ('Статус', 'Количество')
TIME_NOW = dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
FILE_DIR = RESULTS_DIR / 'status_summary_{time}.csv'.format(time=TIME_NOW)


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}

    def process_item(self, item, spider):
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] += 1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)
        with open(FILE_DIR, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow((FIELDS_NAME))
            for key, val in self.results.items():
                writer.writerow([key, val])
            writer.writerow(['Total', sum(self.results.values())])
