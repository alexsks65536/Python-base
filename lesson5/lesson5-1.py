def nums_gen(n):
    for num in range(1, n + 1, 2):
        yield num

print(*nums_gen(100), sep=" ")

############ Второй способ ###################

nums_gen = (nums_gen for nums_gen in range(1, 100 +1, 2))

print(*nums_gen, sep=" ")