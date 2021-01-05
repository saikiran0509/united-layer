
class Member:
    """Member(Person) Details."""

    def __init__(self, full_name: str='', intro: str='', msg : str='', is_instructor=False, skills=None):
        """Initialize the attributes of member(Person)."""
        self.full_name = full_name
        self.intro = intro
        if is_instructor:
            self.member_type = "instructor"
            self.bio = msg
            self.skills_list = skills or []
        else:
            self.member_type = "attendees"
            self.reason = msg

    def add_skill(self, skill :str):
        """Add the skill to instructor skill sets."""
        if self.member_type == "instructor":
            self.skills_list.append(skill)

    def __str__(self):
        """Return the type of this Member object"""
        return f'This Member is a {self.member_type}'


class Workshop:
    """Workshop in PythonCon."""

    EVENT_MSG = "Welcome to {} Workshop \nDate = {} \nTotal Instructors = {} \nTotal Attendees = {} \n"
    INST_MSG="{})Full Name = {} \n Intro = {} \n About = {} \n Skills = {} \n"
    ATDS_MSG="{})Full Name = {} \n Intro = {} \n Reason = {} \n"

    def __init__(self, event_date: str, subject: str):
        """Initialize the basic attributes of Workshop."""
        self.event_date = event_date
        self.subject = subject
        self.instructor_list = []
        self.attendees_list = []

    @property
    def total_instructors(self) -> int:
        """Returns the total number of instructors for this Workshop."""
        return len(self.instructor_list)

    @property
    def total_attendees(self) -> int:
        """Returns the total number of attendees for this Workshop."""
        return len(self.attendees_list)

    def add_participant(self, member_obj: Member):
        """Add the Member to either instructor_list or attendees_list based on is_instructor."""
        if member_obj.member_type == "instructor":
            self.instructor_list.append(member_obj)
        else:
            self.attendees_list.append(member_obj)

    def print_details(self):
        """Print the details of the Workshop."""
        print(Workshop.EVENT_MSG.format(self.subject.upper(), self.event_date, self.total_instructors, self.total_attendees))
        #Instructor Details
        print("\nInstructor Details:")
        for idx, int_obj in enumerate(self.instructor_list, start=1):
            print(Workshop.INST_MSG.format(idx, int_obj.full_name, int_obj.intro, int_obj.bio, int_obj.skills_list))
        #Attendees Details
        print("\nAttendees Details:")
        for idx, ats_obj in enumerate(self.attendees_list, start=1):
            print(Workshop.ATDS_MSG.format(idx, ats_obj.full_name, ats_obj.intro, ats_obj.reason))
        print(f"\n---------------- END OF {self.subject.upper()} WORKSHOP ----------------\n")

    def __repr__(self):
        """Return the coding representations of how to create the Workshop class instance"""
        return f'Workshop(event_date="{self.event_date}", subject="{self.subject}")'


def main():
    """All the Instances Creation logics of PYTHON_CON can happen here."""
    a1 = {"full_name": "sai kiran", "intro": "Hi, my name is sai kiran!", "msg": "I've always wanted to make websites!"}
    a2 = {"full_name": "venkatesh", "intro": "Hi, my name is venkatesh!", "msg": "I've always wanted to learn coading!"}
    a3 = {"full_name": "santosh", "intro": "Hi, my name is santosh!", "msg": "I wanted to create new websites!"}
    i1 = {"full_name": "sarath", "intro": "Hi, my name is sarath!", "is_instructor": True, "skills": ["python"],
          "msg": "I've been coding in Python for 4 years and want to share my experience!"}
    i2 = {"full_name": "avinash", "intro": "Hi, my name is avinash!", "is_instructor": True, "skills": ["python", "Go"],
          "msg": "I've been coding in Python & Go for 2 years and want to share my experience!"}

    #Creating the Member Instances
    a1_obj = Member(**a1)
    a2_obj = Member(**a2)
    a3_obj = Member(**a3)
    i1_obj = Member(**i1)
    i2_obj = Member(**i2)
    i1_obj.add_skill("c++")
    #Creating the Workshop Instances
    w1_obj = Workshop(event_date="20210115", subject="python Tech talk")
    w1_obj.add_participant(a1_obj)
    w1_obj.add_participant(i1_obj)
    w1_obj.add_participant(a3_obj)
    w2_obj = Workshop(event_date="20210125", subject="Python & Go Discussion")
    w2_obj.add_participant(a2_obj)
    w2_obj.add_participant(i2_obj)
    #Print the Details of the Workshops
    w1_obj.print_details()
    w2_obj.print_details()


if __name__ == '__main__':
    main()
