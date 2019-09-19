import random


def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width)
              + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i * n:(i + 1) * n] for i in range(n)]


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    B = []
    for i in range(len(A)):
        B.append(A[i][pos[1]])
    return B


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    if pos[0] < 4:
        return (A[(pos[1] - 1) // 3])
    elif pos[0] < 7:
        return (A[3 + ((pos[1] - 1) // 3)])
    elif pos[0] < 10:
        return (A[6 + ((pos[1] - 1) // 3)])


def solve(grid):
    position = find_empty_positions(grid)
    if position == (-1, -1):
        return grid

    values = find_possible_values(grid, position)
    n = len(values)
    for i in range(n):
        elem = random.choice(values)
        grid[position[0]][position[1]] = elem
        solution = solve(grid)
        if solution is not None:
            return solution
    grid[position[0]][position[1]] = '.'
    return None


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'],['4', '5', '6'],['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'],['4', '.', '6'],['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'],['4', '5', '6'],['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if A[i][j] == '.':
                return i, j


def find_possible_values(grid, pos):
    """ Вернуть множество всех возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzles/puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    row = set(get_row(grid, pos))
    col = set(get_col(grid, pos))
    block = set(get_block(grid, pos))
    return list(digits - row - col - block)


def check_solution(solution):
    """ Если решение solution верно, то вернуть True,
    в противном случае False """
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    k = 0
    for i in range(9):
        for j in range(9):
            row = set(get_row(solution, [i][j]))
            col = set(get_col(solution, [i][j]))
            block = set(get_block(solution, [i][j]))
            if row == col & col == block & block == digits:
                k += 1
    if k == 81:
        return True
    else:
        return False


def generate_sudoku(N):
    grid = [['.' for i in range(9)] for i in range(9)]
    grid = solve(grid)

    places = [(i, j) for i in range(9) for j in range(9)]
    for q in range(81 - N):
        place = random.choice(places)
        places.remove(place)
        grid[place[0]][place[1]] = '.'
    return grid

if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)

