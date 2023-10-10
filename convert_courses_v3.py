import pandas as pd
import json
import re
class CourseInfo:
    def __init__(self, courseID, name, units: (str, None) = None):
        self.courseID = courseID
        self.name = name
        self.units = units
        self.prerequisites = []
        self.corequisites = []
def extract_relevant_courses_v2(text, relevant_course_keys):
    """Extract relevant course codes from the given text based on the list of relevant course keys."""
    if pd.isnull(text):
        return []
    
    # Split prerequisites by ";"
    prereq_groups = [group.strip() for group in text.split(';')]
    
    parsed_prereqs = []
    for group in prereq_groups:
        # Extract course codes using regex
        course_codes = re.findall(r'\b[A-Z]{2,4} \d{4}[A-Z]*\b', group)
        
        # Filter based on relevant course keys and add to parsed_prereqs if not empty
        relevant_courses = [code for code in course_codes if code in relevant_course_keys]
        if relevant_courses:
            parsed_prereqs.append(relevant_courses)
    
    return parsed_prereqs

def parse_courses_from_csv(csv_path, json_path):
    # Load the JSON file to get the list of relevant course keys
    with open(json_path, 'r') as file:
        courses_json = json.load(file)
    relevant_course_keys = list(courses_json.keys())


    # Load the CSV file
    courses_df = pd.read_csv(csv_path)

    course_objects = {}

    for index, row in courses_df.iterrows():
        course_name, prereq, coreq = row
        units = str(course_name[-3:]).strip().replace(')', '').replace('(', '')
        course_name_parts = str(course_name[:-3]).strip().split(' - ')
        courseID = course_name_parts[0]
        name = ' - '.join(course_name_parts[1:])

        course = CourseInfo(courseID, name, units)
        course.prerequisites = extract_relevant_courses_v2(prereq, relevant_course_keys)
        course.corequisites = extract_relevant_courses_v2(coreq, relevant_course_keys)
        course_objects[courseID] = course

    # Convert CourseInfo objects to dictionaries
    parsed_courses = {}
    for courseID, course_obj in course_objects.items():
        parsed_courses[courseID] = {
            "courseID": course_obj.courseID,
            "name": course_obj.name,
            "units": course_obj.units,
            "prerequisites": course_obj.prerequisites,
            "corequisites": course_obj.corequisites
        }                    

    return parsed_courses

if __name__ == "__main__":
    csv_path = './CourseCurriculum/2023-2024_Courses.csv'
    json_path = './CourseCurriculum/courses_2023-2024.json'
    result_dict = parse_courses_from_csv(csv_path, json_path)
    print(len(result_dict.keys()))
    
    with open('parsed_courses.json', 'w') as outfile:
        json.dump(result_dict, outfile, indent=4)
