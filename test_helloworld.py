from myplugin import say_hello


def test_helloworld_without_argument():
    say_hello()


def test_helloworld_with_argument():
    say_hello("new world")