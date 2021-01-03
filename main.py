# This is a sample Python script.
from Core.settings import BASE_DIR
from Core.utils.csv_creator import CSVCreator


def create_csv_files(n):
    print(f'Create {n} csv files')
    CSVCreator(n).create_csv_concurrent()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_csv_files(10000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
