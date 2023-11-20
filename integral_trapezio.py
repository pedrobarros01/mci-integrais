
from integral import Integral
import math

class IntegralTrapezio(Integral):

    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None, func_integral=None, func_derivada_integral=None) -> None:
        super().__init__(limite_inf, limite_sup, h, quant_pontos, x, func_integral, func_derivada_integral)
        

    def erro_generalizado(self):
        derivada_2_grau_limite_inf = self.func_derivada_integral(self.limite_inf)
        derivada_2_grau_limite_sup = self.func_derivada_integral(self.limite_sup)
        maior = self.saber_maior(derivada_2_grau_limite_inf, derivada_2_grau_limite_sup)
        return abs(-1 * self.quant_pontos * (math.pow(self.h, 3) / 12) / maior)
    
    def erro_simples(self):
        derivada_2_grau_limite_inf = self.func_derivada_integral(self.limite_inf)
        derivada_2_grau_limite_sup = self.func_derivada_integral(self.limite_sup)
        maior = self.saber_maior(derivada_2_grau_limite_inf, derivada_2_grau_limite_sup)
        return abs(-1 * (self.h ** 3 / 12) * maior)
        
      
    def integral(self):
        for x in self.x:
            self.y.append(self.func_integral(x))
        primeiro = self.y.pop(0)
        ultimo = self.y.pop()
        cte = self.h / 2
        soma = 0
        for y in self.y:
            soma += (2 * y)
        return cte * (primeiro + soma + ultimo)

if __name__ == '__main__':
    int_trapezio_1_questao = IntegralTrapezio(
        limite_inf=0, 
        limite_sup=1, 
        h=0.1,
        func_integral=lambda x: x * math.sqrt(x**2 + 1),
        func_derivada_integral=lambda x: ((2 * math.pow(x, 3) + 3 * x)) / ((math.pow(x, 2) + 1) * (math.sqrt(x**2 + 1)))
        )
    print(f'Erro Geral = {int_trapezio_1_questao.erro_generalizado()}')
    print(f'F(x) 1°q = {round(int_trapezio_1_questao.integral(), 5)}')

    int_trapezio_2_questao = IntegralTrapezio(
        limite_inf=0,
        limite_sup=1,
        h=0.02,
        func_integral=lambda x: 1 / (0.25 - math.cos(x) + 1),
        func_derivada_integral=lambda x: (-1 * math.cos(x) * (-math.cos(x) + 1.25) - 2 * math.pow(math.sin(x), 2)) / ((-math.cos(x) + 1.25) ** 3)
    )
    print(f'Erro geral = {int_trapezio_2_questao.erro_generalizado()}')
    print(f'F(x) 2°q= {(int_trapezio_2_questao.integral())}')
    


        
