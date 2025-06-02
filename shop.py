def previousGreaterElement(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result array with -1
    stack = []  # Stack to store potential PGE candidates

    # Traverse the array from left to right
    for i in range(n):
        # Maintain stack as decreasing, pop smaller elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, the top of the stack is the PGE
        if stack:
            result[i] = stack[-1]

        # Push the current element to the stack
        stack.append(arr[i])

    return result


# Example usage
arr = [4, 5, 2, 25, 7, 8, 6]
print("Previous Greater Element:", previousGreaterElement(arr))
