""" Say that you're a traveler on a d 2D grid. You begin in 
the top-left corner and your goal is to travel to the bottom-right
corner. You may only move  down or right.


In how many ways can you travel to the goal on a grid with 
dimension m * n?
"""


# recursion
def gridTravelerRecursion(m, n):
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0
    
    # down is row - 1, right is column - 1
    return gridTravelerRecursion(m - 1, n) + gridTravelerRecursion(m, n -1)


def gridTravelerMemoization(m,n, table = {}):
    key = m, n

    if key in table:
        return table[key]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    table[key] = gridTravelerMemoization(m - 1, n, table) + gridTravelerMemoization(m, n - 1, table)
    return table[key]
    


if __name__ == '__main__':
    print(gridTravelerMemoization(1,1)) # 1
    print(gridTravelerMemoization(2,3)) # 3
    print(gridTravelerMemoization(3,2)) # 3
    print(gridTravelerMemoization(3,3)) # 6
    print(gridTravelerMemoization(18,18)) # 2333606220