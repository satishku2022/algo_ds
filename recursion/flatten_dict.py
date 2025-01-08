
from typing import Dict, Union

DeepNestedDict = Dict[str, Union[str, 'DeepNestedDict']]

def flatten_dictionary_sv(dictionary: DeepNestedDict) -> Dict[str, str]:

    def flatten_dictionary_helper(initial_key, dictionary, flat_dictionary):
        for key in dictionary:
            value = dictionary[key]
            if initial_key and key:
                new_key = "{}.{}".format(initial_key, key)
            elif initial_key:
                new_key = initial_key
            else:
                new_key = key

            if isinstance(value, dict):
                flatten_dictionary_helper(new_key, value, flat_dictionary)
            else:
                flat_dictionary[new_key] = value



    flat_dictionary = {}
    flatten_dictionary_helper("", dictionary, flat_dictionary)
    return flat_dictionary



def flatten_dictionary(dictionary):
    def flatten_dictionary_helper(initial_key, dictionary, flat_dictionary):
        for key in dictionary:
            value = dictionary[key]

            if initial_key and key:
                new_key = "{}.{}".format(initial_key, key)
            elif initial_key:
                new_key = initial_key
            else:
                new_key = key

            if isinstance(value, dict):
                flatten_dictionary_helper(new_key, value, flat_dictionary)
            else:
                flat_dictionary[new_key] = value

    flat_dictionary = {}
    flatten_dictionary_helper("", dictionary, flat_dictionary)
    return flat_dictionary

'''
 { a:1 , b:{c:2}}
  a 1 
  b.c 2 
'''

# debug your code below
dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

print(flatten_dictionary_sv(dict_input))




'''
Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it. Assume that values are either an integer, a string, or another dictionary.

If a certain key is empty, it should be excluded from the output (see e in the example below).

Example

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
'''