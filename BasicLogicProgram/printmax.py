


def solve(a, n, k, index, sum, maxsum):

    if (k == 1):
        maxsum = max(maxsum, sum)
        sum = 0
        for i in range(index, n):
            sum += a[i]
        maxsum = max(maxsum, sum)
        return

    sum = 0
    for i in range(index, n):
        sum += a[i]


        maxsum = max(maxsum, sum)
        solve(a, n, k - 1, i + 1, sum, maxsum)
if __name__ == "__main__":
    arr = [10, 5, 2, 7, 8, 7]
    k = 3
    n = 6
    solve(arr, n, k, 0, 0, 0)

    print(solve())