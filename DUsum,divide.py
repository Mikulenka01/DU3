from random import randint



def list_sort(nums):
    negative = []
    even = []
    odd = []
    positive = []
    for n in nums:
        if n < 0:
            negative.append(n)

        else:
            even.append(n)

        if n % 2 == 1:
            odd.append(n)

        else:
            positive.append(n)

    return odd, even, negative, positive


numbers = [randint(-10, 10) for _ in range(10)]

result = list_sort(numbers)
print(result)

o, e, n, p = list_sort(numbers)
_ = list_sort(numbers)
print(o)
print(e)
print(n)
print(p)
print(_)

nums = 0
for index in range(nums):
    if nums[index] < nums[s_n_index]:
        s_n_index = index

    if nums[index] > nums[l_n_index]:
        l_n_index = index

