import sys

tries = 0
for line in sys.stdin:
    if not line.strip():
        continue
    tries += 1
    if int(line.strip()) == 4:
        print(f"Correct in {tries} tries")
        break