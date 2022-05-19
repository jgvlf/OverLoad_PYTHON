from multipledispatch import dispatch


class WMultipleDispatch:
    def __init__(self):
        pass

    @staticmethod
    @dispatch(int, int)
    def somar(n1, n2):
        return n1 + n2

    @staticmethod
    @dispatch(int, int, int)
    def somar(n1, n2, n3):
        return n1 + n2 + n3
