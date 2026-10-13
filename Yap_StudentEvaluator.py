#=======================================================================================================================
#       Programmer      : Brentt Ethann R. Yap
#       Section         : 8 - Sampaguita
#       Description     : A Python program that accepts the student’s name and three scores, calculates the average, identifies the performance level,
#                         and displays a report.
#=======================================================================================================================
def display_header():
    print("Student Performance Evaluator")
    print("=============================")

def get_student_info():
    name = input("Enter Student Name: ")
    student_score_1 = float(input("Enter Student Score 1: "))
    student_score_2 = float(input("Enter Student Score 2: "))
    student_score_3 = float(input("Enter Student Score 3: "))
    print(f"{name}")
    print(f"{student_score_1}")
    print(f"{student_score_2}")
    print(f"{student_score_3}")
    return name, student_score_1, student_score_2, student_score_3

def evaluate_performance(student_score_1, student_score_2, student_score_3):
    average_score = (student_score_1 + student_score_2 + student_score_3)/3
    performance_level = ""
    if average_score >= 90:
        performance_level += "Outstanding"
    elif average_score >= 85:
        performance_level += "Very Satisfactory"
    elif average_score >= 80:
        performance_level += "Satisfactory"
    elif average_score >= 75:
        performance_level += "Fairly Satisfactory"
    else:
        performance_level += "Needs Improvement"
    print(f"{average_score:.2f}")

    return performance_level, average_score
display_header()
get_student_info()
evaluate_performance()


