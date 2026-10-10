class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        heap = []

        for key in freq:
            heapq.heappush(heap, (freq[key], key))

        largest = heapq.nlargest(k, heap)

        rv = []

        for v in largest:
            rv.append(v[1])

        return rv


