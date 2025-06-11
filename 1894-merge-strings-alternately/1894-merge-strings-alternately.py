class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sizeWord1, sizeWord2 = len(word1), len(word2)
        index = 0
        mergedString = ""

        while(index < sizeWord1 and index < sizeWord2):
            mergedString += (word1[index] + word2[index])
            index+=1
        while(index < sizeWord1):
            mergedString += word1[index]
            index+=1

        while(index < sizeWord2):
            mergedString += word2[index]
            index+=1

        return mergedString