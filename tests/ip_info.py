from z30lib import ip

print(ip.get_private_ip())                    # Get private IP
print(ip.get_public_ip())                     # Get public IP

ip.FormatTemplate.type_1("+", "Private IP", ip.get_private_ip)    # Format the Output as type_1: 

# There are existing the following types:
#        type_1: [<symbol>] <name>: <value>
#        type_2: (<symbol>) <name>: <value>
#        type_3: {<symbol>} <name>: <value>
#        type_4: <symbol> <name>: <value>