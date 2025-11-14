class Complex:
    def __init__(self, reg, imag):
        self.reg = reg
        self.imag = imag

    def __str__(self):
        return f'{self.reg} " + " {self.imag}+"i" '

    def __repr__(self):
        return f"Complex({self.reg}, {self.imag})"


    def re(self):
        return self.reg
    def im(self):
        return self.imag

    def add(self, other):
        return Complex(self.reg + other.reg, self.imag + other.imag)
    def sub(self, other):
        return Complex(self.reg - other.reg, self.imag - other.imag)
    def mul(self, other):
        return Complex(self.reg * other.reg, self.imag * other.imag)
    def div(self, other):
        return Complex(self.reg / other.reg, self.imag / other.imag)




