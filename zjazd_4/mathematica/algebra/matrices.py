# def add_matrices():
#     X = [[12, 7, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
#
#     Y = [[5, 8, 1],
#          [6, 7, 3],
#          [4, 5, 9]]
#
#     result = [[0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0]]
#
#     licznik_r = []
#
#     for i in range(len(X)):
#         for j in range(len(X[0])):
#             result[i][j] = X[i][j] + Y[i][j]
#
#     for r in result:
#         licznik_r.append(r)
#         print("r", r)
#         print("Licznik r", licznik_r)

def add_matrices(X,Y):
    result = []
    for row_i in range(len(X)):
        new_row = []
        for col_i in range(len(X[row_i])):
            new_row.append((X[row_i][col_i] + Y[row_i][col_i]))
        result.append(new_row)
    return result

def sub_matrices(X, Y):
    result = []
    for row_i in range(len(X)):
        new_row = []
        for col_i in range(len(X[row_i])):
            new_row.append((X[row_i][col_i] - Y[row_i][col_i]))
        result.append(new_row)
    return result

# a = add_matrices()
# print(a)
