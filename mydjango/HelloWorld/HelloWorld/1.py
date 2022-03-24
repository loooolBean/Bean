class Solution:
    def sumup(self, inputArray):
        sum1=0
        for i in len(inputArray):
            if  inputArray[i] > inputArray[0]:
                sum1+=inputArray[i]
                i+=1
        return sum1