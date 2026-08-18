class Solution(object):
    def mirrorDistance(self, n):
        original =  n
        reverse  = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10

        return abs(original - reverse)
