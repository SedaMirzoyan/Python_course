import json
from types import SimpleNamespace

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def main():
    #convert dictionary to json data
    input_dict = { "name": "Bob", "mark": 56, "city": "Lisbon"}

    to_json = json.dumps(input_dict)
    print(to_json)
    print(type(to_json))

    #convert class object to json
    obj1 = A(5, 6)
    obj2 = A(3, 4)

    json_obj1 = json.dumps(obj1.__dict__) 
    json_obj2 = json.dumps(obj2.__dict__) 
    print(json_obj1, type(json_obj1))
    print(json_obj2, type(json_obj2))


    #convert json data into a custom python object
    test_dict = """{ "name": "Bob", "mark": 56, "city": "Lisbon"}"""

    to_obj = json.loads(test_dict)
    print(type(to_obj))


if __name__=="__main__":
    main()