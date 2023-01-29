class MyHashMap:
    def __init__(self):
        pass

    def put(self, key: int, value: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def remove(self, key: int) -> None:
        pass

    def __get_index(self, key, value) -> int:
        pass


def main():
    obj = MyHashMap()
    key, value = 1, 1
    obj.put(key, value)
    param_2 = obj.get(key)
    obj.remove(key)


if __name__ == '__main__':
    main()
