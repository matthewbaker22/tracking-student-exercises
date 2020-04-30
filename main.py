from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

student_1 = Student("Matt", "Baker", "matthewbaker22", 38)
student_2 = Student("Matt", "Krueger", "mattkSlack", 38)
student_3 = Student("Mike", "Prince", "mikeprince", 38)
student_4 = Student("Michael", "Clark", "michaelclark", 38)

exercise_1 = Exercise("Daily Journal", "JavaScript")
exercise_2 = Exercise("Nutshell", "JavaScript")
exercise_3 = Exercise("React Nutshell", "React")
exercise_4 = Exercise("Tracking Student Exercises", "Python")

instructor_1 = Instructor("Andy", "Collins", "andycollins", 40)
instructor_2 = Instructor("Kristen", "Norris", "kristennorris", 38)
instructor_3 = Instructor("Bryan", "Neilson", "bryanneilson", 40)

instructor_1.asign_student_exercise(student_1, exercise_1)
instructor_1.asign_student_exercise(student_2, exercise_1)

