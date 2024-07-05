class Solution(object):
    def finalValueAfterOperations(self, operations):
        result = 0
        for operation in operations:
            if operation ==  "++X" or operation == "X++":
                result = result + 1
            elif operation ==  "--X" or operation == "X--":
                result = result - 1
        return result
        