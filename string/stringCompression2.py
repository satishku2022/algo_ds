'''

question :

aaabbbcc a{3}b{3}c{2}


a{1,3}b{2,4}c --- aabbbbc aaabc

'''









'''
compress string using stack 
'''
def compressStack(input):
    stack = []
    '''
        1 read ch, if stack is not empty and top is not same 
        2 read ch, if stack is not empty and top is same 
        3 read ch, if stack is empty 
    '''
    print(input)
    output = []
    for ch in input:
        if stack and stack[-1]==ch:
            stack.append(ch)
        if stack and stack[-1]!=ch:
            count = 0
            while stack:
                currch = stack.pop()
                count+=1
            output.append(currch)
            if count > 1:
                output.append("{")
                output.append(str(count))
                output.append("}")
        if not stack:
            stack.append(ch)
    print(stack)
    count = 0
    while stack:
        currch = stack.pop()
        count += 1
    output.append(currch)
    if count > 1:
        output.append("{")
        output.append(str(count))
        output.append("}")

    return "".join(output)




'''
compress using 2 pointer 
'''
def compressIter(input):

    read = 0
    output = []
    length = len(input)
    while read < length:
        read_next = read + 1
        while read_next < length and input[read_next] == input[read]:
            read_next += 1
        output.append(input[read])
        if read_next-read > 1 :
            output.append("{")
            output.append(str(read_next-read))
            output.append("}")
        read = read_next
    return "".join(output)








'''
uncompress using rec
'''
def uncompressRec(input,output):
    if not input:
        return

    if len(input)==1:
        output.append(input[0])
        return
    else:
        ch = input[0]
        if input[1] == "{":
            index= input.index("}")
            val = int(input[2:index])
            for i in range(val):
                output.append(ch)
            return uncompressRec(input[index+1:],output)

        else:
            output.append(ch)
            return uncompressRec(input[1:],output)




def uncompressIter(input):
    length = len(input)
    


def compress_compare_string1(s, compS):

    # first compress then compare
    sc = compressIter(s)
    print(sc)
    return sc == compS

def compress_compare_string2(s, compS):

    # first compress then compare
    output = []
    uncompressRec(compS,output)
    print(output)
    return "".join(output)== s


def test_uncompress(compS):
    output = []
    uncompressRec(compS,output)
    print(output)


#print(compress_compare_string1("aaabbccc","a{3}b{2}c{3}"))

print(compress_compare_string2("aaabbccc","a{3}b{2}c{3}"))
print(compress_compare_string2("aaabbc","a{3}b{2}c"))