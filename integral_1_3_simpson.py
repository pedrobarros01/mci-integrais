from integral import Integral
import math

class IntegralUmTercoSimpson(Integral):
    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None, func_integral=None, func_derivada_integral=None) -> None:
        super().__init__(limite_inf, limite_sup, h, quant_pontos, x, func_integral, func_derivada_integral)
        

    def erro_generalizado(self):
        return super().erro_generalizado()
    
    def erro_simples(self):
        return super().erro_simples()
    
    def integral(self):
        for x in self.x:
            self.y.append(self.func_integral(x))
        
        primeiro = self.y.pop(0)
        ultimo = self.y.pop()
        cte = self.h / 3
        somaImpares = 0
        somaPares = 0
        for i in  range(0, len(self.y)):
            if i  % 2 == 0:
                somaImpares += (4 * self.y[i])
            if i % 2 == 1:
                somaPares += (2 * self.y[i])
        return cte * (primeiro + somaImpares + somaPares + ultimo)
    


if __name__ == '__main__':
    inte_1_3_simpson = IntegralUmTercoSimpson(
            limite_inf=0, 
            limite_sup=1, 
            h=0.1, 
            func_integral=lambda x: x * math.sqrt(x**2 + 1)
            )
    print(round(inte_1_3_simpson.integral(), 5))