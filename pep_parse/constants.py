import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

RESULTS_DIR = BASE_DIR / 'results'
RESULTS_DIR.mkdir(exist_ok=True)
FIELDS_NAME = ('Статус', 'Количество')
TIME_NOW = dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
FILE_DIR = RESULTS_DIR / 'status_summary_{time}.csv'.format(
    time=TIME_NOW)