class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        print(seats, students)

        total_moves = 0
    
        # Calculate the moves required for each student to reach a seat
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        
        return total_moves

        