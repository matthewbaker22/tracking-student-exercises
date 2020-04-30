from nssperson import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, student_slack_handle, cohort):
        super().__init__(first_name, last_name, student_slack_handle, cohort)
        self.exercises = list()

    def output(self):
        print(f"{self.first_name} {self.last_name} {self.student_slack_handle} {self.student_cohort} {self.exercises}")

    

