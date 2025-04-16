"""TEST_DATA
4 2
<expected> 5

5 3
<expected> 9

5 2
<expected> 8

10 20
<expected> 1

1000000 500000
<expected> 420890625

10 3
<expected> 193

4 4
<expected> 4

"""

n, k = map(int, input().split())

if k > n:
    # K could be larger then N.
    print(1)
    exit()

# Limit Time Error (LTE)
# a = [1] * k
# a.append(k)

# for i in range(k + 1, n + 1):
#     prev = a[-1]
#     shift_out = a.pop(0) # remove one item from the left
#     sum = prev * 2 - shift_out
#     # print(f"i: {i} -> {sum}")
#     a.append(sum % 1_000_000_000) # answer the mod of 10^9 means overflow at 10^9
# print(a[-1])

a = [1] * (n + 1)
a[k] = k

for i in range(k + 1, n + 1):
    prev = a[i - 1]
    shift_out = a[i - 1 - k]
    sum = prev * 2 - shift_out
    # print(f"i: {i} -> {sum}")
    a[i] = sum % 1_000_000_000
print(a[n])

# a = [1] * k
# a.append(k)

# MOD = len(a)

# if k == n:
#     print(k)
#     exit()

# for i in range(k + 1, n + 1):
#     prev = a[(i - 1) % MOD]
#     shift_out = a[i % MOD]
#     sum = prev * 2 - shift_out
#     # print(f"i: {i} -> {sum}")
#     a[i % MOD] = sum % 1_000_000_000
# print(a[i % MOD])
