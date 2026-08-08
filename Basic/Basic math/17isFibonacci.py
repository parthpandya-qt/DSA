import math

def isSquare(n):
	if n < 0:
		return False
	root = int(math.sqrt(n))
	return root * root == n


def isFibonacci(n):
	if n < 0:
		return False
	if n == 0 or n == 1:
		return True
	return isSquare(5 * n * n + 4) or isSquare(5 * n * n - 4)


if __name__ == "__main__":
	num = int(input())
	print(isFibonacci(num))