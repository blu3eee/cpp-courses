import csv
import json
import re

def parse_course(course_str):
    pattern = r'([^-\n]+)\s*-\s*(.*?)\s*\((\d+-?\d*)\)?'
    match = re.match(pattern, course_str)
    
    if match:
        course_id, name, units = match.groups()
        return {"id": course_id.strip(), "name": name.strip(), "units": units}
    else:
        print(f"Error parsing course: {course_str}")
        return None

def parse_data(school_year: str):

    # Read the requirements file to get the majors and their requirements
    major_requirements = {}
    with open(f'./CourseCurriculum/{school_year}_Requirements.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            major, requirements = row
            major_requirements[major.split(': ')[0]] = {"requirements": requirements}

    with open(f'./CourseCurriculum/{school_year}_Programs.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            major, required, electives = row
            
            required_courses = [parse_course(course)["id"] for course in required.split("),") if parse_course(course) is not None]
            electives_courses = [parse_course(course)["id"] for course in electives.split("),") if parse_course(course) is not None]
            major_requirements[major.split(': ')[0]] = {
                "requirements": major_requirements[major.split(': ')[0]]["requirements"],
                "required": required_courses,
                "electives": electives_courses,
                "units": major.split(': ')[1],
                "name": major.split(': ')[0],
            }

    # Export dictionaries to JSON
    with open(f'./parsed/majors_{school_year}.json', 'w') as f:
        json.dump(major_requirements, f, indent=2)

    courses_info = {}

    with open(f'./CourseCurriculum/{school_year}_Courses.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            course, prereq, coreq = row
            course = parse_course(course)
            if (course):
                courses_info[course["id"]] = {
                    "id": course["id"],
                    "name": course['name'],
                    "units": course["units"],
                    "prerequisites": prereq,
                    "corequisites": coreq
                }
            
    # Export dictionaries to JSON
    with open(f'./parsed/courses_{school_year}.json', 'w') as f:
        json.dump(courses_info, f, indent=2)


available_years = ['2019-2020', '2020-2021', '2021-2022', '2022-2023', '2023-2024']

for school_year in available_years:
    parse_data(school_year)