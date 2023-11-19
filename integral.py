from abc import ABC, abstractmethod

class Integral(ABC):
    def __init__(self, 
                 limite_inf: int = None, 
                 limite_sup:int = None, 
                 h: float = None, 
                 quant_pontos:int = None, 
                 x: list[float] = None
                 ) -> None:
        self.y = []
        if h is None:
            self.x = x
            self.limite_inf = x[0]
            self.limite_sup =  x[-1]
            self.h = (self.limite_sup - self.limite_inf) / quant_pontos
        else:
            self.h = h
            self.limite_inf = limite_inf
            self.limite_sup = limite_sup
            self.x = []
            self.criar_vetor_x()

    def criar_vetor_x(self):
        i = self.limite_inf
        while i <= self.limite_sup:
            self.x.append(i)
            i += self.h        
    @abstractmethod
    def funcao_integral(self, x: int | float):
        pass

    @abstractmethod
    def funcao_derivada(self, x: int | float):
        pass

    @abstractmethod
    def erro_simples(self):
        pass

    @abstractmethod
    def erro_generalizado(self):
        pass

    @abstractmethod
    def integral(self):
        pass
