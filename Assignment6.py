import numbers


1. Reverse a number without converting to string
def q1_reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return sign * rev


 2. Check whether a number is a palindrome
def q2_number_palindrome(n):
    return n >= 0 and n == q1_reverse_number(n)


 3. Check whether a number is an Armstrong number 
def q3_armstrong(n):
    if n < 0:
        return False
    digits = len(str(n))
    total = sum(int(d) ** digits for d in str(n))
    return total == n


 4. Factorial using a loop 
def q4_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


 5. Fibonacci series up to N terms 
def q5_fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


 6. Check whether a number is prime 
def q6_is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


7. Print all prime numbers between 1 and 100 
def q7_primes_1_to_100():
    return [n for n in range(1, 101) if q6_is_prime(n)]


8. Find GCD and LCM of two numbers 

def q8_gcd_lcm(a, b):
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    gcd = x
    lcm = 0 if a == 0 or b == 0 else abs(a * b) // gcd
    return gcd, lcm


 9. Reverse a string without slicing 
def q9_reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result


 10. Check whether a string is a palindrome
def q10_string_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == q9_reverse_string(cleaned)


 11. Count vowels, consonants, digits and special characters 
def q11_count_string_types(s):
    vowels = consonants = digits = special = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
                else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif not ch.isspace():
            special += 1
    return {"vowels": vowels, "consonants": consonants,
            "digits": digits, "special_characters": special}


12. Frequency of each character in a string 
def q12_character_frequency(s):
    frequency = {}
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency


13. First non-repeating character 
def q13_first_non_repeating(s):
    frequency = q12_character_frequency(s)
    for ch in s:
        if frequency[ch] == 1:
            return ch
    return None


 14. Remove duplicate characters from a string 
def q14_remove_duplicate_characters(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result


 15. Check whether two strings are anagrams 
def q15_are_anagrams(a, b):
    clean_a = sorted(ch.lower() for ch in a if ch.isalnum())
    clean_b = sorted(ch.lower() for ch in b if ch.isalnum())
    return clean_a == clean_b


16. Find the longest word in a sentence 
def q16_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)


17. Find the second-largest element without sort() 
def q17_second_largest(numbers):
    largest = second = None
    for n in numbers:
        if largest is None or n > largest:
            if n != largest:
                second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second  # None if there is no distinct second-largest value


 18. Remove duplicate elements from a list without set() 
def q18_remove_list_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


19. Find common elements between two lists 
def q19_common_elements(a, b):
    result = []
    for item in a:
        if item in b and item not in result:
            result.append(item)
    return result


 20. Move all zeros to the end, preserving other order 
def q20_move_zeros(numbers):
    non_zeros = [n for n in numbers if n != 0]
    zeros = [n for n in numbers if n == 0]
    return non_zeros + zeros


 21. Find missing number in a list containing 1 to N 
def q21_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)


22. Maximum difference where larger element appears later 
def q22_max_difference(numbers):
    if len(numbers) < 2:
        return None
    minimum_so_far = numbers[0]
    max_difference = None
    for value in numbers[1:]:
        difference = value - minimum_so_far
        if max_difference is None or difference > max_difference:
            max_difference = difference
        minimum_so_far = min(minimum_so_far, value)
    return max_difference


 23. Rotate a list to the right by K positions 
def q23_rotate_right(items, k):
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else items[:]


 24. Find pairs whose sum equals a target 
def q24_pairs_with_sum(numbers, target):
    pairs = []
    seen = set()
    for n in numbers:
        complement = target - n
        if complement in seen:
            pair = (complement, n)
            if pair not in pairs:
                pairs.append(pair)
        seen.add(n)
    return pairs


25. Count frequency of each word in a paragraph 
def q25_word_frequency(paragraph):
    frequency = {}
    for word in paragraph.lower().split():
        word = word.strip(".,!?;:\"'()[]{}")
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency


26. Merge two dictionaries; add values for common keys 
def q26_merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


 27. Sort a dictionary based on its values 
def q27_sort_dictionary(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))


28. Find student with highest marks 
def q28_top_student(students):
    # Example: [{"name": "Asha", "marks": 90}, {"name": "Ravi", "marks": 85}]
    if not students:
        return None
    return max(students, key=lambda student: student["marks"])


 29. Group words by their first character 
def q29_group_by_first_character(words):
    groups = {}
    for word in words:
        if word:
            first = word[0].lower()
            groups.setdefault(first, []).append(word)
    return groups


 30. Convert two lists into a dictionary 
def q30_lists_to_dictionary(keys, values):
    if len(keys) != len(values):
        raise ValueError("Both lists must have the same length.")
    return dict(zip(keys, values))


 31. Recursive function to calculate factorial 
def q31_recursive_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * q31_recursive_factorial(n - 1)


 32. Recursive function to find sum of digits 
def q32_recursive_sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + q32_recursive_sum_digits(n // 10)


33. Implement own map() function 
def q33_my_map(function, iterable):
    result = []
    for item in iterable:
        result.append(function(item))
    return result


 34. Return only even numbers from a list 
def q34_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]


 35. Flatten a nested list 
def q35_flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(q35_flatten(item))
        else:
            result.append(item)
    return result


 36. Student Management System 
