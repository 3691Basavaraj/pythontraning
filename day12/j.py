import json
with open('/home/basavaraj/Desktop/Tibil/simple.json') as file:
    data = json.load(file)
    print(type(data))




'''
|                 Python                 |  JSON  |
|:--------------------------------------:|:------:|
|                  dict                  | object |
|               list, tuple              |  array |
|                   str                  | string |
| int, float, int- & float-derived Enums | number |
|                  True                  |  true  |
|                  False                 |  false |
|                  None                  |  null  |

'''