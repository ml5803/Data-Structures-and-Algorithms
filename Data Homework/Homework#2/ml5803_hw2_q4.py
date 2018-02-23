def e_approx(n):
    temp_factorial = 1
    approx = 0
    for i in range(1,n+2):
        approx += 1/temp_factorial
        temp_factorial *= i
    return approx

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

main()