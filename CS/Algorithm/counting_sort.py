def count_sort_str(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(256)]
    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


def count_sort_int(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


if __name__ == '__main__':
    test_int = [5, 5, 5, 1, 1, 2, 3, 3, 3, 2, 1, 1, 2, 2, 2]
    test_str = 'ddcceeaagagagggagag'
    print(test_int, test_str)
    count_sort_int(test_int)
    answer = count_sort_str(test_str)
    print(test_int, ''.join(answer))