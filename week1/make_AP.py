temp = 0
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
            
        return True
    
