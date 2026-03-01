from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], g: int) -> bool:
        n = len(hand)
        if n % g != 0:
            return False
        
        # sort the values
        # then compute their frequency into another array, whose length is unique_elements
        # then, start from the lowest. 
        # in each loop, we use the count_low of the lowest, and check the next consectutive "g-1"
        # have at least the same as the count_low.
        # We also reduce the frequecy of each of the following g-1 by count_low.
        # if any of them don't have count_low, return False
        # during this loop, the first element with frequency greater than count_low is set to next_lowest_index.
        # continue the same until next_lowest_index >= unique_elements.

        hand.sort()
        freq = [[hand[0], 1]]
        for i in range(1, n):
            if hand[i] == freq[-1][0]:
                freq[-1][1] += 1
            else:
                freq.append([hand[i], 1])
        
        # print(freq)
        uniq = len(freq)
        curr_lowest_index = 0
        while curr_lowest_index < uniq:
            lowest_element = freq[curr_lowest_index]
            count_low = lowest_element[1]
            low = lowest_element[0]
            next_lowest_index = curr_lowest_index + g
            # print(f"starting from {curr_lowest_index}: {freq[curr_lowest_index]}, next low = {next_lowest_index}")
            for i in range(1, g):
                j = curr_lowest_index + i
                # print(f"checking for {curr_lowest_index}: {j}")
                if j >= uniq or freq[j][0] != (low + i) or count_low > freq[j][1]:
                    # print(f"Falsifying: {count_low}, {freq[j][1]}")
                    return False
                
                # print(f"Truthifying: {count_low}, {freq[j][1]}")
                if next_lowest_index == (curr_lowest_index + g) and freq[j][1] > count_low:
                    next_lowest_index = j
                
                freq[j][1] -= count_low
                
            curr_lowest_index = next_lowest_index
        
        return True

if __name__ == "__main__":
    s = Solution()
    hand = [3, 4, 2, 5]
    g = 2
    print(s.isNStraightHand(hand, g))
