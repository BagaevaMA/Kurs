from pprint import pprint

list_of_lists_1= [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_list = list_of_lists

    def __iter__(self):
        self.cursor_outer = 0
        self.cursor_inner = -1
        return self

    def __next__(self):
        self.cursor_inner += 1
        if self.cursor_inner >= len(self.list_of_list[self.cursor_outer]):
            self.cursor_outer += 1
            self.cursor_inner = 0
        if self.cursor_outer >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.cursor_outer][self.cursor_inner]

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
pprint(list(FlatIterator(list_of_lists_1)))