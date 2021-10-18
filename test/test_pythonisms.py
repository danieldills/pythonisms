import pytest

from pythonisms import LinkedList

# @pytest.mark.skip("pending")
def test_for_in():
    colors = LinkedList(('red', 'green', 'orange'))
    colors_list = []
    for color in colors:
        colors_list.append(color)
    assert colors_list == ['red', 'green', 'orange']

# @pytest.mark.skip("pending")
def test_sum_values():
    ll_values = LinkedList((5,10,15))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 30

# @pytest.mark.skip("pending")
def test_list_comprehension():
    colors = LinkedList(('yellow', 'green', 'blue'))
    cap_colors = [color.upper() for color in colors]
    assert cap_colors == ['YELLOW', 'GREEN', 'BLUE']

# @pytest.mark.skip("pending")
def test_list_cast():
    colors = ['blue', 'indigo', 'violet']
    color = LinkedList(colors)
    assert list(color) == colors

# @pytest.mark.skip("pending")
def test_range():
    num_range = range(1,15+3)
    nums = LinkedList(num_range)
    assert len(nums) == 17
