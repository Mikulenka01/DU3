
from random import randint

nums1 = []
nums2 = [randint (-10, 10) for _ in range(10)]
for _ in range(10):
    nums1.append(randint(-10, 10))
    #print(f"nums1: {nums1}")

print(nums1)
print(nums2)

#task 1
nums3 = nums1 + nums2
print(nums3)

nums3_v2 = nums1.copy()
for n in range(len(nums2)):
    nums3_v2.append(n)

print(nums3_v2)
print(nums1)

print()

#task 2
nums4 = []
for n in nums3:
    if n not in nums4:
        nums4.append(n)

new_nums4 = sorted(nums4)
new_nums4.reverse()
print(new_nums4)


