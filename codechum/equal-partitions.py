# Given an array of integers, determine how many ways it can be partitioned into two nonempty parts such that the sum of all elements on the left side is equal to the bitwise XOR of all elements on the right side. A partition divides the array between any two consecutive indices, keeping the original order of elements intact. For each possible split, calculate the sum of the left subarray and the XOR of the right subarray, then count how many partitions satisfy the equality condition.

# e.g.
# 2 1 3 0 6 0

# There are two partitions:
# 2+1+3 = 0^6^0
# 2+1+3+0 = 6^0


from functools import reduce

size = input("Enter size: ")
print("Enter elements: ")
arr = [int(num) for num in input().split()]

count = 0
for i in range(1, len(arr)):
    left = arr[0:i]
    right = arr[i:len(arr)]
    leftsum = sum(left)
    rightxor = reduce(lambda x, y: x ^ y, right)
    if leftsum == rightxor:
        count += 1

print(f"Number of partitions: {count}")