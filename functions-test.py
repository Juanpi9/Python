#!/usr/bin/env python3.6
def hello_world ():
    print("Hello world")

def print_name (name) :
    print(f"Name is {name}")

def number (num) :
    return num + 2

def add_two(num):
    return num + 2

hello_world ()
print_name("Peter")

result = add_two (3)
print(f"{result}")