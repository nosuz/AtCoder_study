#!/usr/bin/python3

"""TEST_DATA
AtCoderBeginnerContest
<expected> ACBC

PaymentRequired
<expected> PR

program
<expected>

"""

import re

s = input()

result = re.sub(r'[^A-Z]', "", s)

print(result)
