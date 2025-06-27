def sort_dict_list(dict_list, key, reverse=False):
    """
    Sort a list of dictionaries by a specific key.
    
    Args:
        dict_list (list): List of dictionaries to sort
        key (str): The key to sort by
        reverse (bool): If True, sort in descending order. Default is False (ascending)
    
    Returns:
        list: Sorted list of dictionaries
    
    Raises:
        KeyError: If the key doesn't exist in one or more dictionaries
        TypeError: If dict_list is not a list or contains non-dict items
    """
    if not isinstance(dict_list, list):
        raise TypeError("First argument must be a list")
    
    if not dict_list:  # Handle empty list
        return dict_list
    
    # Check if all items are dictionaries
    if not all(isinstance(item, dict) for item in dict_list):
        raise TypeError("All items in the list must be dictionaries")
    
    # Check if key exists in all dictionaries
    if not all(key in item for item in dict_list):
        raise KeyError(f"Key '{key}' not found in all dictionaries")
    
    return sorted(dict_list, key=lambda x: x[key], reverse=reverse)


# Example usage and test cases
if __name__ == "__main__":
    # Sample data
    students = [
        {"name": "Alice", "age": 23, "grade": 85},
        {"name": "Bob", "age": 21, "grade": 92},
        {"name": "Charlie", "age": 22, "grade": 78},
        {"name": "Diana", "age": 24, "grade": 96}
    ]
    
    # Sort by age (ascending)
    print("Sorted by age (ascending):")
    sorted_by_age = sort_dict_list(students, "age")
    for student in sorted_by_age:
        print(f"  {student}")
    
    print("\nSorted by grade (descending):")
    sorted_by_grade = sort_dict_list(students, "grade", reverse=True)
    for student in sorted_by_grade:
        print(f"  {student}")
    
    print("\nSorted by name (alphabetical):")
    sorted_by_name = sort_dict_list(students, "name")
    for student in sorted_by_name:
        print(f"  {student}")
    
    # Alternative: Using Python's built-in sorted() directly
    print("\n--- Alternative approaches ---")
    
    # Simple one-liner for basic sorting
    simple_sort = sorted(students, key=lambda x: x["age"])
    print("Simple sort by age:", simple_sort[0]["name"], "is youngest")
    
    # Using operator.itemgetter for better performance with large datasets
    from operator import itemgetter
    efficient_sort = sorted(students, key=itemgetter("grade"), reverse=True)
    print("Most efficient sort by grade:", efficient_sort[0]["name"], "has highest grade")