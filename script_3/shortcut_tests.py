#!/usr/bin/python3

import os

import pathlib

DESKTOP = pathlib.Path.home().__str__() + "/Desktop/"

def main():
    try:
        print(os.path.exists(DESKTOP + "system_report.py"))
    except:
        print("did not work")

if __name__ == '__main__':
    main()