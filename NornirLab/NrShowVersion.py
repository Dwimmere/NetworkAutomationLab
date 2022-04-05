# Nornir script using Netmiko to run show version command"

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.plugins.inventory.simple import SimpleInventory
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_netmiko.tasks import netmiko_send_command

if __name__ == "__main__":
    InventoryPluginRegister.register("SimpleInventory", SimpleInventory)

    nr = InitNornir(
        runner={
            "plugin": "threaded",
            "options": {
                "num_workers": 30,
            },
        },
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                    "host_file": "/inventory/hosts.yaml",
                    "group_file": "/inventory/groups.yaml",
                    "defaults_file": "/inventory/defaults.yaml"
                },
            }
    )

result = nr.run(netmiko_send_command, command_string="show version")

shVerOutput = open('shVerOutput.txt', 'w')
shVerOutput.append(result)

print_result(result)





