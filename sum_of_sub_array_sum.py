def get_prefix_sum(num_array: list) -> list:
    prefix_sum = [num_array[0]]
    for index in range(1, len(num_array)):
        prefix_sum.append(prefix_sum[index - 1] + num_array[index])
    return prefix_sum


def get_sub_array_sum(num_array: list) -> int:
    prefix_sum = get_prefix_sum(num_array)
    sub_array_sum = 0
    for index1 in range(len(num_array)):
        for index2 in range(index1, len(num_array)):
            if index1 == 0:
                sub_array_sum += prefix_sum[index2]
            else:
                sub_array_sum += prefix_sum[index2] - prefix_sum[index1 - 1]
    return sub_array_sum


try:
    nums_array = list(map(int, input("Enter Integers separated by space : ").split()))
    print("The sum of sub arrays of given array is : ", get_sub_array_sum(nums_array))
except ValueError:
    print("Invalid input. Please enter integers only")
