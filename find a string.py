def count_substring(string, sub_string):
    a=len(string)
    b=len(sub_string)
    c=0
    for i in range(a-b+1):
        for j in range(b):
            if string[i+j]!=sub_string[j]:
                break
            if (j==b-1):
                c+=1

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
