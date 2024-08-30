# Write a python program to convert two lists into a dictionary.

def list_to_dict():
    Name_list1 = ['Darshan', 'Vinayak', 'Dhoran']
    Phone_list2 = [111,222,333]
    result = dict(zip(Name_list1,Phone_list2))
    print("Your dict := ",result)
list_to_dict()


# Now convert this dict to tuple

def dict_to_tuple():
    x = {'Darshan': 111, 'Vinayak': 222, 'Dhoran': 333}
    print("Your tuple is:=")
    for i in x.items():
        print(i)
dict_to_tuple()        
