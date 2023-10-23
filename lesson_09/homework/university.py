from student import Student

students = [
    Student('Aleksey Smirnov', 6),
    Student('Anna Volkova', 8),
    Student('Ivan Petrov', 9),
    Student('Alisa Kovalchuk', 9.5),
    Student('Anton Vlasov', 6.5),
]

def calc_sum_scholarship(students):
    ts = sum(student.get_scholarship() for student in students)
    return ts

def get_excellent_student_count(students):
    exc = sum(1 for student in students if student.is_excellent())
    return exc
