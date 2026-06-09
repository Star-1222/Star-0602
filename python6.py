s = input().strip()
freq = {}
for ch in s:
    if ch.isalpha():  # 只统计字母
        freq[ch] = freq.get(ch, 0) + 1

if freq:   # 确保有字母
    max_count = max(freq.values())
    for ch in sorted(freq.keys()):
        if freq[ch] == max_count:
            print(ch, max_count)
