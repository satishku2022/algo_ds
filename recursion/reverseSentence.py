from typing import List


def reverse_words(arr: List[str]) -> List[str]:
    output = []
    stack = []
    for i in range(len(arr)-1, -1, -1):


        if arr[i] == "  " and stack:
            print(stack)
            while stack:
                output.append(stack.pop())
            output.append(" ")
        else:
            stack.append(arr[i])

    print(stack)
    if stack:
        while stack:
            output.append(stack.pop())


    return output


# debug your code below
arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
       'm', 'a', 'k', 'e', 's', '  ',
       'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

print(reverse_words(arr))