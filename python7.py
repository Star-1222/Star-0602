n = int(input())
nums = list(map(int, input().split()))
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

max_count = max(freq.values())
for num in sorted(freq.keys()):
    if freq[num] == max_count:
        print(num, max_count)
