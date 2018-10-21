# lista = [1, 2, 3, 4, 5, 6]
#
#
# def przytnij(lista, x):
#     start = lambda x: x > 3
#     stop = lambda x: x == 6
#     out = []
#     if start and stop:
#         x.append(out)
#
# print(przytnij(lista,3))
#
# def wieksze_niz_3(x):
#     out = []
#     if x > 3:
#         out.append(x)
# def równe_6(x):
#     out = []
#     if x <=6:
#         out.append(x)


def przytnij(data, start, stop):
    result = set()
    for element in data:
        if element >= start and element <= stop:
            result.append(element)
    return result.add(element)
