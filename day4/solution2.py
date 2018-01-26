"""
--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle input is still iwrupvqb.
"""

import hashlib

input = "iwrupvqb"
count = 1
while True:
    if hashlib.md5((input + str(count)).encode('UTF-8')).hexdigest()[0:6] == '000000':
        print(count)
        break
    count += 1
