from utils import read_file, fastSort
from hashtable import HashTable

FILENAME = 'table.csv'
DELIMITER = ','
NUM_COLUMNS = 7

arr = read_file(FILENAME, DELIMITER, NUM_COLUMNS)
# print(read_file(FILENAME, DELIMITER, NUM_COLUMNS))


hashes = HashTable(capacity=len(arr))
i=0
for elem in arr[1:]:
    hashes.insert(key=elem[0], value=elem[1:])
    i +=1
print(i)
print()


# print(hashes.__get__())

arr = hashes.__get__()
# print(arr)


# общая выручка
def summary_revenue(arr):
    total = 0

    for idx in range(len(arr)):
        print(idx)
        total += int(arr[idx][-1])

    return total


# получить самый продаваемый по колву продукт
# где:
#   arr -> массив
#   column_number -> id колонки из массива с критерием
def get_best_product(arr, column_number):
    sortedMatrix = fastSort(arr, column_number=column_number)
    result = []

    for idx in range(len(sortedMatrix) - 1, 0, -1):
        if sortedMatrix[idx][column_number] == sortedMatrix[-1][column_number]:
            result.append(sortedMatrix[idx])
        else:
            return result

    return result


# вычислить долю
# где:
#   x -> сумма, процент которой надо вычислить
#   n -> общая выручка
def calc_percentage(x, n):
    return x * 100 / n



# общ выручка, колво продан единиц и доля от общ выручки
def accounting(arr):
    total_sum = summary_revenue(arr)
    report = []
    for idx in range(len(arr)):
        report.append([
                    arr[idx][2],
                    arr[idx][4],
                    round(calc_percentage(x=int(arr[idx][6]), n=total_sum), 2),
        ])
    return [total_sum, report]


print()
print(accounting(arr))
print(f'len: {arr.__len__()}')

# add excep handl