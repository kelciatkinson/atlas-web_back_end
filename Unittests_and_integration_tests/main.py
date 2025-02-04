#!/usr/bin/env python3
"""Main file to demonstrate access_nested_map function"""
import utils

access_nested_map = utils.access_nested_map

def main():
    # Example 1: Simple nested dictionary
    nested_map = {"a": {"b": {"c": 1}}}
    path = ["a", "b", "c"]
    
    try:
        result = access_nested_map(nested_map, path)
        print(f"Example 1 - Path {path}:")
        print(f"Result: {result}\n")  # Should print 1
    except KeyError as e:
        print(f"Error: Key {e} not found\n")

    # Example 2: More complex nested dictionary
    nested_map2 = {
        "level1": {
            "level2": {
                "level3": "deep value",
                "sibling": "another value"
            },
            "level2_b": "value"
        }
    }
    
    # Try different paths
    paths = [
        ["level1", "level2", "level3"],
        ["level1", "level2_b"],
        ["level1", "level2", "sibling"]
    ]

    for path in paths:
        try:
            result = access_nested_map(nested_map2, path)
            print(f"Example 2 - Path {path}:")
            print(f"Result: {result}\n")
        except KeyError as e:
            print(f"Error: Key {e} not found\n")

    # Example 3: Error case - invalid path
    invalid_nested_map = {"a": 1}
    invalid_path = ["a", "b"]  # This will raise an error because 'a' is not a mapping
    
    try:
        result = access_nested_map(invalid_nested_map, invalid_path)
        print(f"Example 3 - Path {invalid_path}:")
        print(f"Result: {result}\n")
    except KeyError as e:
        print(f"Example 3 - Error case:")
        print(f"Error: Key {e} not found\n")

if __name__ == "__main__":
    main()
