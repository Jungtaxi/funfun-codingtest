# https://leetcode.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [], []
        for ls in logs:
            if ls.split()[1].isdigit():
                dig.append(ls)
            else:
                let.append(ls)
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let + dig
