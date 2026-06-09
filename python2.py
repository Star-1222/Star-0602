def get_numbers():
    numbers = []
    while True:
        line = input("Enter a number (<Enter> to quit):")
        if line == "":
            break
        numbers.append(float(line))
    return numbers

def mean(nums):
    return sum(nums) / len(nums) if nums else 0.0

def median(nums):
    if not nums:
        return 0.0
    s = sorted(nums)
    n = len(s)
    return (s[n//2] if n%2 else (s[n//2-1]+s[n//2])/2)

data = get_numbers()
if data:
    print(f"The mean is {mean(data):.6f}")
    print(f"The median is {median(data):.6f}")
