def nextGreaterElement(arr):
    n = len(arr)
    result1 = [-1] * n  # Initialize result array with -1
    result2=[-1]*n
    stack1 = [] # Stack to store potential NGE candidates
    stack2=[]
    for i in range(n - 1, -1, -1):
        while stack1 and stack1[-1] <= arr[i]:
            stack1.pop()

        if stack1:
            result1[i] = stack1[-1]
        stack1.append(arr[i])
    for i in range(n):
        while stack2 and stack2[-1] <= arr[i]:
            stack2.pop()
        if stack2:
            result2[i]=stack2[-1]
        stack2.append(arr[i])

    return (result1,result2)

arr = [4, 5, 2, 25, 7, 8, 6]
print("Next Greater Element:", nextGreaterElement(arr))
