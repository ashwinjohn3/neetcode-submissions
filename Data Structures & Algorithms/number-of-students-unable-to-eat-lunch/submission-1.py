from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # O(N)
        std_cnt = Counter(students)
        rest = len(students)
        for sandwich in sandwiches: 
            if std_cnt[sandwich] > 0:
                std_cnt[sandwich] -= 1
                rest -= 1
            else: 
                break
        return rest
            



            



             




        