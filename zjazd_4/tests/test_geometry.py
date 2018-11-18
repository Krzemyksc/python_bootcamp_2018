from mathematica.geometry.figures import square_area, triangle_area


def test_square_area():
    assert square_area(4) == 16
    assert square_area(0) == 0
    assert square_area(-10) == None


def test_triangle_area():
    assert triangle_area(1, 2) == 1
    assert triangle_area(10, 20) == 100
