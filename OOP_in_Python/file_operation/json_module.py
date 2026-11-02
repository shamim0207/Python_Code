import json
js_str='{"name":"shamim","Subject":"AI/ML","isStudent":true}'

py_obj=json.loads(js_str)

print(py_obj)

#================================================================================

with open("code.json","r") as f:
    py_object=json.load(f)
    print(py_object)