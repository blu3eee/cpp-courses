import csv
from .CourseInfo import CourseInfo
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
        "description": course_obj.description,
        "prerequisites": course_obj.prerequisites
    }

# Export dictionaries to JSON
with open('./CourseCurriculum/courses_2023-2024.json', 'w') as f:
    json.dump(course_dicts, f, indent=4)