

def main():
    with open('in.txt') as f:
        line = f.readline()
        crabs = list(map(int, line.split(',')))
        res = 1e+9
        left = min(crabs)
        right = max(crabs)
        for i in range(left, right+1):
            cur = 0
            for item in crabs:
                n = abs(item - i) + 1
                cur += n * (n - 1) // 2

            if cur < res:
                res = cur

        print(res)


if __name__ == '__main__':
    main()