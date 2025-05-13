class Solution(object):
    def reverse(self, x):
        sum=0
        neg=False
        if x<0:
            neg=True
            x=-x
        while(x>0):
            temp = x%10
            sum=sum*10 + temp
            x//=10
        if neg:
           sum=-sum
        if sum < -2**31 or sum > 2**31 - 1:
            return 0
        return sum
        