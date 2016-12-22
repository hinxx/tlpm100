# Thorlabs power meter PM100USB

More info at https://www.thorlabs.com/thorproduct.cfm?partnumber=PM100USB.

# Prerequisites

Before IOC can be started the _/dev/bus/usb/xxx/yyy_ needs to have proper permissions; for this the udev rules file _88-thorlabs-pm100.rules_ can be copied to the _/etc/udev/rules.d_ folder.

# Usage

Check the PM100USB-Manual.pdf_ chapter 6.3 for details about the commands.

Here is a list of all PVs (by default $(P) macro is set to 'PM100'):

| PV | Description |
| ------------- :| ----- :|
| PM100:IDN | Identification string with model number and firmware version |
| PM100:asyn | asynDriver specific PV |


Check if the device is present:

    caget -S PM100:IDN
    PM100:IDN Thorlabs,PM100USB,P2003113,1.3.2

# Misc

When connected via USB a _/dev/bus/usb/xxx/yyy_ device node is created:

	[246991.193167] usb 4-1: new full-speed USB device number 9 using xhci_hcd
	[246996.322149] usb 4-1: New USB device found, idVendor=1313, idProduct=8072
	[246996.322152] usb 4-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
	[246996.322154] usb 4-1: Product: PM100USB
	[246996.322156] usb 4-1: Manufacturer: Thorlabs
	[246996.322157] usb 4-1: SerialNumber: P2003113

