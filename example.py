from collections import Counter

def secondmostfreq(arr):
    freq=Counter(arr)
    sortedfreq=sorted(freq.items(),key=lambda x :x[1],reverse=True)
    return sortedfreq[1][0]
def secondlargest(arr):
    second=float('-inf')
    first=float('-inf')
    for num in arr:
        if num > first:
            second=first
            first=num
        # elif num > second and num !=first:
        #     second=num
    return second if second !=float('-inf') else "None"




arr=[ 40,50,30,40,50,30,30]
print(secondmostfreq(arr))
print(secondlargest(arr))
