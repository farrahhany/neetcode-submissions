class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        #step 1: count how many times each number appears
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        #step 2: oragnize nums by their frequency count
        for n , c in count.items():
            freq[c].append(n)

        
        res = []
        for i in range(len(freq)-1 , 0 , -1):
            for n in freq[i]:  #check all num at this freq level
                res.append(n)
                if len(res) == k:
                    return res

        