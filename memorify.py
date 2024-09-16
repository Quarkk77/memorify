#!/usr/bin/env python3
import json
import sys
import os

# File to store the names
json_file = os.path.expanduser("~/.memorify_list.json")

# Initialize the list if the file doesn't exist
if not os.path.exists(json_file):
    with open(json_file, 'w') as f:
        json.dump([], f)

def load_names():
    """Load names from the JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)

def save_names(names):
    """Save names to the JSON file."""
    with open(json_file, 'w') as f:
        json.dump(names, f, indent=2)

def echo_names():
    """Print names with their corresponding numbers."""
    names = load_names()
    if names:
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
    else:
        print("No names in the list.")

def add_name(name):
    """Add a name to the list."""
    names = load_names()
    names.append(name)
    save_names(names)
    print(f"Added: {name}")

def delete_name(number):
    """Delete a name by its number."""
    names = load_names()
    if 1 <= number <= len(names):
        removed = names.pop(number - 1)
        save_names(names)
        print(f"Deleted: {removed}")
    else:
        print("Invalid number.")

def show_help():
    """Show help instructions."""
    print("Usage:")
    print("  memorify                  - Echo names in the list.")
    print("  memorify add <name>       - Add a name to the list.")
    print("  memorify delete <number>  - Delete a name by its number.")
    print("  memorify help             - Show this help message.")

def main():
    if len(sys.argv) == 1:
        echo_names()
    elif sys.argv[1] == "add" and len(sys.argv) == 3:
        add_name(sys.argv[2])
    elif sys.argv[1] == "delete" and len(sys.argv) == 3 and sys.argv[2].isdigit():
        delete_name(int(sys.argv[2]))
    else:
        show_help()

if __name__ == "__main__":
    main()
