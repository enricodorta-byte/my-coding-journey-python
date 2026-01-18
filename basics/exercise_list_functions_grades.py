# Exercise: Lists + functions + loops
# Collect grades from user until -1, then compute stats
# Date: 18 January 2026

def calculate_grade_stats(grades):
    """Compute average, max, min, and passing count from a list of grades."""
    if not grades:
        return None, None, None, 0
    
    average = sum(grades) / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)
    passing = sum(1 for grade in grades if grade >= 6)
    
    return average, max_grade, min_grade, passing

# Main program
grades = [] #Empty list to store valid grades

print("Grade calculator (enter -1 to finish)")

while True:
    try:
        grade = float(input("Enter grade (0-10; 1 to stop): "))
    except ValueError:
        print("Invalid input - please enter a number.")
        continue

    if grade == -1:
        break

    if 0 <= grade <= 10:
        grades.append(grade)
    else:
        print("Grade must be between 0 and 10 - discarded.")

# Results
if grades:
    avg, max_g, min_g, passing_count = calculate_grade_stats(grades)
    print("\nGrade statistics:")
    print(f"Number of grades: {len(grades)}")
    print(f"Average grade: {avg:.2f}")
    print(f"Highest grade: {max_g}")
    print(f"Lowest grade: {min_g}")
    print(f"Passing grades (>= 6): {passing_count} ({(passing_count / len(grades)) * 100:.1f}%)")
else:
    print("\nNo valid grades entered.")
    