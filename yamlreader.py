import yaml

with open('r1.yml') as file:
    yaml_data = yaml.safe_load(file)

print(yaml_data)