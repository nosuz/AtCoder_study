"""TEST_DATA
6
login
private
public
logout
private
public
<expected> 1

4
private
private
private
logout
<expected> 3

20
private
login
private
logout
public
logout
logout
logout
logout
private
login
login
private
login
private
login
public
private
logout
private
<expected> 3

"""

n = int(input())

login = False
failed = 0
for _ in range(n):
    s = input()
    if s == "login":
        login = True
    elif s == "logout":
        login = False
    elif not login and (s == "private"):
        failed += 1

print(failed)
