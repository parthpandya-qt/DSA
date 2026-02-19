def findpatter(string,pattern):
    pos=string.find(pattern)
    while pos>=0:
        print(pos)
        pos=string.find(pattern,pos+1)
        