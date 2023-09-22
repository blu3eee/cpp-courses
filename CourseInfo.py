class CourseInfo:
    def __init__(self, courseID, name, units: str | None = None):
        self.courseID = courseID
        self.name = name
        self.units = units
        self.description = ''
        self.prerequisites = []