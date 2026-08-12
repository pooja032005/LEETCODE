class Solution(object):
    def reverse(self, x):
         MIN=-2**31
         MAX=2**31-1
         res=0
         sign=-1 if x<0 else 1
         x=abs(x)
         while x!=0:
            digit=x%10
            x//=10
            if res>MAX//10 or (res==MAX//10 and digit>7):
                return 0

            res=res*10+digit

         return sign*res

        