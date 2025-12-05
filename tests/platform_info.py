from z30lib import platform

print(platform.FormatTemplate.type_1("/", "OS", platform.get_os_name))                           # Get the Name of your OS
print(platform.FormatTemplate.type_1("/", "CPU", platform.get_cpu_name))                         # Get the Name of your CPU
print(platform.FormatTemplate.type_1("/", "Network Device", platform.get_network_device_name))   # Get the Name of your Network Device

# There are existing the following types:
#        type_1: [<symbol>] <name>: <value>
#        type_2: (<symbol>) <name>: <value>
#        type_3: {<symbol>} <name>: <value>
#        type_4: <symbol> <name>: <value>