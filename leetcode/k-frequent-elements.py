# simple solution
def topKFrequent(nums, k):
        freq = []
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for i in range(k):
            most_freq = max(count, key=count.get)
            freq.append(most_freq)
            count.pop(most_freq)

        return freq