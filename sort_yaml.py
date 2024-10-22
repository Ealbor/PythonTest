import yaml
from ipaddress import ip_address

# Load the YAML file
with open('dns_to_ip.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Sort the dictionary by the IP address
# key=lambda item: ip_address(item[1]) sorts by the IP value (the second element in each item)
sorted_data = dict(sorted(data.items(), key=lambda item: ip_address(item[1])))

# Write the sorted data back to the YAML file
with open('dns_to_ip.yaml', 'w') as file:
    yaml.dump(sorted_data, file, default_flow_style=False)
