from bisect import bisect_left, bisect_right


def bin_search(target, lst):
    left = 0
    right = len(lst) - 1
    p = -1

    while right >= left:
        p = (right + left) // 2
        if target < lst[p]:
            right = p - 1
        elif target > lst[p]:
            left = p + 1
        else:
            return p

    # targetのインデックス（なければ-1）
    return p


def bin_search_left(target, lst):
    left = 0
    right = len(lst) - 1
    result = -1

    while right >= left:
        p = (right + left) // 2
        if target < lst[p]:
            right = p - 1
        elif target > lst[p]:
            result = p
            left = p + 1
        else:
            return p

    # targetより小さい要素の最大インデックス（最大より大きければ-1）
    return result


def bin_search_right(target, lst):
    left = 0
    right = len(lst) - 1
    result = -1

    while right >= left:
        p = (right + left) // 2
        if target < lst[p]:
            result = p
            right = p - 1
        elif target > lst[p]:
            left = p + 1
        else:
            return p

    # targetより大きい要素の最小インデックス（最小より小さければ-1）
    return result


if __name__ == "__main__":
    lst = [0, 2, 4, 4, 5]

    print(lst)
    for i in [-1, 3, 4, 5, 6]:
        p = bin_search(i, lst)
        p_left = bin_search_left(i, lst)
        p_right = bin_search_right(i, lst)
        p_bl = bisect_left(lst, i)
        p_br = bisect_right(lst, i)
        print(
            f"bin_search_right: {i} => {p}, left:{p_left}, right: {p_right}, b_left:{p_bl}, b_right:{p_br}",
            end="\n\n",
        )
