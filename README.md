powerfail
=========

Power failure detection and orderly shutdown via Raspberry Pi.

![alt text][circuit]

I have a cheap UPS that lacks communication so it can't really shut things down in the event of a power outage.  The idea is to detect when it happens, then properly shut things down.  Right now I have a PC, NAS storage, and Raspberry Pi hooked up and I'd like to shut them down properly in the event of a power failure.

My UPS is an APC 450VA model (cost about $50).  Many (most) have a relay inside that switches to battery power in the event of a power failure.  The one I have inside is a 12V relay.  There is a constant 12V across the coil of the relay when it is running on wall power.  Once power fails, the voltage goes to 0 and trips the relay and uses battery power.  This means the transistor on the opto will open up and not conduct (causing GPIO to go high).

I wrote a C program that calls a shutdown script once a power failure has been detected.  This is done by checking the GPIO port I set up for a high value.  If it is high for more than 10 seconds, it will initiate a shutdown of my devices.  It will also log the event, and send me a text with `sendpf.py`.

My +12V was reading 11.5V or so and I used to have only a 0.5k resistor, but it brought the voltage down to 10.5V and was drawing 25mA.  I upped it to a 1.5k resistor and now it draws less than 5mA.  You don't need much on these optos, so it's best to draw as little current as possible to not interfere with the UPS.

This was done using a Gertboard, by Gert van Loo.  It's an expansion board for the Raspberry Pi.  My C program is based off his many example programs found at **[here][1]** where his Makefile and .c/.h files can be downloaded.

The shutdown script `powerfail.sh` uses sshpass in order to ssh without a password prompt and initiate shutdown commands.

[circuit]: http://brontopixel.com/images/2013/08/12/ups.png "UPS Power Failure Detection Circuit"
[1]: http://www.raspberrypi.org/phpBB3/viewtopic.php?f=42&t=20410
