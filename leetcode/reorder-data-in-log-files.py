import heapq
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters= []
        nums = []
        for log in logs:
            if log[-1].isdigit():
                nums.append(log)
            else:
                letters.append(log)
               

        letters.sort(key=lambda x: (x.split(" ")[1:] , x.split(" ")[0]))
       
        return letters + nums