class Solution:
     def subarraySum(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        map[0] = 1
        print ('map is ',map)
        count, sum = 0, 0
        for num in nums:
            sum += num
            print ('sum is ',sum)
            count += map[sum - k]
            print ('count is ',count)
            map[sum] += 1
            print ('map is ',map)
        
        return count
