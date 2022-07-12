You will need the requests[secure] python module.

```buildoutcfg
pip install requests[secure]
```

You change the controller credentials either through environment variables or by editing the dnac_config.py file
## 00_port_capacity_util.py
This script will produce CSV providing port capacity for each swtich.
```buildoutcfg
./00_port_capacity_util.py

```
## 02_interface_device.py
This script shows all of the interfaces connected to a specific device.
```buildoutcfg

./02_interface_device.py 10.10.22.70

```

