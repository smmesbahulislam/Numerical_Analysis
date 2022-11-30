import sympy as sy

def Multiple_Segment_Simpson():
    equation = input("Enter the equation: ")
    a, b = (map(float, input("Enter the lower_limit(a),upper_limit(b) : ").split(",")))
    n = int(input("Enter the number of segment(n): "))

    f = lambda x: eval(equation)
    g = lambda x: (0 * x)

    def exact_solution(a, b):
        x = sy.Symbol("x")
        exact = sy.integrate(f(x), (x, a, b))
        return exact

    def multi_segment_simpson(a, b, n):
        h = (b - a) / n

        sum = f(a) + f(b)

        for i in range(1, n):
            k = a + i * h
            if i % 2 == 0:
                sum = sum + 2 * f(k)
            else:
                sum = sum + 4 * f(k)
        sum = sum * h / 3
        return sum

    ans = multi_segment_simpson(a, b, n)
    exact_result = exact_solution(a, b)
    true_error = (exact_result - ans)
    true_percentage_error = (abs(true_error) / exact_result) * 100
    print("The result using Multiple Segment Simpson's 1/3rd Rule : %.4f" % ans)
    print("The true percentage error : %.4f" % true_percentage_error)


#run this code:
# Multiple_Segment_Simpson()