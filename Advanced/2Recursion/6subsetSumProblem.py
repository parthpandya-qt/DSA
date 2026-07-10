
def subsetSum(arr, sum, n):
    # If required sum is achieved
    if sum == 0:
        return 1

    # If no elements are left
    if n < 0:
        return 0

    include = subsetSum(arr, sum - arr[n], n - 1)
    exclude = subsetSum(arr, sum, n - 1)

    return include + exclude


#this code is calcualting the number of subsets which are giving the required sum 