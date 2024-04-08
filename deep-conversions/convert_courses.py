from typing import Dict
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
major_courses = {}
with open('./CourseCurriculum/2023-2024_Programs.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        major_name, required_courses, electives = row
        # all_courses = required_courses.split(", ") + electives.split(", ")
        major_courses[major_name] = {
            "required": required_courses.split("),"),
            "electives": electives.split("),")
        }

# Convert the courses into CourseInfo objects
course_objects = {}
for major, courses in major_courses.items():
    for course in courses['required']:
        if course == '':
            continue
        units = str(course[-3:]).strip().replace(')', '').replace('(', '')
        
        parts = str(course[:-3]).split(' - ')
        courseID = parts[0]
        name = ' - '.join(parts[1:])
            
        course_objects[courseID] = CourseInfo(courseID, name, units)
        
    for course in courses['electives']:
        if course == '':
            continue
        units = str(course[-3:]).strip().replace(')', '').replace('(', '')
        
        parts = str(course[:-3]).split(' - ')
        courseID = parts[0]
        name = ' - '.join(parts[1:])
        # print(courseID, name)
            
        course_objects[courseID] = CourseInfo(courseID, name, units)

import json

# Convert CourseInfo objects to dictionaries
course_dicts = {}
for courseID, course_obj in course_objects.items():
    course_dicts[courseID] = {
        "courseID": course_obj.courseID,
        "name": course_obj.name,
        "units": course_obj.units,
        "prerequisites": course_obj.prerequisites
    }

# Export dictionaries to JSON
# with open('./CourseCurriculum/courses_2023-2024.json', 'w') as f:
#     json.dump(course_dicts, f, indent=4)
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
                    # print(course.required_standing)
            print()
            
        course.prerequisites = []
        
        
        course.corequisites = []

        course_objects[courseID] = course
        tested_rows+=1
        if (tested_rows == 10):
            break