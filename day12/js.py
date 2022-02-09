'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
Python has a built-in package called json, which can be used to work with JSON data.
'''
# Example:
import json

'''x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)  # Convert from JSON to Python(parsing)
print(y['name'])'''

people_j = '''
    {
    "people": [
        {
            "firstName": "Joe",
            "lastName": "Jackson",
            "gender": "male",
            "age": 28,
            "number": "7349282382"
        },
        {
            "firstName": "James",
            "lastName": "Smith",
            "gender": "male",
            "age": 32,
            "number": "5678568567"
        }
    ]
}'''
df = json.loads(people_j)  # Convert from JSON to Python(parsing)
#print(json.dumps(df, indent=3))  # use indent parameter to make it easy to read
# print(json.dumps(df, indent=4, separators=(". ", " = ")))
# print(json.dumps(df, indent=4, sort_keys=True))
# for i in df['people']:
#     print(i['firstName'])
#    del i['gender']

# print(i)

people_j2 = json.dumps(people_j, indent=5)  # Convert from python to JSON
json.dumps(people_j2)
print(people_j2)
