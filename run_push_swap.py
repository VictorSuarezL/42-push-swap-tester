#!/usr/bin/env python3

import subprocess
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to generate a list of 6 random numbers
def generate_random_numbers(n):
    return random.sample(range(1, 5*n), n)

def save_arg_to_file(ARG, filename):
    with open(filename, 'a') as f:
        f.write(' '.join(map(str, ARG)) + '\n')

# Usage:
# save_arg_to_file(ARG, 'arg.txt')

batch = 10
number_to_test = [5, 100, 500]
# Run the commands 10 times with different numbers
for n in number_to_test:
    max = -1
    print(f"{bcolors.WARNING}*Checking n = {n}:{bcolors.ENDC}", end = ' ')
    for i in range(batch):
        ARG = generate_random_numbers(n)
        command = ['./push_swap'] + list(map(str, ARG))
        result = subprocess.run(command, stdout=subprocess.PIPE)
        lines = result.stdout.decode('utf-8').count('\n')
        if(lines > max):
            max = lines
            max_numbers = ARG
            check = 0
        if(lines > 5500 and n == 500):
            print(f"\t{bcolors.OKBLUE}max exceeded with: {max} for {n} numbers{bcolors.ENDC}")
            save_arg_to_file(ARG, 'arg.txt')
        command = ['./push_swap'] + list(map(str, ARG))
        checker_command = ['./checker_MAC'] + list(map(str, ARG))
        push_swap_process = subprocess.Popen(command, stdout=subprocess.PIPE)
        checker_process = subprocess.Popen(checker_command, stdin=push_swap_process.stdout, stdout=subprocess.PIPE)
        push_swap_process.stdout.close()  # Allow checker_process to receive a SIGPIPE if push_swap_process exits.
        output = checker_process.communicate()[0].decode('utf-8').strip()
        if output == "KO":
            print(f"{bcolors.FAIL}KO{bcolors.ENDC}")
            print(f"\t{bcolors.FAIL}--> Running with ARG = {ARG}{bcolors.ENDC}")
            exit(1)
        elif output != "OK":
            print(f"{bcolors.FAIL}Error{bcolors.ENDC}")  # prints "Error" in red
            # print("Running with ARG =", ARG)
            exit(1)
        elif(max > 12 and n == 5) or (max > 1500 and n == 100) or (max > 11500 and n == 500):
            print(f"\t{bcolors.FAIL}--> Running with ARG = {ARG}{bcolors.ENDC}")
            print(f"\033[0;31mMAX =  {lines} for {n} numbers!\033[0m")
            exit(1)
    if output == "OK":
        print(f"\t{bcolors.OKGREEN}OK{bcolors.ENDC} max_movements = {bcolors.OKGREEN}{max}{bcolors.ENDC}")
        if (i == (batch - 1) and n == 100 and max <= 700) or (i == (batch - 1) and n == 500 and max <= 5500):
            print(f"\t{bcolors.OKCYAN}+5 pts{bcolors.ENDC}")
        elif n == 5:
            print(f"\t{bcolors.OKCYAN}OK{bcolors.ENDC}")
        else:
            # print(f"\t{bcolors.OKBLUE}max exceeded with: {max} for {n} numbers{bcolors.ENDC}")
            print(f"\t{bcolors.OKBLUE}Writting arg.txt file...{bcolors.ENDC}")
            # save_arg_to_file(max_numbers, 'arg.txt')

