from datafake import CURRENCY_NAMES, EXCHANGE_RATE

class Currency:
    def __init__(self, valor, code):
        self.valor = valor
        self.code = code.upper()

    def __str__(self):
        return f"{self.valor:.2f}{self.code}"

    def __eq__(self, dr):
        if (self.code == dr.code):
            return self.valor == dr.valor
        return self == dr.convert(self.code)
    
    def __gt__(self, dr):
        if self.code == dr.code:
            return self.valor > dr.valor
        return self > dr.convert(self.code)
    
    def __ge__(self, dr):
        return (self > dr) or (self == dr)
    
    def __add__(self, dr):
        if self.code == dr.code:
            return Currency(self.valor + dr.valor, self.code)
        raise ValueError("Moedas devem ser do mesmo país!")

    def __neg__(self):
        return Currency(-self.valor, self.code)
    
    def __sub__(self, dr):
        return self + (-dr)
    
    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return Currency(self.valor * n, self.code)
        raise ValueError(f"{n} deve ser um valor inteiro ou float.")

    def __rmul__(self, es):
        return self * es

    def __truediv__(self, dr):
        if isinstance(dr, int) or isinstance(dr, float):
            return Currency(self.valor / dr, self.code)
        raise ValueError(f"{dr} deve ser um valor inteiro ou float.")

    def __floordiv__(self, dr):
        if isinstance(dr, int) or isinstance(dr, float):
            return Currency(self.valor // dr, self.code)
        raise ValueError(f"{dr} deve ser um valor inteiro ou float.")

    def convert(self, to_code):
        rate = EXCHANGE_RATE[self.code][to_code]
        to_code = to_code.upper()
        value = rate * self.valor
        return Currency(value, to_code)





moeda1 = Currency(50, "BRL")
moeda2 = Currency(52, "BE")

print(moeda1 * moeda2)
