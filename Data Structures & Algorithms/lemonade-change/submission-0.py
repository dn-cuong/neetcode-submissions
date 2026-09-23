class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        income = 0
        for i in range(len(bills)):
            change = bills[i] - 5
            income += 5

            if income < change:
                return False
            
            income -= change

        return True