#!/usr/bin/python3

# python3 validate.py sample.py

# {{contents.title}}
# {{contents.url}}

"""TEST_DATA
{% for example in contents.examples %}{{example.0}}
<expected> {{example.1}}

{% endfor %}
"""

A = int(input())

A, B = input().split()

A, B = map(int, input().split())
N, M = map(int, input().split())

A = list(map(int, input().split()))
