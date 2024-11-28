def is_number(s):
    try:
        float(s)  # Use int(s) if you only care about integers
        return True
    except ValueError:
        return False

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = 0
        previous = []
        
        for operation in operations:
            if is_number(operation):
                previous.append(int(operation))
            
            if operation == "+":
                previous.append( previous[len(previous) - 1] + previous[len(previous) - 2] )

            if operation == "D":           
                previous.append( previous[len(previous) - 1] * 2 )
            
            if operation == "C":
                previous.pop()
            
            print(f"{previous}")

        return sum(previous)
        

        
