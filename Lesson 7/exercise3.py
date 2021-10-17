from math import ceil


class Chunk:
    cells_count: int

    def __init__(self, cells_count: int):
        if cells_count <= 0:
            raise ValueError('Число клеток должно быть больше нуля')
        self.cells_count = cells_count

    def __add__(self, other):  # +
        return Chunk(self.cells_count + other.cells_count)

    def __sub__(self, other):  # -
        return Chunk(self.cells_count - other.cells_count)

    def __mul__(self, other):  # *
        return Chunk(self.cells_count * other.cells_count)

    def __truediv__(self, other):  # /
        return Chunk(self.cells_count // other.cells_count)

    def __get_cells_in_row(self, row_index, row_len):
        count = self.cells_count
        return min(row_len, count - row_index * row_len)

    def make_order(self, row_len):
        return '\n'.join(['*' * self.__get_cells_in_row(i, row_len) for i in range(ceil(self.cells_count/row_len))])

    def get_printable_order(self, row_len):
        return f'Ячеек: {self.cells_count}, Длина строки: {row_len}\n{self.make_order(row_len)}'


my_chunk1 = Chunk(9)
my_chunk2 = Chunk(10)
my_chunk3 = Chunk(4)

my_chunk_add = my_chunk1 + my_chunk1
my_chunk_sub = my_chunk2 - my_chunk3
my_chunk_mul = my_chunk1 * my_chunk3
my_chunk_div = my_chunk2 / my_chunk3

print(my_chunk1.make_order(4), end='\n\n')

print(my_chunk_add.get_printable_order(4), end='\n\n')
print(my_chunk_sub.get_printable_order(5), end='\n\n')
print(my_chunk_mul.get_printable_order(6), end='\n\n')
print(my_chunk_div.get_printable_order(100500), end='\n\n')
