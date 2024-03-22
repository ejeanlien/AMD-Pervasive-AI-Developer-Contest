import json

def get_keyword_value_and_id(json_file, keyword):
    with open(json_file, 'r') as f:
        data = json.load(f)
        if keyword in data:
            return {'value': data[keyword], 'id': data.get('id', None)}
        else:
            return None

# Usage
json_file = 'your_file.json'  # replace with your json file
keyword = 'your_keyword'  # replace with your keyword
result = get_keyword_value_and_id(json_file, keyword)
print(f'The value of {keyword} is {result["value"]} and its related ID is {result["id"]}')

