# A program that reads in a text file and outputs the number of e's it contains
# Author: Tihana Gray

import sys
import os

def count_es(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        return text.count('e')  # Only lowercase 'e'

def main():
    if len(sys.argv) < 2:
        sys.exit("Error: No filename provided.\nUsage: python es.py <filename>")

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        sys.exit(f"Error: File '{filename}' does not exist.")

    if not filename.endswith(".txt"):
        sys.exit("Error: Only .txt files are supported.")

    try:
        print(count_es(filename))  # Prints only the count
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()