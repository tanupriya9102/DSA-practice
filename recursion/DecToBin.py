# DECIMAL TO BINARY NUMBER
from unicodedata import digit


# STEPS
# 1.Divide the number by 2.
# 2.Get int quotient for next iteration
# 3.Get remainderfor binary digit
# 4.Repeat till quotient is 0

def dtb(n):
    assert n==int(n)
    if n==0:
        return 0
    else:
        return ((n%2)+10*dtb(int(n/2)))
print(dtb(-14))