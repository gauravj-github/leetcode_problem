class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        p=x
        temp = 0
        sum =0

        while(x>0):
            temp= x%10
            sum =(sum*10) +temp
            x=x//10
       
        return sum == p

        