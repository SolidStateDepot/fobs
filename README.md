# fobs
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
