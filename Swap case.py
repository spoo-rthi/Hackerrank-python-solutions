# Method 1

def swap_case(s):
    case_change=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            case_change.append(s[i].lower())
        elif (s[i].islower()==True):
            case_change.append(s[i].upper())
        else:
            case_change.append(s[i])    
        stri=''
    return stri.join(case_change)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
 # Method 2
    
def swap_case(s):
    i=0
    a=list(s)
    for x in a:
        if(x.isupper()):
           a[i]=x.lower()
        else:
            a[i]=x.upper()
        i+=1
    s=''.join(a)
        
    return s;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
