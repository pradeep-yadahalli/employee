
import pytest
from employee_details import get_employee_details

def test_get_employee_details():
    name = "Alice"
    emp_id = "EMP123"
    department = "Finance"
    salary = 75000

    expected = (
        "Employee Name: Alice\n"
        "Employee ID: EMP123\n"
        "Department: Finance\n"
        "Salary: 75000"
    )

    assert get_employee_details(name, emp_id, department, salary) == expected
