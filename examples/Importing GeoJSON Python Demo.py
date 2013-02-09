# TITLE: Importing GeoJSON Example in Python
# AUTHOR: Tom Schenk Jr., City of Chicago
# CREATED: 2013-01-23
# UPDATED: 2013-02-03
# NOTES: Quick example to import GeoJSON data in Python.
# MODULES: json

import json
pedway_json = open('PATH/TO/FILE/data/Pedway_Routes.json', 'r')
pedway_routes = json.load(json_data)
json_data.close()