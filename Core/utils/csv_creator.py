import csv
import threading
import multiprocessing
from datetime import datetime

from settings import BASE_DIR


class CSVCreator:
    def __init__(self, number_of_files):
        self.number_of_files = number_of_files

    def _create_csv(self, number):
        with open(f'{BASE_DIR}\csv_storage\storage_{number}.csv', 'w') as new_csv:
            writer = csv.writer(new_csv)

            for x in range(1, 10000):
                writer.writerow([f'row_{x}', f'name_{x}'])

    def create_csv_concurrent(self):
        processes = []
        start_time = datetime.now()
        print(f'Before concurrent run {start_time}')
        for n in range(1, self.number_of_files):
            process = multiprocessing.Process(target=self._create_csv, args=(n,))
            processes.append(process)
            process.start()

        for p in processes:
            p.join()

        end_time = datetime.now()
        print(f'After concurrent loop {end_time}')
        print(f'Concurrent run took {end_time - start_time}')

    def create_csv_sequential(self):
        start_time = datetime.now()
        print(f'Before sequential loop {start_time}')
        for n in range(1, self.number_of_files):
            self._create_csv(n)

        end_time = datetime.now()
        print(f'After sequential loop {end_time}')
        print(f'Concurrent run took {end_time - start_time}')
