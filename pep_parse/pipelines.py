import csv
import datetime as dt
from pathlib import Path

# При попытке вынести все константы в отдельный файл, заваливаются тесты,
# но функциональность полностью сохраняется
BASE_DIR = Path(__file__).parent.parent

FIELDS_NAME = ('Статус', 'Количество')
DIR_OUTPUT = 'results'
DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'
TIME_NOW = dt.datetime.now().strftime(DT_FORMAT)


class PepParsePipeline:
    def open_spider(self, spider):
        """Формирование пути до директории results."""
        self.results = {}
        self.result_dir = BASE_DIR / DIR_OUTPUT
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        """Подсчет количества статусов."""
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] += 1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        """Запись данных в файл."""

        file_dir = self.result_dir / FILE_NAME.format(
            time=TIME_NOW)
        with open(file_dir, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow((FIELDS_NAME))
            for key, val in self.results.items():
                writer.writerow([key, val])
            writer.writerow(['Total', sum(self.results.values())])
