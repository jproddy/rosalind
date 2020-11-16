'''
Find the Minimum Number of Coins Needed to Make Change
http://rosalind.info/problems/ba5a/

Given: An integer money and an array Coins of positive integers.

Return: The minimum number of coins with denominations Coins that changes money.
'''
filename = 'rosalind_ba5a.txt'

def min_coins(money, coins):
	# returns -1 if making change is not possible
	arr = [0] * (money + 1)
	c = sorted(coins, reverse=True)
	for amt in range(1, money + 1):
		lower_cases = [arr[amt-coin] for coin in c if amt - coin >= 0]
		if lower_cases:
			arr[amt] = min(lower_cases) + 1
	return arr[money]

def main():
	with open(filename) as f:
		money = int(f.readline().strip())
		coins = list(map(int, f.readline().strip().split(',')))
	print(min_coins(money, coins))

if __name__ == '__main__':
	main()
