import yaml
from ipaddress import ip_address

# Load the YAML file
with open('dns_to_ip.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Sort by IP address
sorted_data = dict(sorted(data.items(), key=lambda item: ip_address(item[1])))

# Write the sorted data back to the YAML file
with open('dns_to_ip.yaml', 'w') as file:
    yaml.dump(sorted_data, file, default_flow_style=False)
