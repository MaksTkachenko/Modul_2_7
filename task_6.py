# Задача 6. Підрахунок глибини вкладених списків

def depth(n):
    if not isinstance(n, list):
        return 0
    elif not n:
        return 1
    else:
        max_depth = 0
        for i in n:
            sub_depth = depth(i)
            max_depth = max(max_depth, sub_depth)
        return 1 + max_depth


print(depth([1, [2, [3, [4, [5]]]]]))  # 5
