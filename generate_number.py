def generate_number(N:int, M:int, prefix=None):
    """Generate all numbers in N-notation (N <= 10) 
       with length M.
       This script uses RECURSION. 
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


generate_number(5, 3)
