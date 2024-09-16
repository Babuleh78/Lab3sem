
def input_coef():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    return a, b, c

def calc_disc(a, b, c):
    return b**2 - 4*a*c

def find_roots(a, b, c):
    D = calc_disc(a, b, c)
    roots = []
    if(D<0):
        return None
    elif(D == 0):
        x = -b/2/a
        if(x>0):
            roots+=[round(x**0.5, 4), round(-x**0.5), 4]
    else:
        x1 = -(b+D**0.5)/2/a
        x2 = -(b-D**0.5)/2/a
        if(x1>0):
            roots += [round(-x1**0.5, 4), round(x1**0.5, 4)]
        if(x2>0):
            roots += [round(-x2**0.5, 4), round(x2**0.5, 4)]
    return roots
   

def print_roots(roots):
    if roots is None:
        print("Уравнение не имеет действительных корней.")
    elif len(roots) == 2:
        print(f"Уравнение имеет два корня: {roots[0]} и {roots[1]}")
    else:
        print(f"Уравнение имеет четыре корня: +-{roots[0]} и +- {roots[2]}")

def main():
    try:
        a, b, c = input_coef()
        roots = find_roots(a, b, c)
        print_roots(roots)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()