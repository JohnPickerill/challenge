from triangle import get_triangle, cost

def test_Cost():  
    tri = get_triangle('triangle_fixture.txt')
    assert cost(tri) == 202