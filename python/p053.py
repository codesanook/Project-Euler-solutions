# 
# Solution to Project Euler problem 53
# by Project Nayuki
# 
# http://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import eulerlib


def compute():
	ans = 0
	for n in range(1, 101):
		for k in range(0, n + 1):
			if eulerlib.binomial(n, k) > 1000000:
				ans += 1
	return str(ans)


if __name__ == "__main__":
	print(compute())
