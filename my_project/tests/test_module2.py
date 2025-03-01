from my_project.module2 import multiply_and_add

def test_multiply_and_add():
    assert multiply_and_add(2, 3, 4) == 10
    assert multiply_and_add(-1, 2, 5) == 3