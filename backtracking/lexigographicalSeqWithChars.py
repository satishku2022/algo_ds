
'''

Given a non-negative integer n, find all n-letter words composed by 'a' and 'b',
return them in a list of strings in lexicographical order.


function dfs(start_index, path):
  if is_leaf(start_index):
    report(path)
    return
  for edge in get_edges(start_index):
    path.add(edge)
    dfs(start_index + 1, path)
    path.pop()

'''

#SOLUTION 1
def generate_all_lex_seq_backtrack(start_index , path):
    if start_index == 2:
        output.append("".join(path))
        return

    for ch in alphabets:
        path.append(ch)
        generate_all_lex_seq_backtrack(start_index+1,path)
        path.pop()



#SOLUTION 2
'''
Start with "" -> a b 

'''

def gen_all_lex_iter(output, iternum ):
    iter_num = 0
    while iter_num < iternum:
        print(output)
        if output:
            count = len(output)
            tmp = []
            for s in output:
                for ch in alphabets:
                    cand = s + ch
                    tmp.append(cand)
            output = tmp

        else:
            for ch in alphabets:
                output.append(ch)

        iter_num += 1
    print(output)



alphabets =["a","b","c"]
output = []
gen_all_lex_iter(output, len(alphabets))

'''
path = []
output = []
generate_all_lex_seq_backtrack(0, path)
print(output)
'''