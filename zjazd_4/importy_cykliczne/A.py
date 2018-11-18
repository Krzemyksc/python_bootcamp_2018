from B import bar # nie zadziałą bo mam import cykliczny w sensie w B chcę importować A a w A chcę zaimportować coś z B
print("Jestem w module A")


def foo():
    return "foo z modułu A"


print(foo())
print(bar())
