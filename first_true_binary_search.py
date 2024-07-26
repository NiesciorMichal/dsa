from typing import List

def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2 #find the center of an array
        if arr[mid]: #if element is True
            boundary_index = mid #update the boundary index
            right = mid - 1 #discard everything to the right of index
        else:
            left = mid + 1 # if the element is False, discard everything to the left of index

    return boundary_index # return the boundary index or -1 if True wasn't find

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
