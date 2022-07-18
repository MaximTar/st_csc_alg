# даны число 1≤n≤10**2 ступенек лестницы и целые числа -10**4≤a_1,…,a_n≤10**4, которыми помечены ступеньки
# найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх
# от нулевой до n-й ступеньки, каждый раз поднимаясь на одну или две ступеньки


# TODO generalize with k=2
def ladder_sum(nums, n):
    previous, current = 0, nums[0]

    for i in range(1, n):
        previous, current = current, max(nums[i] + previous, nums[i] + current)

    return current


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(ladder_sum(nums, n))


if __name__ == '__main__':
    main()
