# fobs

## Current Working Instructions
The registration computer in the corner of the woodshop is correctly setup with proxmark3 (iceman) and the reflash script from this repo.

To use the reflash script:
- Take the proxmark3 out of its box and connect to USB port on the computer
- Open a terminal with Ctrl+Alt+T
- Run `python3 reflash.py`

You should now see scrolling text of the reader attempting to read a fob. The lights on the reader should periodically flash red.

When you now place a fob over the reader it will read it (flash red) detect that it has an incorrect facility code and overwrite the facility code (flash green), then return to flashing red as it periodically reads the card and decides not to take action.

A bag of fobs can now be one-by-one passed over the reader until it flashes green. It takes ~3 seconds per fob.

## How to setup proxmark3 and the reflash.py script
I found much better luck using the "iceman" fork of proxmark from here: https://github.com/RfidResearchGroup/proxmark3

The registration computer is currently using their latest master commit as of writing this: 4ca3f2c

Follow the linux installation instructions and compiling instructions (in detail) from that repo's doc files.

After that the `python3 relfash.py` command should simply work.

## Some debugging tips
You should be able to run `pm3` from the terminal and get to the proxmark3 command line. It should automatically detect the proxmark3 if the firmware is correct.

You can check if the device is functioning properly with `hw tune` this command failed on one of the proxmarks we have due to some issue with the lf antenna.

`lf hid reader` can be used inside of pm3 to manually check a card.

## Legacy Instructions for older setup - DO NOT FOLLOW
Script for creating blank key fobs for SSD.

Instructions for use:

-Install the proxmark3 utility. For a mac, install brew and then use it to install proxmark3: 
https://github.com/Proxmark/homebrew-proxmark3
Linux instructions: https://github.com/Proxmark/proxmark3/wiki/Ubuntu-Linux

-Plug in the proxmark3 reader. Figure out which USB device it has.
On a mac, run ls /dev/tty.usbmodem*
On linux, run ls /dev/ttyUSB*

You should see a serial device like /dev/tty.usbmodem14201 or /dev/ttyUSB0

-Download the fobs.py script from this repo.

-Open the fobs.py script in a text editor of your choice. 
   Fill in this value for SERIAL_DEV in the fobs.py script.
   Fill in the SITE_CODE and RANGE_START values with the correct ones (these can be found on the #fobs slack channel)
   Fill in the COUNT variable with the number of fobs you want to program. Default is 50.
   
-Run the script (open a terminal, go to the same directory you put the script, and type 'python3 fobs.py')
-If everything went right, you should be prompted to place a fob on the low frequency antenna of the proxmark. Do this and press enter.
-Repeat for each fob in your batch to program.

-Update the fobs channel that you made a new batch of fobs and the batch number and size of the batch. The next time we run the script, the next seqence number will need to be the original sequence plus the batch size (so if the orig sequence is 100 and batch size is 50, the next time we program fobs, the sequence number should be 150).
