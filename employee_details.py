# employee.py
# Program to accept employee information and return a formatted string

import sys

def get_employee_details(name, emp_id, department, salary):
    """Return a formatted string with employee details."""
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

if __name__ == "__main__":
    print("=== Employee Information Processor ===")
    try:
        # Case 1: Values passed via command-line arguments (CLI/Jenkins)
        if len(sys.argv) > 4:
            name = sys.argv[1]
            emp_id = sys.argv[2]
            department = sys.argv[3]
            salary = float(sys.argv[4])
        else:
            # Case 2: No arguments — use default employee details
            name = "John Doe"
            emp_id = "E101"
            department = "HR"
            salary = 55000

        print("\n=== Program Parameters ===")
        print("Name:", name)
        print("Employee ID:", emp_id)
        print("Department:", department)
        print("Salary:", salary)

        # Format details using the function
        details = get_employee_details(name, emp_id, department, salary)

        print("\n=== Employee Details ===")
        print(details)

    except ValueError:
        print("Error: Salary must be a valid number.")
    except Exception as e:
        print("An error occurred:", e)
