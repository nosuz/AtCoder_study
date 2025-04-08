"""TEST_DATA
10
<expected> 40

11
<expected> -1

400
<expected> 1

"""

a = int(input())

answer = 400 // a

if answer * a == 400:
    print(answer)
else:
    print(-1)
