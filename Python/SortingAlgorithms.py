ls = [3, 1, 41, 59, 26, 53, 59]

def selection_sort(ls):
    length = len(ls)
    for i in range(length - 1):
        min_index = i

        for j in range(i + 1, length - 1):
            if ls[j] < ls[min_index]:
                min_index = j

        # Swap values
        prev_num = ls[i]
        ls[i] = ls[min_index]
        ls[min_index] = prev_num

    print(ls)

selection_sort(ls)
