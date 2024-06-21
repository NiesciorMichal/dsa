def merge_sort(array):
    if len(array) <= 1:
        return array

    def merge(left, right):
        merged_array = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged_array.append(left[left_index])
                left_index += 1
            else:
                merged_array.append(right[right_index])
                right_index += 1

        merged_array.extend(left[left_index:])
        merged_array.extend(right[right_index:])

        return merged_array

    middle_point = len(array) // 2
    left_part = merge_sort(array[:middle_point])
    right_part = merge_sort(array[middle_point:])

    return merge(left_part, right_part)

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:', numbers)
    sorted_numbers = merge_sort(numbers)
    print('Sorted array: ', str(sorted_numbers))