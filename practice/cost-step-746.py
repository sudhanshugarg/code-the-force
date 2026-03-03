class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one_up = two_up = 0
        # start from n-1th floor
        # pay cost for 1 step
        # for n-3th floor
        # either pay dp[i] = min(cost[i] + dp[i+1], cost[i] + dp[i+2]), whichever is lower
        for i in range(n-1, -1, -1):
            one_up_cost = cost[i] + one_up
            two_up_cost = cost[i] + two_up

            two_up = one_up
            one_up = min(one_up_cost, two_up_cost)
        
        return min(one_up, two_up)
