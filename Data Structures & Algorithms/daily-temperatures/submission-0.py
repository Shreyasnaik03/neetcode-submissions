class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result = []

        for i in range(l):
            count = 1
            j = i+1
            while j< l :
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == l else count 
            result.append(count)
        return result
        