def q36_student_management():
    students = {}  # student_id: {"name": ..., "marks": ...}
    while True:
        print("\\n1.Add student  2.Display all  3.Search by ID")
        print("4.Update student  5.Delete student  6.Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            sid = input("Student ID: ").strip()
            if sid in students:
                print("Student ID already exists.")
                continue
            name = input("Student name: ").strip()
            marks = float(input("Marks: "))
            students[sid] = {"name": name, "marks": marks}
            print("Student added.")
        elif choice == "2":
            if not students:
                print("No student records.")
            for sid, details in students.items():
                print(sid, details)
        elif choice == "3":
            sid = input("Enter student ID: ").strip()
            print(students.get(sid, "Student not found."))
        elif choice == "4":
            sid = input("Enter student ID to update: ").strip()
            if sid in students:
                students[sid]["name"] = input("New name: ").strip()
                students[sid]["marks"] = float(input("New marks: "))
                print("Student updated.")
            else:
                print("Student not found.")
        elif choice == "5":
            sid = input("Enter student ID to delete: ").strip()
            if students.pop(sid, None) is not None:
                print("Student deleted.")
            else:
                print("Student not found.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


 37. Bank Account Management 
def q37_bank_account_management():
    accounts = {}  # account_number: {"name": ..., "balance": ...}
    while True:
        print("\\n1.Create account  2.Deposit  3.Withdraw")
        print("4.Check balance  5.Display account details  6.Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            acc = input("Account number: ").strip()
            if acc in accounts:
                print("Account already exists.")
                continue
            name = input("Account holder name: ").strip()
            accounts[acc] = {"name": name, "balance": 0.0}
            print("Account created.")
        elif choice in ("2", "3", "4", "5"):
            acc = input("Account number: ").strip()
            if acc not in accounts:
                print("Account not found.")
                continue
            if choice == "2":
                amount = float(input("Deposit amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    accounts[acc]["balance"] += amount
                    print("Deposit successful.")
            elif choice == "3":
                amount = float(input("Withdrawal amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > accounts[acc]["balance"]:
                    print("Insufficient balance.")
                else:
                    accounts[acc]["balance"] -= amount
                    print("Withdrawal successful.")
            elif choice == "4":
                print("Balance:", accounts[acc]["balance"])
            else:
                print("Account number:", acc, "| Details:", accounts[acc])
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


 38. Employee Salary Management 
def q38_employee_salary_management():
    employees = {}
    while True:
        print("\\n1.Add employee  2.Calculate/display salary  3.Display all  4.Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            eid = input("Employee ID: ").strip()
            if eid in employees:
                print("Employee ID already exists.")
                continue
            name = input("Employee name: ").strip()
            basic = float(input("Basic salary: "))
            hra = float(input("HRA: "))
            allowance = float(input("Other allowance: "))
            deductions = float(input("Total deductions: "))
            employees[eid] = {
                "name": name, "basic": basic, "hra": hra,
                "allowance": allowance, "deductions": deductions
            }
            print("Employee added.")
        elif choice in ("2", "3"):
            records = employees.items() if choice == "3" else None
            if choice == "2":
                eid = input("Employee ID: ").strip()
                if eid not in employees:
                    print("Employee not found.")
                    continue
                records = [(eid, employees[eid])]
            for eid, emp in records:
                gross = emp["basic"] + emp["hra"] + emp["allowance"]
                net = gross - emp["deductions"]
                print("\\nID:", eid, "| Name:", emp["name"])
                print("Gross salary:", gross)
                print("Deductions:", emp["deductions"])
                print("Net salary:", net)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


 39. Library Management System 
def q39_library_management():
    books = {}  # title: {"available": True/False}
    while True:
        print("\\n1.Add book  2.Display available books  3.Issue book")
        print("4.Return book  5.Search by title  6.Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Book title: ").strip()
            if title in books:
                print("Book already exists in this simple library record.")
            else:
                books[title] = {"available": True}
                print("Book added.")
        elif choice == "2":
            available = [title for title, info in books.items() if info["available"]]
            print("Available books:", available)
        elif choice in ("3", "4", "5"):
            title = input("Enter book title: ").strip()
            if choice == "5":
                print(books.get(title, "Book not found."))
            elif title not in books:
                print("Book not found. Add it first.")
            elif choice == "3":
                if books[title]["available"]:
                    books[title]["available"] = False
                    print("Book issued.")
                else:
                    print("Book is already issued.")
            else:
                if not books[title]["available"]:
                    books[title]["available"] = True
                    print("Book returned.")
                else:
                    print("Book was not issued.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")



 40. Task Management Application 
def q40_task_management():
    tasks = {}  # task_id: {"title": ..., "completed": ...}
    while True:
        print("\\n1.Add task  2.View all tasks  3.Update task")
        print("4.Delete task  5.Mark completed  6.Filter tasks  7.Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            tid = input("Task ID: ").strip()
            if tid in tasks:
                print("Task ID already exists.")
                continue
            title = input("Task description: ").strip()
            tasks[tid] = {"title": title, "completed": False}
            print("Task added.")
        elif choice == "2":
            if not tasks:
                print("No tasks.")
            for tid, task in tasks.items():
                status = "Completed" if task["completed"] else "Pending"
                print(tid, "-", task["title"], "-", status)
        elif choice in ("3", "4", "5"):
            tid = input("Task ID: ").strip()
            if tid not in tasks:
                print("Task not found.")
                continue
            if choice == "3":
                tasks[tid]["title"] = input("New task description: ").strip()
                print("Task updated.")
            elif choice == "4":
                del tasks[tid]
                print("Task deleted.")
            else:
                tasks[tid]["completed"] = True
                print("Task marked as completed.")
        elif choice == "6":
            status = input("Type 'completed' or 'pending': ").strip().lower()
            if status not in ("completed", "pending"):
                print("Invalid status.")
                continue
            wanted = status == "completed"
            for tid, task in tasks.items():
                if task["completed"] == wanted:
                    print(tid, "-", task["title"])
        elif choice == "7":
            break
        else:
            print("Invalid choice.")















































