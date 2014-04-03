from truncate import trunc


STRING = "This is a sentance. This is another."


def test_smaller_than_limit():
    result = trunc(STRING, max_pos=1000)

    assert STRING + '...' == result


def test_with_period_before_max_pos():
    result = trunc(STRING, max_pos=STRING.find('.') + 3)

    assert 'This is a sentance...' == result


def test_first_space_before_max_pos():

    for i in range(5, 8):
        result = trunc(STRING, max_pos=i)
        assert 'This...' == result


def test_no_space_or_period():
    string = 'ThisisasentanceThisisanother'

    result = trunc(string, max_pos=5)

    assert 'Thisi...' == result
