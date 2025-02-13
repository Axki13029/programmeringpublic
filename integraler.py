def trapezoidal_rule(func, a, b, n):
    """
    Approximate the integral of func from a to b using the trapezoidal rule.
    
    :param func: Function to integrate (callable).
    :param a: Lower limit of integration.
    :param b: Upper limit of integration.
    :param n: Number of trapezoids.
    :return: Approximation of the integral.
    """
    h = (b - a) / n  # Width of each trapezoid
    result = 0.5 * (func(a) + func(b))  # Endpoints contribution
    
    for i in range(1, n):
        x = a + i * h
        result += func(x)
    
    result *= h
    return result

if __name__ == "__main__":
    print("Welcome to the Integral Solver!")
    print("You can integrate functions like 'x**2 + 3*x + 1'.")
    
    # Get user input
    function_input = input("Enter the function to integrate (in terms of x): ")
    lower_limit = float(input("Enter the lower limit of integration: "))
    upper_limit = float(input("Enter the upper limit of integration: "))
    num_trapezoids = int(input("Enter the number of trapezoids to use: "))
    
    # Define the function
    def f(x):
        return eval(function_input)  # Evaluate the user's function

    # Calculate the integral
    integral_value = trapezoidal_rule(f, lower_limit, upper_limit, num_trapezoids)
    
    print(f"The integral of {function_input} from {lower_limit} to {upper_limit} is approximately {integral_value}")
