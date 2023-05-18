import random


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __get__(self):
        return self.key, self.value


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # емкость
        self.size = 0  # размер массива
        self.table = [None] * (self.capacity + int(self.capacity / 2))  # задаем размер таблицы
        self.factor = 2  # scale factor
        self.ckei = 1

    def resize(self):
        self.capacity *= self.factor
        new_table = [None] * (self.capacity + int(self.capacity / 2))

        for node in self.table:
            if node is not None:
                self.insert(key=node.key, value=node.value, table=new_table)

        self.table = new_table

        return

    def _hash(self, key, length, i):
        return hash(tuple(key)) % length + i

    def checkCollisions(self, index, table=None):
        if table is None:
            table = self.table

        try:
            current = table[index]
        except IndexError:
            print('увел колво ячеек')

        return current is not None  # если не пусто то коллизия есть

    def insert(self, key, value, table=None):
        if table is None:
            table = self.table

        i = 0

        while True:
            index = self._hash(key=key, length=self.capacity, i=i)

            if not self.checkCollisions(index=index, table=table):
                table[index] = Node(key, value)
                self.size += 1
                # print(f'Добавлено {index} // {key}')
                # print(f'Размер текщий {self.ckei}')
                self.ckei += 1

                return
            else:
                current = self.table[index]

                while current:
                    if current.key == key:
                        current.value = value
                        # print(f'обновлено {index} // {key}')
                        return
                    current = current.next
                    # print(index)

                new_node = Node(key, value)
                new_node.next = self.table[index]
                self.table[index] = new_node
                # print(f'добавлено в цепочку {index} // {key}')
                self.size += 1
                self.ckei += 1
                return

            # i += 1

        # i = 0
        #
        # # if self.size == self.capacity:
        # #     self.resize()
        #
        # while True:
        #     index = self._hash(key=key, length=self.capacity, i=i)
        #
        #     if not self.checkCollisions(index=index, table=table):
        #         table[index] = Node(key, value)
        #         self.size += 1
        #         # print(f'index: {index}')
        #         # # print(f'Добавлено {self.ckei}')
        #         # print(f'Добавлено {key}')
        #         # self.ckei += 1
        #
        #         return
        #     i += 1

        # print(self.table[index].key)

        # if checkCollisions(key=key, index=index):
        #     self.table[index] = Node(key, value)  # insert("apple", 3)
        #     self.size += 1
        # else:
        #     current = self.table[index]
        #     while current:
        #         if current.key == key:
        #             current.value = value
        #             return
        #         current = current.next
        #     new_node = Node(key, value)
        #     new_node.next = self.table[index]
        #     self.table[index] = new_node
        #     self.size += 1

    def search(self, key):
        index = self._hash(key=key, length=self.capacity, i=0)

        if self.checkCollisions(index=index):
            current = self.table[index]

            while current:
                if current.key == key:
                    return current.value
                current = current.next

        raise KeyError(key)

        # index = self._hash(key=key, length=self.capacity, i=0)
        # i = 0
        #
        # print(f'  : {self.checkCollisions(index=index)}    // {index}')
        #
        # # if self.checkCollisions(index=index):
        # if self.checkCollisions(index=index):
        #     while index <= (self.capacity + int(self.capacity / 2)):
        #
        #         index = self._hash(key=key, length=self.capacity, i=i)
        #         # if self.table[index] is not None:
        #         current = self.table[index]
        #
        #         if current.key == key:
        #             return [current.key, current.value]
        #
        #         else:
        #             i += 1

        # raise KeyError(key)

    def remove(self, key):

        index = self._hash(key=key, length=self.capacity, i=0)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __get__(self):
        # return self.table
        # ck = 0
        for i in self.table:
            if i is not None:
                # print([i.key, i.value])
                print([i.key, i.value])
                # ck += 1
                if i.next is not None:
                    print([i.next.key, i.next.value])
                    # ck += 1
        # print(f'ck: {ck}')

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
