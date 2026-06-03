class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        
        def generate_susbet(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return 
            if i == len(candidates) or total > target:
                return 
           
            
            cur.append(candidates[i])
            generate_susbet(i+1, cur, total + candidates[i])
            cur.pop()
         

            generate_susbet(i+1, cur, total)
        generate_susbet(0, [], 0)

        return [list(i) for i in res]