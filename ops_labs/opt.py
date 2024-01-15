
def f(x):
    return 2 * x**3 + 3 * x**2 + 4 * x + 5

def triangle_search(a, b, epsilon, L):
    x0 = b

    iterations = 0
    while b - a > epsilon:
        iterations += 1
        fa = f(a)
        fb = f(b)
        x0 = ((a + b) / 2) + ((fa - fb) / 2*L)
        x1 = ((a + x0) / 2) + ((fa - f(x0)) / 2*L)
        x2 = ((x0 + b) / 2) + ((f(x0) - fb) / 2*L)

        if f(x1) <= f(x2):
            b = x2
            x0 = x1
        else:
            a = x1
            x0 = x2

    return x0, iterations

# Заданный отрезок (-2, -1) и точность 0.5 * 10^-5
start_interval = -2
end_interval = -1
tolerance = 0.5 * 10**-5

# константа Липшица
L = 0.05

min_point, iterations = triangle_search(start_interval, end_interval, tolerance, L)
min_value = f(min_point)

print(f"Минимум функции: x = {min_point}, y = {min_value}. Найден за {iterations} итераций")

