from csv import reader
from unicodedata import lookup


def load_csv(file_name):
    file = open(file_name, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

filename  = 'diabetes.csv'

ds = load_csv(filename)

print('Loaded data file{0}, with {1} rows, and {2} columns.'.format(filename, len(ds), len(ds[0])))

print(ds[0])
print(ds[1])

#data is loaded as strings we need to convert it to
#floating point number.
def str_column_to_float(dataset,column, has_header_row=True):
    """
    converts a dataset string columns to float data type
    :param dataset:
    :param column: the column to be converted
    :param has_header_row: if the first row contains the columns' names
    :return:
    """
    index = 0
    if has_header_row:
         index = 1
    for row in dataset[index:]:
        row[column] = float(row[column].strip())

for i in range(len(ds[0])):
    str_column_to_float(ds,i,has_header_row=True)

print(ds[1])

def str_column_to_int(dataset,column,has_header_row=True):
    """
    Converts a
    :param dataset:
    :param column:
    :param has_header_row:
    :return:
    """
    index = 0
    if has_header_row:
        index = 1
    class_values = [row[column] for row in dataset[index:]]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset[index:]:
        row[column] = lookup[row[column]]
    return lookup

filename = "iris.csv"

ds = load_csv(filename)

print('Loaded data file{0}, with {1} rows, and {2} columns.'.format(filename, len(ds), len(ds[0])))

print(ds[0])
for i in range(4):
    str_column_to_float(ds,i,False)
lookup = str_column_to_int(ds,4,False)
print(ds[1])