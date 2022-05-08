#Mock CCC '18 Contest 2 J1

def StringExpressionVerify():
    temp = input()
    arr = temp.split(' ')
    if(eval(''.join(arr[:3])) == int(arr[4])):
        return True
    return False

StringExpressionVerify()
