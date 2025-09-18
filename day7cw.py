a=["milk", "bread", "eggs"]
def add_item(item):
    a.append(item)
    
add_item('porotta')    
# print(a)
def remove_last_item():
    a.pop()
remove_last_item()   
# print(a)
x=lambda item:print('item:',item)
for i in a:
    x(i)
def count_characters(items):
    
    if not items:
        return 0

    return len(items[0]) + count_characters(items[1:])

print("Total characters:", count_characters(a))    