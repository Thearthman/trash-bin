import math


def npr(_n: int, _r: int):
    return math.factorial(_n) / math.factorial(_n - _r)


def ncr(_n: int, _r: int):
    return math.factorial(_n) / (math.factorial(_n - _r) * math.factorial(_r))


class Binomial():
    def __init__(self, n: int , p: float ):
        self._n = n
        self._p = p
        self._q = 1 - p

    def __str__(self) -> str:
        return str("X~B(" + str(self._n) + str(self._p) + ')')

    def P(self, equality: str, _k: int):
        _probability_when_X_equals_K = (self._p ** _k) * (self._q ** (self._n - _k)) * \
                                      ncr(self._n, _k)
        if equality == '=':
            return _probability_when_X_equals_K
        elif equality == '<=':
            for i in range(_k):
                _probability_when_X_equals_K += (self._p ** i) * (self._q ** (self._n - i)) * \
                                               ncr(self._n, i)
            return _probability_when_X_equals_K
        elif equality == '<':
            _probability_when_X_equals_K = 0
            for i in range(_k):
                _probability_when_X_equals_K += (self._p ** i) * (self._q ** (self._n - i)) * \
                                               ncr(self._n, i)
            return _probability_when_X_equals_K
        elif equality == '>':
            for i in range(_k):
                _probability_when_X_equals_K += (self._p ** i) * (self._q ** (self._n - i)) * \
                                               ncr(self._n, i)
            return 1 - _probability_when_X_equals_K
        else:
            _probability_when_X_equals_K = 0
            for i in range(_k):
                _probability_when_X_equals_K += (self._p ** i) * (self._q ** (self._n - i)) * \
                                               ncr(self._n, i)
            return 1 - _probability_when_X_equals_K

    def Exp(self):
        return self._n * self._p

    def Var(self):
        return self.Exp() * self._q


class Geometric():
    def __init__(self,*, p: float):
        self._p = p
        self._q = 1 - self._p

    def __str__(self) -> str:
        return str("X~Geo(" + str(self._p) + ')')

    def P(self, equality: str, _k: int):
        _probability_when_X_equals_K = self._p * (self._q ** (_k - 1))
        if equality == '=':
            return _probability_when_X_equals_K
        elif equality == '<=':
            return 1 - ((1 - self._p) ** _k)
        elif equality == '>':
            return (1 - self._p) ** _k
        elif equality == '=>':
            return _probability_when_X_equals_K + ((1 - self._p) ** _k)
        elif equality == '<':
            return 1 - _probability_when_X_equals_K - ((1 - self._p) ** _k)

    def Exp(self):
        return 1 / self._p

    def Var(self):
        return self._q / (self._p ** 2)

class Poisson():
    def __init__(self, l: float ):
        self._l = l

    def __str__(self) -> str:
        return str("X~Po("+ str(self._l)+')')

    def P(self,equality:str ,_k:int):
        _probability_when_X_equals_K = math.e**(-self._l)*self._l**_k/math.factorial(_k)
        if equality == '=':
            return _probability_when_X_equals_K
        elif equality == '<=':
            for i in range(_k):
                _probability_when_X_equals_K += math.e**(-self._l)*self._l**_k/ \
                                               math.factorial(i)
            return _probability_when_X_equals_K
        elif equality == '>':
            for i in range(_k):
                _probability_when_X_equals_K += math.e**(-self._l)*self._l**_k/ \
                                               math.factorial(i)
            return 1 - _probability_when_X_equals_K
        elif equality == '<':
            _probability_when_X_equals_K = 0
            for i in range(_k):
                _probability_when_X_equals_K += math.e**(-self._l)*self._l**_k/ \
                                               math.factorial(i)
            return _probability_when_X_equals_K
        elif equality == '>=':
            _probability_when_X_equals_K = 0
            for i in range(_k):
                _probability_when_X_equals_K += math.e ** (-self._l) * self._l ** _k / \
                                                math.factorial(i)
        return 1 - _probability_when_X_equals_K

    def Exp(self):
        return self._l

    def Var(self):
        return self._l