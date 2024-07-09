def shiftTable(Pattern,ST):
    m = len(Pattern)
    for i in range(128):
        ST[i]=m
    for i in range(m-1):
        index = ord(Pattern[i])-ord('0')
        ST[index]=m-1-i

def horspool(Pattern,str,ST):
    m=len(Pattern)
    n=len(str)
    i=m-1
    while(i<n):
        j=0
        while (j<m and Pattern[m-1-j] == str[i-j]):
            j+=1
        if(j==m):
            return (i-m+1)
        i=i+ST[ord(str[i])-ord('0')]
    return -1

def main():
    Pattern = "Example"
    Text = "here is an Example of horspool algorithm example"
    ST = [0] * 128  
    shiftTable(Pattern, ST)
    position = horspool(Pattern, Text, ST)
    if position != -1:
        print(f"Pattern found at position: {position}")
    else:
        print("Pattern not found in the text")

main()
        
            
    