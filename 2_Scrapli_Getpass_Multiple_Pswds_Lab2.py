from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
import getpass

"""
This Script will configure get userpassword for north region devices, south region devices
& one Device vIOS-R7 which has diffrent password using through Getpass module and will
embend password into groups & hosts inventory file accordingly. We dont have not hard coded pasword key in default file 

as per topology north region devices are managed through northadmin & south region devices managed through southadmin
Please make sure devices are configured with username and password as per region
"""
nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Getpass_Cisco_Lab3/Inventory/config.yaml")

# Input Password for north region devices
north_region_pswd = getpass.getpass (prompt='Enter Password for North Region Devices: ')
# Embend passsword into password key in groups fle.
nr.inventory.groups['north'].password = north_region_pswd

# Input Password for south region devices
south_region_pswd = getpass.getpass (prompt='Enter Password for South Region Devices: ')
# Embend passsword into password key in groups fle.
nr.inventory.groups['south'].password = south_region_pswd

# Input Password for vIOs_R7 device
vIOS_R7_pswd = getpass.getpass (prompt='Enter Password for vIOs_R7 Device: ')
# Embend passsword into password key in hosts file.
nr.inventory.hosts['vIOS-R7'].password = vIOS_R7_pswd


# will send show command to devices using dynamic passsword provided 
def send_show_command (task):
    task.run (task=send_command, command="show ip int brie")

send_show_command_results = nr.run (task=send_show_command)
print_result (send_show_command_results)


