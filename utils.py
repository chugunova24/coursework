

def read_file(file, delimiter, num_columns):
    with open(file=file, mode='r') as f:
        arr = f.read()
        new_arr = []
        start = 0
        end = None

        for idx in range(len(arr)):
            if arr[idx] == '\n' or arr[idx] == delimiter:
                end = idx
                new_arr.append(arr[start:end])
                start = idx + 1

        return [new_arr[i:i + num_columns] for i in range(0, len(new_arr), num_columns)][1:]


def fastSort(matrix, column_number):
    def reqFastSort(arr, l, r):
        lptr, rptr = l, r  # определяем указатели слева/справа
        refIdx = (lptr + rptr) // 2  # (выбираем опору в середине)
        ref = int(arr[refIdx][column_number])  # получаем значение опоры
        # пока первый эелемент меньше/равен второму
        # передвигаем так, чтобы этот элемент встал на своё место.
        # Все элементы меньше него перемещаются влево, а равные и большие
        # элементы перемещаются вправо.
        while lptr <= rptr:
            # меньше него перемещаются влево
            while int(arr[lptr][column_number]) < ref:
                lptr += 1
            # а равные и большие элементы перемещаются вправо.
            while int(arr[rptr][column_number]) > ref:
                rptr -= 1
            if (lptr <= rptr):
                arr[lptr], arr[rptr] = arr[rptr], arr[lptr]
                lptr += 1
                rptr -= 1

        if l < rptr:
            reqFastSort(arr, l, rptr)
        if r > lptr:
            reqFastSort(arr, lptr, r)

    hashes = matrix[0]
    arr = matrix[1]
    reqFastSort(arr, 0, len(arr) - 1)
    return arr




