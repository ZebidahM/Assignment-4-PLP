#my code
from operator import itemgetter

def sort_dict_list(dict_list, key, reverse=False):
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


# #github copilot code
def sort_by_key(data, key, reverse=False):
    """
    Sorts a list of dictionaries by a specified key, handling missing keys and mixed types.
    """
    def safe_key(d):
        value = d.get(key, None)
        return str(value) if value is not None else ''
    return sorted(data, key=safe_key, reverse=reverse)

if __name__ == "__main__":
    # Example 1: Students
    students = [
        {"name": "Alice", "age": 23, "grade": 85},
        {"name": "Bob", "age": 21, "grade": 92},
        {"name": "Charlie", "age": 22, "grade": 78},
        {"name": "Diana", "age": 24, "grade": 96}
    ]
    print("Students sorted by age:")
    for s in sort_by_key(students, "age"):
        print(f"  {s}")

    # Example 2: Employees (different structure)
    employees = [
        {"employee_id": 101, "department": "HR", "salary": 50000},
        {"employee_id": 102, "department": "IT", "salary": 70000},
        {"employee_id": 103, "department": "Finance", "salary": 65000}
    ]
    print("\nEmployees sorted by salary (descending):")
    for e in sort_by_key(employees, "salary", reverse=True):
        print(f"  {e}")

    # Example 3: Cars (another structure)
    cars = [
        {"make": "Toyota", "model": "Corolla", "year": 2020},
        {"make": "Honda", "model": "Civic", "year": 2018},
        {"make": "Ford", "model": "Focus", "year": 2019}
    ]
    print("\nCars sorted by year:")
    for c in sort_by_key(cars, "year"):
        print(f"  {c}")