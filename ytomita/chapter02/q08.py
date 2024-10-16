for nums in range(2,101):
    i = True
    for x in range(2,nums):
        if (nums%x)== 0:
            i = False
            break
    if i:
        print(nums)