def read_set(set_name):
    n= int(input(f"Enter the number of elemnts of the set of {set_name}:"))
    elements=set()
    print(f"Enter the elements of {set_name}:")
    for _ in range(n):
        elements.add(int(input()))

    return elements
setA=read_set("SET A")
setB=read_set("SET B")
union=setA|setB
intersection=setA&setB
sub=setA-setB
print("The result of union between the 2 given set:",union)
print("The result of intersection between the 2 given set:",intersection)
print("The result of subtraction between the 2 given set:",sub)