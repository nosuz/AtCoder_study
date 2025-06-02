#!/usr/bin/python3

# python3 validate.py sample.py

# {{problem_url}}

"""TEST_DATA
{% for example in examples %}{{example.0}}
<expected> {{example.1}}

{% endfor %}
"""

a = int(input())

a, b = input().split()

a, b = map(int, input().split())
n, m = map(int, input().split())

a = list(map(int, input().split()))
