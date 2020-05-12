
def main():
    a = ['ab', 'bc', 'cd']
    b = permutation(a)
    print(b)

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    
    l = []

    for i in range(len(lst)):
        m = lst[i]
        remaining_list = lst[:i] + lst[i + 1:]
        for p in permutation(remaining_list):
            l.append([m] + p)
    return l

if __name__ == "__main__":
    main()