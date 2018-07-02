def generate_permutations(N:int, M:int=-1, prefix=None):
    """Generation all permutations of N numbers in M positions
       with prefix
    """
    M = N if M == -1 else M # by default N numbers in N positions
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(9,9)
