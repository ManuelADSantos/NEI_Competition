N = int(input())

if N < 1 or N > 1e4:
    exit()

# print("Valid")
library = []

for i in range(0, N):
    square = input()
    square = square.split(" ")
    # print(square)

    if int(max(square)) > 1e6 or int(min(square)) < 0:
        exit()

    if len(square) != 4:
        exit()

    coord = [[int(square[0]), int(square[1])],[int(square[2]), int(square[3])]]
    library.append(coord)

# print(library)

dim = max(max(max(library)))

grid = [[0 for col in range(dim)] for row in range(dim)]
# print(grid)

for sq in library:
    # print("sq:"+str(sq))
    for i in range(dim):
        for j in range(dim):
            if i >= sq[0][0] and i < sq[1][0] and j >= sq[0][1] and j < sq[1][1]:
                grid[i][j] += 1


# print(grid)

cnt = 0
for i in range(dim):
    for j in range(dim):
        if grid[i][j] == N:
            cnt += 1

print(cnt)