import json

with open('school.json', 'r') as dip:
    data = json.load(dip)
for classes in data["classes"]:
    if classes['class_1'] > ['class_2']:
        print(classes['students'])