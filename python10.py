import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:1+n]))
    nums.sort()
    print(' '.join(map(str, nums)))

if __name__ == '__main__':
    main()
