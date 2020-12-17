import subprocess

# Get SITE_CODE and RANGE_START values from #fobs channel on slack.
SITE_CODE = <FIXME>
RANGE_START = <FIXME>
# How many fobs you're making in a batch.
COUNT = 50

SERIAL_DEV = "/dev/tty.usbmodem14201"

for fob in range(RANGE_START, RANGE_START+COUNT):
  input(f"Plase fob for {fob} on LF antenna and press a key.")
  cmd = f"lf hid write H10301 f {SITE_CODE} c {fob}"
  subprocess.call(["proxmark3", SERIAL_DEV, "-c", cmd])
