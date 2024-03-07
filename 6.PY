L1=[1,2,2,3,3,4,5]
Element_Count={}

for Element in L1:
    if Element in Element_Count:
        Element_Count[Element]+=1
    
    else:
        Element_Count[Element]=1

for Element,count in Element_Count.items():
    print(f"The count of {Element} is : {count}")