class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if 0 <= index <= len(self._data) - 1:
            return self._data[index]
        else:
            raise IndexError()

    def clear(self):
        if self.is_empty():
            print('Não há elementos')
            return None
        self._data.clear()
        print('')

    def get_all(self):
        return list(self._data)
