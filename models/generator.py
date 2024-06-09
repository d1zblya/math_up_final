from math import floor
from random import randint, choice, random
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib
matplotlib.use('Agg')

class MathProblemGenerator():
    # для разделения строки на числа и возвращаение индексов начала и конца чисел в строке
    def separation_of_nums(self, expression: str):
        exp = list(expression)
        nums = '1234567890.'
        for i in range(len(exp)):
            # A - цифра, B - строка *A A B A B A A*
            if exp[i] in nums:
                exp[i] = 'A'
            else:
                exp[i] = 'B'
        begin = []
        end = []
        for i in range(len(exp) - 1):
            syb = exp[i] + exp[i + 1]
            if syb == 'AB':
                end.append(i)
            elif syb == 'BA':
                begin.append(i)
        if expression[-1] in nums:
            end.append(len(exp) - 1)
        if expression[0] in nums:
            begin = [-1] + begin
        return [(x + 1, y + 1) for x, y in zip(begin, end)]         
        
    def __init__(self):
        self.funcs = []
        
    def add_funcs(self, func):
        self.funcs.append(func)
    
    # приминение рандомной функции к числу
    def complication(self, num: int):
        return choice(self.funcs)(num)
    
    # усложнениие примера
    def rnd_complication(self, expression: str):
        x, y = choice(self.separation_of_nums(expression))
        expression = expression[:x] + '(' + self.complication(float(expression[x:y])) + ')' + expression[y:]
        return expression
    
    # усложнение примера с шаагами
    def rnd_complication_with_steps(self, answer: int, steps: int):
        answer = str(answer)
        for _ in range(steps):
            answer = self.rnd_complication(answer)
        return answer
    
    def get_problem(self) -> int:
        rnd_num = randint(1, 100)

        plt.axis("off")
        latex_expression = self.rnd_complication_with_steps(rnd_num, 3)
        plt.text(0.5, 0.5, "$" + latex_expression + "$", horizontalalignment='center', verticalalignment='center', fontsize=20)
        plt.savefig('static/img/problem.png', bbox_inches='tight', pad_inches=0)
        plt.clf()
        
        return rnd_num
        

# округление чисел до заданной велечины и обертывание в скобки, если < 0 
def rounding_nums(*args, acc=2):
    rounded_nums = []
    for arg in args:
        num = round(arg, acc)
        if num > 0:
            num = str(num)
        else:
            num = f'({str(num)})'
        rounded_nums.append(num)
    return rounded_nums

# усложнение суммой    
def difficult_sum(num: int):
    rnd = [randint(1, 100), round(random() * 10, 3), round(random() * 100, 3)]
    a = choice(rnd)
    b = num - a
    a, b = rounding_nums(a, b)
    return f'{a} + {b}'

# усложнение разностью
def difficult_sub(num: int):
    rnd = [randint(1, 100), round(random() * 10, 3), round(random() * 100, 3)]
    a = choice(rnd)
    b = a - num
    a, b = rounding_nums(a, b)
    return f'{a} - {b}'

# усложнение делением
def difficult_div(num: int):
    if '.' in str(num):
        f = str(num)
        difference = '0' + f[f.find('.'):]
        
        num = num - float(difference)
        num = str(num)
        num = int(num[:num.find('.')])
        
        b = randint(1, 50)
        a = b * num
        if difference == '0.0':
            return '\\frac{' + str(a) + '}{' + str(b) + '}'
        else:
            return '\\frac{' + str(a) + '}{' + str(b) + '}' + ' + ' + difference
    else:
        b = randint(1, 50)
        a = b * num
        return '\\frac{' + str(a) + '}{' + str(b) + '}'

# усложнение умножением   
def difficult_mul(num: int):
    if '.' in str(num):
        f = str(num)
        difference = '0' + f[f.find('.'):]
                
        num = num - float(difference)
        num = str(num)
        num = int(num[:num.find('.')])
                
        b = choice([2, 4, 5, 8, 10, 25, 50, 100, 200])
        a = num / b
        if difference == '0.0': 
            return f'{a} * {b}'
        else:
            return f'{a} * {b} + {difference}'
    else:
        b = choice([2, 4, 5, 8, 10, 25, 50, 100, 200])
        a = num / b
        return f'{a} * {b}'

# gen = MathProblemGenerator()
# gen.add_funcs(difficult_sum)
# gen.add_funcs(difficult_sub)
# gen.add_funcs(difficult_div)
# gen.add_funcs(difficult_mul)

# print(f'Пример: {gen.rnd_complication_with_steps(rnd_num, 2)}; Ответ: {rnd_num}')

    
    
