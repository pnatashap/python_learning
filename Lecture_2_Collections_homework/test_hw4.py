from hw4 import cache


def test_hw4():
    def func(a, b):
        return (a ** b) ** 2

    # я добавила еще фунцию, чтобы проверить
    def func2(a, b):
        return (a + b) ** 2

    cache_func = cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    cache_func2 = cache(func2)
    val_2 = cache_func(*some)

    val_3 = cache_func2(*some)
    val_4 = cache_func2(*some)

    assert val_1 is val_2
    assert val_3 is val_4
