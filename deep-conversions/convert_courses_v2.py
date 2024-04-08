import csv

class CourseInfo:
    def __init__(self, courseID, name, units: str | None = None):
        self.courseID = courseID
        self.name = name
        self.units = units
        self.required_standing = []
        self.prerequisites = []
        self.corequisites = []

# Read the programs file to get the courses for each major
course_objects = {}
with open('./CourseCurriculum/2023-2024_Courses.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    
    tested_rows = 0

    for row in reader:
        
        course_name, prereq, coreq = row
        units = str(course_name[-3:]).strip().replace(')', '').replace('(', '')
        course_name_parts = str(course_name[:-3]).strip().split(' - ')
        courseID = course_name_parts[0]
        name = ' - '.join(course_name_parts[1:])

        course = CourseInfo(courseID, name, units)
        
        if prereq != '':
            for requirement in prereq.split(';'):
                print(requirement.strip())
                if "standing" in requirement.lower():
                    academic_standings = []
                    for standing in requirement.split(','):
                        academic_standings.append(standing.replace('standing', '').replace('Standing', '').strip())
                    course.required_standing = academic_standings
                    print(course.required_standing)
            print()
            
        course.prerequisites = []
        
        
        course.corequisites = []

        course_objects[courseID] = course
        tested_rows+=1
        if (tested_rows == 10):
            break