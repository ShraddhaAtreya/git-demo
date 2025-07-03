# check_multiple.py

# Hardcoded test values
number = 9
divisor = 3  # Change this to 4 to simulate a failed case

print(f"Checking if {number} is a multiple of {divisor}...")

if number % divisor == 0:
    print(f"{number} is a multiple of {divisor}. Test Passed.")
    exit(0)  # Jenkins marks this build as SUCCESS
else:
    print(f"{number} is NOT a multiple of {divisor}.  Test Failed.")
    exit(1)  # Jenkins marks this build as FAILURE
