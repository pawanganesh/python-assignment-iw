# Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.

# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

class ZeroSum:
    def real_num_sum(self, lst):
        result = []
        l = len(lst)
        for a in range(0, l-2):
            for b in range(a+1, l-1):
                for c in range(b+1, l):
                    if (lst[a] + lst[b] + lst[c] == 0):
                        temp = [lst[a], lst[b], lst[c]]
                        result.append(temp)
        if result == []:
            return 'Not Found'
        else:
            return result


real_num1 = [-25, -10, -7, -3, 2, 4, 8, 10]
real_num2 = [1, 5, 34, 2, 11, 21, 12, 25]
real_num3 = [1, -1, 0, -34, -11, 21, 11, 21]
zero_sum = ZeroSum()
print(zero_sum.real_num_sum(real_num1))
print(zero_sum.real_num_sum(real_num2))
print(zero_sum.real_num_sum(real_num3))