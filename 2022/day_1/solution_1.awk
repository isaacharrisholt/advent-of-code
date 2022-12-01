BEGIN {
	sum = 0
	max = 0
	}
NF > 0  {
		sum += $1
	}
NF == 0 {
		if (sum > max) max = sum
		sum = 0
	}
END { print max }
