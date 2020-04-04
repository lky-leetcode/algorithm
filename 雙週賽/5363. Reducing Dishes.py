#A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
#Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]
#Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.
#Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
#23nd two weekly contest
#第4題

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        maxValue = 0
        tempMaxValue = 0
        countNonZero = 0
        for value in satisfaction:
            if value < 0:
                countNonZero += 1
            else:
                break
        for i in range(countNonZero, len(satisfaction)):
            maxValue += (i - countNonZero + 1) * satisfaction[i]
            
        for i in range(countNonZero, -1, -1):
            tempMaxValue = 0
            for j in range(i, len(satisfaction)):
                tempMaxValue += (j - i + 1) * satisfaction[j]
            if tempMaxValue > maxValue:
                maxValue = tempMaxValue

        return maxValue
            
                
        
            