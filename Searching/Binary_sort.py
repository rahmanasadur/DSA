def binary_search(list1,key):
    low = 0
    high = len(list1)-1
    Found = False
    while low<=high and not Found:
        mid = (low + high)//2
        if key == list1[mid]:
            Found = True
        elif key>list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("Key is found")
    else:
        print("key is not found")


list1 = [3,4,1,6,8,5]
print(list1)
list1.sort()
key = int(input("Enter the key"))
binary_search(list1,key)

