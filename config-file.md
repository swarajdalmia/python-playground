# Config Files

- Writing data to json file 
```
import json

config = {'key1': 'value1', 'key2': 'value2'}

with open('config.json', 'w') as f:
    json.dump(config, f)
```


- Reading data from json

```
import json

with open('config.json', 'r') as f:
    config = json.load(f)

#edit the data
config['key3'] = 'value3'

#write it back to the file
with open('config.json', 'w') as f:
    json.dump(config, f)
```


For other file types, look [here](https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file)
