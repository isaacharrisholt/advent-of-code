BEGIN {
        sum = 0
        first = 0
        second = 0
        third = 0
        }
NF > 0  {
                sum += $1
        }
NF == 0 {
                if (sum > first) 
                {
                        third = second;
                        second = first;
                        first = sum;
                }       
                else if (sum > second)
                {
                        third = second;
                        second = sum;
                }
                else if (sum > third)
                {
                        third = sum;
                }
                sum = 0
        }
END { print first + second + third }

