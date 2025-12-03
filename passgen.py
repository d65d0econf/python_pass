#!/usr/bin/env python3
import argparse
import random
import string
#cool CLI flags, all flags are false unless used, then TRUE
parser = argparse.ArgumentParser(description="Quick password generator")
parser.add_argument("-l", "--length", type=int, default=12, help="length of the password")
parser.add_argument("-u", "--no-uppercase", action="store_true", help="removes uppercase letters")
parser.add_argument("-n", "--no-numbers", action="store_true", help="removes numbers")
parser.add_argument("-s", "--no-symbols", action="store_true", help="removes special characters")
args = parser.parse_args()
#now the actual password making
pool = string.ascii_lowercase
if not args.no_uppercase:
    pool += string.ascii_uppercase
if not args.no_numbers:
    pool += string.digits
if not args.no_symbols:
    pool += string.punctuation
#generate
password = ''.join(random.choice(pool) for _ in range(args.length))

print(password)