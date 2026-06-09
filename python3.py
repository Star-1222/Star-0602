n = int(input("How  many numbers are there? "))
max_val = None
for i in range(n):
    val = int(input("Enter  a  number  >> "))
    if max_val is None or val > max_val:
        max_val = val
print(f"The  largest  value  is {max_val}")
