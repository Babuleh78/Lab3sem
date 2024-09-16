import sys
import math

def get_coef(to_print, i):
    
    try:
        coef_s= sys.argv[i]
        coef = float(coef_s)
    except (IndexError, ValueError):
        print(to_print)
        while(True):
            coef_s = input()
            try:
                coef = float(coef_s)
                break
            except ValueError:
                print("�������� ����! ������� ����� ��� ���:")
            
    return coef
    
def get_roots(a,b,c):
    roots = []
    D = b**2-4*a*c
    if(D <0):
        return roots
    elif(D == 0):
        x = -b/2/a
        if(x>0):
            roots += [round(x**0.5, 4), round(-x**0.5, 4)]
    else:
        x1 = -(b+D**0.5)/2/a
        x2 = -(b-D**0.5)/2/a
        if(x1>0):
            roots += [round(-x1**0.5, 4), round(x1**0.5, 4)]
        if(x2>0):
            roots += [round(-x2**0.5, 4), round(x2**0.5, 4)]
    return roots


def main():
   
    a = get_coef("������� �������� 1:", 1)
    b = get_coef("������� �������� 2:", 2)
    c = get_coef("������� �������� 3:", 3)
   
    roots = get_roots(a, b, c)
    if len(roots) == 0:
        print(f"��������� {int(a)}x^4 + {int(b)}x^2 + = 0 �� ����� ������.")
    elif len(roots) <= 4:
        root_list = ', '.join(map(str, roots))
        print(f"��������� {int(a)}x^4 + {int(b)}x^2 + {int(c)} = 0 ����� �����(��): {root_list}.")
    else:
        print("������: ������� ������ 4 ������.")

if __name__ == "__main__":
    main()