import logging

# ex1
logging.basicConfig(level=logging.DEBUG, filename="hw23.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")


class Calculator:
    @staticmethod
    def nums_sum(a, b):
        return a + b

    @staticmethod
    def nums_sub(a, b):
        return a - b

    @staticmethod
    def nums_mult(a, b):
        return a * b

    @staticmethod
    def nums_div(a, b):
        if b == 0:
            logging.warning("Zero Division Error")
            return None
        else:
            return a / b

    @staticmethod
    def nums_max(a, b):
        if a > b or a == b:
            return a
        else:
            return b

    @staticmethod
    def nums_min(a, b):
        if a > b or a == b:
            return b
        else:
            return a

    @staticmethod
    def nums_sqr(a, b):
        return a ** b

    @staticmethod
    def nums_prec(a, b):
        return a * b / 100
# ex 2


def factorial(n):
    if n < 0:
        logging.warning("Negative factorial Error")
        raise ValueError
    if n is not int:
        logging.warning("Wrong Type Error")
        raise ValueError
    if n is not int:
        raise
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
