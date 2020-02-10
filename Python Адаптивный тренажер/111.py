def find(x, y, el, el1):
    count = 0
    for k in range(el, x):
        for g in range(el1, y):
            if field[k][g] == '*':
                count += 1
    return count


n, m = map(int, input().split())
field = [list(input()) for i in range(n)]


for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            continue
        else:
            if i == 0 and j == 0:
                field[i][j] = find(2, 2, i, j)
            elif i == 0 and j != 0 and j != m:
                field[i][j] = find(2, 3, i, j - 1)
            elif i != 0 and j == 0 and i != n:
                field[i][j] = find(3, 2, i - 1, j)
            elif i == n and j == 0:
                field[i][j] = find(2, 2, i - 1, j)
            else:
                field[i][j] = find(3, 3, i - 1, j - 1)


for element in field:
    for j in element:
        print(j, end='')
    print()