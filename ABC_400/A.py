"""TEST_DATA
10
#40

11
#-1

400
#1

"""

a = int(input())

answer = 400 // a

if answer * a == 400:
    print(answer)
else:
    print(-1)
