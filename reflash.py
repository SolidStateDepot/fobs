import subprocess

# SSD's default
SITE_CODE=142

while True:
    print("Reading...")
    out = subprocess.check_output(["pm3", "-c", "lf hid reader"])
    # Correct output contains:
    # [+] [H10301  ] HID H10301 26-bit                FC: 142  CN: 29136  parity ( ok )
    found_fc = out.find(b"FC: ")
    found_cn = out.find(b"CN: ")
    found_parity = out.find(b"parity")
    if found_fc == -1 or found_cn == -1 or found_parity == -1:
        print("Did not understand read result.")
        continue
    fc = int(out[found_fc+4:found_cn])
    cn = int(out[found_cn+4:found_parity])
    print(f"Read card: fc={fc} cn={cn}")
    if fc == SITE_CODE:
        print(f"Card {cn} already had correct site code...")
        continue
    print(f"Overwriting facility code for {cn}")
    out2 = subprocess.check_output(["pm3", "-c", f"lf hid clone -w H10301 --fc {SITE_CODE} --cn {cn}"])