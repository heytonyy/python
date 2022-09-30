
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result += num
        for arg in nums:
            self.result += arg
        return self
    def subtract(self, num, *nums):
        # your code here
        self.result -= num
        for arg in nums:
            self.result -= arg
        return self

# create an instance:
md = MathDojo()

# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result

# should print 5
print(x)

# run each of the methods a few more times and check the result!
y = md.add(1).subtract(1,3,1).add(5,5).subtract(1).result
print(y)
