from nssperson import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, instructor_slack_handle, instructor_cohort):
        super().__init__(first_name, last_name, instructor_slack_handle, instructor_cohort)
        self.instructor_specialty = list()

    def asign_student_exercise(self, student, exercise):
       student.exercises.append(exercise) 