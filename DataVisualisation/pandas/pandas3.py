import pandas
import json

b= pandas.read_json('sample4.json')

print(b.to_string())