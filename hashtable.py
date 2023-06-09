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

                return
            else:
                current = self.table[index]

                while current:
                    if current.key == key:
                        current.value = value

                        return
                    current = current.next

                new_node = Node(key, value)
                new_node.next = self.table[index]
                self.table[index] = new_node
                self.size += 1

                return

    def search(self, key):
        index = self._hash(key=key, length=self.capacity, i=0)

        if self.checkCollisions(index=index):
            current = self.table[index]

            while current:
                if current.key == key:
                    return current.value
                current = current.next

        raise KeyError(key)

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
        res = []

        for i in self.table:
            if i is not None:
                res.append([i.key] + i.value)
                if i.next is not None:
                    res.append([i.next.key] + i.next.value)

        return res

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
