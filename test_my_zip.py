import pytest
from main import my_zip

def test_zip_equal_length_lists():
    # Тест на одинаковой длине списков
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    result = my_zip(list1, list2)
    assert result == [(1, 'a'), (2, 'b'), (3, 'c')]

def test_zip_first_list_longer():
    # Тест, когда первый список длиннее второго
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b']
    result = my_zip(list1, list2)

    assert result == [(1, 'a'), (2, 'b')]

def test_zip_second_list_longer():
    # Тест, когда второй список длиннее первого
    list1 = [1, 2]
    list2 = ['a', 'b', 'c']
    result = my_zip(list1, list2)

    assert result == [(1, 'a'), (2, 'b')]

def test_zip_empty_list():
    # Тест на пустых списках
    list1 = []
    list2 = []
    result = my_zip(list1, list2)

    assert result == []

def test_zip_one_empty_list():
    # Тест, когда один из списков пуст
    list1 = [1, 2, 3]
    list2 = []
    result = my_zip(list1, list2)

    assert result == []
    
    
if __name__ == "__main__":
    pytest.main()