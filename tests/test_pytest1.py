import app as app

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(10, 5) == 5

def test_multiply():
    assert app.multiply(4, 5) == 20

def test_divide():
    assert app.divide(10, 2) == 5
