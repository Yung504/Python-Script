import subprocess


from pip._vendor.distlib.compat import raw_input


interface = raw_input("interface -> ")
new_mac = raw_input("new MAC address -> ")

print("Changing MAC address for : "+interface+" to -> "+new_mac)

#subprocess.call("Command to execute",shell = True)

subprocess.call("ifconfig",shell = True)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig",shell = True)