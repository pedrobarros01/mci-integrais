
from integral import Integral
import math

class IntegralTrapezio(Integral):

    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None) -> None:
        super().__init__(limite_inf, limite_sup, h, quant_pontos, x)
        

    def erro_generalizado(self):
        return super().erro_generalizado()
    
    def erro_simples(self):
        return super().erro_simples()
    
    def funcao_derivada(self, x: int | float):
        return super().funcao_derivada(x)
    
    def funcao_integral(self, x: int | float):
        return x * math.sqrt(x**2 + 1)
    
    def integral(self):
        for x in self.x:
            self.y.append(self.funcao_integral(x))
        primeiro = self.y.pop(0)
        ultimo = self.y.pop()
        cte = self.h / 2
        soma = 0
        for y in self.y:
            soma += (2 * y)
        return cte * (primeiro + soma + ultimo)

if __name__ == '__main__':
    int_trapezio = IntegralTrapezio(limite_inf=0, limite_sup=1, h=0.1)
    print(round(int_trapezio.integral(), 5))


        
