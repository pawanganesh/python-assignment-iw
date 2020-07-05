# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

class Validator:
    def __init__(self, brackets):
        self.brackets = brackets

    def bracket_validator(self):

        braces = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        length = len(self.brackets)

        if length % 2 == 0:
            al = length // 2
            d = al - 1

            if all(braces[self.brackets[d - i]] == self.brackets[al + i] for i in range(al)):
                return True
            else:
                return False
        else:
            return False

validator1 = Validator('[{()}]')
print('[{()}] :' ,validator1.bracket_validator())

validator1 = Validator('[)')
print('[) :' ,validator1.bracket_validator())

validator1 = Validator('({[)]')
print('({[)] :' ,validator1.bracket_validator())

validator1 = Validator('{{{')
print('{{{ :' ,validator1.bracket_validator())
