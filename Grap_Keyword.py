import json

def get_keyword_value(json_file, keyword):
    with open(json_file, 'r') as f:
        data = json.load(f)
        if keyword in data:
            return data[keyword]
        else:
            return None

# Usage
json_file = 'your_file.json'  # replace with your json file
keyword = 'your_keyword'  # replace with your keyword
value = get_keyword_value(json_file, keyword)
print(f'The value of {keyword} is {value}')
