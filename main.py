from Core.utils.csv_creator import CSVCreator


def create_csv_files(n):
    print(f'Create {n} csv files')
    CSVCreator(n).create_csv_concurrent()


if __name__ == '__main__':
    create_csv_files(10000)

