from bs4 import BeautifulSoup

# =========================
# 1) PARSE HTML (FIXED)
# =========================
def parse_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    rows = soup.find_all("tr")[1:]  # skip header

    students = {}

    for row in rows:
        cols = row.find_all("td")

        name = cols[0].text.strip()
        student_id = cols[1].text.strip()
        dept = cols[2].text.strip()

        # subjects + grades (multi values in same td)
        subjects = cols[3].text.strip().split()
        grades = list(map(float, cols[4].text.strip().split()))

        if name not in students:
            students[name] = {
                "id": student_id,
                "department": dept,
                "grades": {}
            }

        # safe mapping
        for i in range(min(len(subjects), len(grades))):
            subject = subjects[i]
            grade = grades[i]

            if subject not in students[name]["grades"]:
                students[name]["grades"][subject] = []

            students[name]["grades"][subject].append(grade)

    return students


# =========================
# 2) GPA CALCULATION
# =========================
def calculate_gpa(avg):
    if avg >= 90:
        return 4.0, "A"
    elif avg >= 80:
        return 3.0, "B"
    elif avg >= 70:
        return 2.0, "C"
    elif avg >= 60:
        return 1.0, "D"
    else:
        return 0.0, "F"


def student_stats(students):
    for name, data in students.items():
        all_grades = []

        for grades_list in data["grades"].values():
            all_grades.extend(grades_list)

        avg = sum(all_grades) / len(all_grades)
        gpa, letter = calculate_gpa(avg)

        data["average"] = avg
        data["gpa"] = gpa
        data["letter"] = letter


# =========================
# 3) SUBJECT STATS
# =========================
def subject_stats(students):
    subjects = {}

    for data in students.values():
        for subject, grades in data["grades"].items():
            subjects.setdefault(subject, []).extend(grades)

    result = {}

    for subject, grades in subjects.items():
        result[subject] = {
            "count": len(grades),
            "average": sum(grades) / len(grades)
        }

    return result


# =========================
# 4) DEPARTMENT STATS
# =========================
def department_stats(students):
    depts = {}

    for data in students.values():
        depts.setdefault(data["department"], []).append(data["average"])

    result = {}

    for dept, avgs in depts.items():
        result[dept] = sum(avgs) / len(avgs)

    return result


# =========================
# 5) SORT STUDENTS
# =========================
def sort_students(students):
    return sorted(
        students.items(),
        key=lambda x: x[1]["gpa"],
        reverse=True
    )


# =========================
# 6) GET STUDENT
# =========================
def get_student(students, name):
    return students.get(name)


# =========================
# 7) PASS / FAIL
# =========================
def pass_fail_count(students):
    passed = 0
    failed = 0

    for data in students.values():
        if data["average"] >= 60:
            passed += 1
        else:
            failed += 1

    return passed, failed


# =========================
# 8) DISPLAY ALL
# =========================
def display_all(students):
    for name, data in students.items():
        print("\n===================")
        print("Name:", name)
        print("ID:", data["id"])
        print("Department:", data["department"])
        print("Grades:", data["grades"])
        print("Average:", round(data["average"], 2))
        print("GPA:", data["gpa"])
        print("Letter:", data["letter"])


# =========================
# 9) MENU
# =========================
def menu(students):
    while True:
        print("\n========= MENU =========")
        print("1-show all students")
        print("2 - show student by name")
        print("3 - show students by GPA")
        print("4 - show subject statistics")
        print("5 - show department statistics")
        print("6 -Count of passed and failed students")
        print("0 -Exit")

        choice = input("Select: ")

        if choice == "1":
            display_all(students)

        elif choice == "2":
            name = input("Enter student name: ")
            student = get_student(students, name)

            if student:
                print(student)
            else:
                print("Student not found")

        elif choice == "3":
            for name, data in sort_students(students):
                print(name, "-> GPA:", data["gpa"])

        elif choice == "4":
            print(subject_stats(students))

        elif choice == "5":
            print(department_stats(students))

        elif choice == "6":
            print(pass_fail_count(students))

        elif choice == "0":
            break

        else:
            print("Invalid choice")


# =========================
# 10) RUN PROGRAM
# =========================
if __name__ == "__main__":
    students = parse_html("data.html")
    student_stats(students)
    menu(students)