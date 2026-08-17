class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def solve(exp):
            if exp in memo :
                return memo[exp]

            results = []

            for i ,ch in enumerate(exp):
                if ch in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i+1:])

                    for  a in left:
                        for  b in right:
                            if ch == '+':
                                results.append(a+b)
                            elif ch == '-':
                                results.append(a-b)
                            else:
                                results.append(a*b)
                        
            if not results:
                results.append(int(exp))

            memo[exp] = results
            return results
        
        return solve(expression)

        