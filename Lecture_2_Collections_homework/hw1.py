"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
import os
import re
from typing import Callable, Iterable


def validate_line(line: str) -> bool:
    parts = line.split()
    if len(parts) == 5:
        return True
    return False


def validate_date(date: str) -> bool:
    parts = date.split()
    date_pattern = re.compile(r'^\d{4}\-\d{2}-\d{2}$')
    for p in parts:
        if date_pattern.match(p):
            return True
    return False


def validate_mail(date: str) -> bool:
    parts = date.split()
    return parts[0].find("@") > 1


def validate_amount(date: str) -> bool:
    parts = date.split()
    return parts[1].match(r'\d+\.\d+')


def validate_currency(date: str) -> bool:
    parts = date.split()
    return len(parts[2]) == 3


check_count = 1


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    global check_count
    report_name = f"report_{check_count}.txt"
    check_count = check_count + 1
    with open(filepath) as file_under_test, open(report_name, "w") as report_file:
        for file_line in file_under_test:
            file_line = file_line.strip()

            # run validation
            for validator in validators:
                is_valid = validator(file_line)
                if not is_valid:
                    report_file.write(f"{file_line} {validator.__name__}\n")
                    break
        report_file.flush()
    return os.path.abspath(report_name)
