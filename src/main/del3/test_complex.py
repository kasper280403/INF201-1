#Kasper S. Karlsen
import pytest
from complex import Complex

def test_str():
    assert str(Complex(1, 2)) == "1+2i"
    assert str(Complex(3, -4)) == "3-4i"

def test_repr():
    assert repr(Complex(1, 2)) == "Complex(1, 2)"

def test_re_im():
    z = Complex(5, -3)
    assert z.re() == 5
    assert z.im() == -3

def test_add():
    z = Complex(1, 2).add(Complex(3, 4))
    assert z.reg == 4 and z.imag == 6

def test_sub():
    z = Complex(5, 7).sub(Complex(2, 3))
    assert z.reg == 3 and z.imag == 4

def test_mul():
    z = Complex(2, 3).mul(Complex(4, 5))
    assert z.reg == 8 and z.imag == 15

def test_div():
    z = Complex(8, 9).div(Complex(2, 3))
    assert z.reg == 4 and z.imag == 3