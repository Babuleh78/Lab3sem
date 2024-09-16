class Bikvadrat:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def solve(self):
        D = self.b**2 - 4 * self.a * self.c
        if D< 0:
            return "��������� �� ����� ������������ ������."
    
        y1 = (-self.b + D**0.5) / (2 * self.a)
        y2 = (-self.b - D**0.5) / (2 * self.a)
        roots = []
        if y1 >= 0:
            roots.append(round(y1**0.5,4))
            roots.append(round(-y1**0.5, 4))
        if y2 >= 0:
            roots.append(round(y2**0.5,4))
            roots.append(round(-y2**0.5,4))
        return roots if roots else "��������� �� ����� ������������ ������."
def main():
    a = float(input("������� ����������� a: "))
    b = float(input("������� ����������� b: "))
    c = float(input("������� ����������� c: "))
    ans = Bikvadrat(a, b, c)
    roots = ans.solve()
    print("����� ���������:", roots)

if __name__ == "__main__":
    main()