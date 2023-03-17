# somar duas listas

from itertools import zip_longest

nums1 = [1, 2, 3, 4, 5, 50, 55, 60]
nums2 = [11, 30, 40, 45]


# somar valores com o zip
sum_w_zip = [x + y for x, y in zip(nums1, nums2)]

# somar valores com zip_longest
sum_all_nums = [x + y for x, y in zip_longest(nums1, nums2, fillvalue=0)]

# mostrar na tela
print(sum_w_zip)
print(sum_all_nums)
