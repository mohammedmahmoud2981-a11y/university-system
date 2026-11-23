# University System

A Python command-line application that parses student academic records from an HTML table (`data.html`), calculates GPA and performance statistics, and provides an interactive terminal menu for querying student, subject, and department data.

- **Repository:** [takya7180-glitch/university-system](https://github.com/takya7180-glitch/university-system)
- **Main Script:** [`project_universty_system.py`](https://github.com/takya7180-glitch/university-system/blob/main/project_universty_system.py)
- **Languages:** Python (61%) · HTML (39%)

## Features

- **HTML Table Parsing:** Extracts student names, IDs, departments, subjects, and numeric grades from `data.html` using `BeautifulSoup` (`html.parser`).
- **Automated GPA & Grading:** Calculates each student's average score, 4.0-scale GPA, and letter grade.
- **Student Lookup & Ranking:** Searches for individual students by name and ranks all students from highest to lowest GPA.
- **Subject & Department Analytics:** Computes enrollment counts and average grades per subject, as well as average grades per department.
- **Pass/Fail Summary:** Tracks the total number of passing (`average >= 60`) and failing (`average < 60`) students.

## Project Structure

| File | Description |
| :--- | :--- |
| [`project_universty_system.py`](https://github.com/takya7180-glitch/university-system/blob/main/project_universty_system.py) | Main Python script containing HTML parsing, statistical calculations, and the interactive CLI menu. |
| `data.html` | Input HTML file containing the student records table loaded at runtime. |
| `project universty system.pyproj` | Visual Studio Python project configuration file. |
| `project universty system.slnx` | Visual Studio solution file. |
| `README.md` | Project documentation. |

> **Note:** The main script filename uses the spelling `project_universty_system.py` (without the second `i`).

## Prerequisites

- **Python 3.x**
- **BeautifulSoup 4** (`beautifulsoup4`) — uses Python's built-in `html.parser`

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/takya7180-glitch/university-system.git
   cd university-system
   ```

2. Install the required dependency:

   ```bash
   pip install beautifulsoup4
   ```

## Usage

Run the main script from the repository root (ensure `data.html` is in the same directory):

```bash
python project_universty_system.py
```

Alternatively, open `project universty system.slnx` in Visual Studio to run the project directly.

### Interactive CLI Menu

Once launched, select an option by entering its number:

| Option | Action |
| :---: | :--- |
| `1` | Display all students and their details |
| `2` | Search for a student by name |
| `3` | List students sorted by GPA (highest to lowest) |
| `4` | View subject statistics (enrollment count and average grade) |
| `5` | View department statistics (average grade per department) |
| `6` | View pass/fail student counts |
| `0` | Exit the application |

## Grading Scale

The `calculate_gpa(avg)` function maps each student's numeric average to a 4.0-scale GPA and letter grade:

| Average Score | Letter Grade | GPA | Status |
| :--- | :---: | :---: | :--- |
| 90 and above | A | 4.0 | Pass |
| 80 – 89.99 | B | 3.0 | Pass |
| 70 – 79.99 | C | 2.0 | Pass |
| 60 – 69.99 | D | 1.0 | Pass |
| Below 60 | F | 0.0 | Fail |

## Expected `data.html` Format

`parse_html(file_path)` reads `data.html` using UTF-8 encoding, skips the header `<tr>` row, and expects 5 columns (`<td>`) per student row:

| Column | Field | Format |
| :---: | :--- | :--- |
| 1 | Name | Student full name |
| 2 | ID | Student identifier |
| 3 | Department | Department name |
| 4 | Subjects | Space-separated subject names |
| 5 | Grades | Space-separated numeric grades matching each subject |

## Core Functions Overview

| Function | Responsibility |
| :--- | :--- |
| `parse_html(file_path)` | Parses `<tr>` rows from `data.html` into structured student dictionaries. |
| `calculate_gpa(avg)` | Converts a numeric average into a `(gpa, letter)` pair on a 4.0 scale. |
| `student_stats(students)` | Computes and stores `average`, `gpa`, and `letter` for every student. |
| `subject_stats(students)` | Calculates enrollment count and average score for each subject. |
| `department_stats(students)` | Calculates the average student grade for each department. |
| `sort_students(students)` | Returns students sorted in descending order by GPA. |
| `get_student(students, name)` | Finds and returns a student record matching the given name. |
| `pass_fail_count(students)` | Counts passing (`average >= 60`) and failing (`average < 60`) students. |
| `display_all(students)` | Prints formatted academic details for all students. |
| `menu(students)` | Runs the interactive command-line loop (`0`–`6`). |

## Credits

Forked from `mohammedmahmoud2981-a11y/university-system`.
