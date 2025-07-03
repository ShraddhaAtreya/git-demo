# check_multiple.py

number = 9
divisor = 3

if number % divisor == 0:
    print(f"{number} is a multiple of {divisor}. Test passed.")
    exit(0)
else:
    print(f"{number} is NOT a multiple of {divisor}. Test failed.")
    exit(1)
