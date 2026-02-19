def count_frequency(arr):
    hmap={}
    for num in arr:
        if num in hmap:
            hmap[num]+=1
        else:
            hmap[num]=1
    return hmap

arr=[2,2,2,5,5,5,1,1,1,6,6,6,8,8,8,8]
result=count_frequency(arr)

for i,value in result.items():
    print(f"{i} : {value}")

