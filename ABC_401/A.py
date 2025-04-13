"""TEST_DATA
200
<expected> Success

401
<expected> Failure

999
<expected> Failure

"""

s = int(input())

if 299 >= s >= 200:
    print("Success")
else:
    print("Failure")
