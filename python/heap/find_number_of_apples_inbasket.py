"""
1196. How Many Apples Can You Put into the Basket
Easy

96

11

Add to List

Share
You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.

Return the maximum number of apples you can put in the basket.

 

Example 1:

Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.
Example 2:

Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.
 

Constraints:

1 <= arr.length <= 10^3
1 <= arr[i] <= 10^3
"""
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        # note that build a heap only requires O(N)
        # more details: https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        heapq.heapify(arr)
        apples = units = 0

        # note that arr[0] always represents the smallest
        # element in the min-heap
        while arr and units + arr[0] <= 5000:
            units += heapq.heappop(arr)
            apples += 1
        return apples

"""
We can transform the input array arr into a min-heap; we then keep popping the first element from it, which is the lightest apple due to min-heap's nature.

Algorithm

Transform arr into a min-heap, and initialize two integer variables: apples to count the number of apples we have put in the basket and units to record the current weight of the basket.
Before units reaches 5000 and while there are remaining elements in the min-heap:
increment apples by 1;
increment units by the popped element from the min-h

"""
