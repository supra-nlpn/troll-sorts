import sys
import os

# Add src directory to path for testing without installation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from troll_sorts import communist_sort, capitalist_sort, island_sort, six_seven_sort

def test_communist_sort():
    my_list = [10, 25, 4, 30, 15, 8]
    result = communist_sort(my_list)
    print(f"Communist: {result}")
    assert result == [15, 15, 15, 15, 15, 15]

def test_capitalist_sort():
    my_list = [10, 25, 4, 30, 15, 8]
    result = capitalist_sort(my_list)
    print(f"Capitalist: {result}")
    assert result == [0, 0, 0, 0, 0, 92]

def test_island_sort():
    my_list = [10, 25, 4, 30, 15, 8]
    result = island_sort(my_list)
    print(f"Island: {result}")
    assert result == [4, 8, 10, 15]

def test_six_seven_sort():
    my_list = [10, 25, 4, 30, 15, 8]
    result = six_seven_sort(my_list)
    print(f"Six-Seven: {result}")
    assert result == [6, 7, 6, 7, 6, 7]

if __name__ == "__main__":
    try:
        test_communist_sort()
        test_capitalist_sort()
        test_island_sort()
        test_six_seven_sort()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\nTest failed!")
        sys.exit(1)
