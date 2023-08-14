def search(list1, key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("Element is found at index:",i)
            break
    
    else:
        print("Element is not found:")

list1 = [2,3,5,1,6,7]
key = int(input("Enter the key element:"))
search(list1,key)
