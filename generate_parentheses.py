def generateParenthesis(n):

    if n == 0: return []    
    result = []
    generateParenthesis_sub(n, n, "", result)
    return result

"""
According to the recursive method to generate well-performed parenthesis

l-> the rest of left bracket
r-> the rest of right bracket
item -> the current state of parenthesis
result-> append to the result list
"""
def generateParenthesis_sub(l, r, item, result):

    if r < l: return
    if l == 0 and r == 0: return result.append(item)
    if l > 0:
        generateParenthesis_sub(l - 1, r, item + '(', result)

    if r > 0:
        generateParenthesis_sub(l, r - 1, item + ')', result)

    
def main():

    s = 10
    result = generateParenthesis(s)
    print(result)
    

if __name__ == '__main__':
    main()