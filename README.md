# Course Curriculum Management

## Overview

This Python script manages information about different courses and major requirements. It reads from CSV files to populate `CourseInfo` and `MajorInfo` objects and exports the CourseInfo objects to a JSON file.

## Features

Reads major courses from a CSV file (2023-2024_Programs.csv) and populates CourseInfo objects.
Exports the course information to a JSON file (courses_2023-2024.json).

## Files

`2023-2024_Programs.csv`: Contains information about major courses, including major name, required courses, and electives.
`courses_2023-2024.json`: The exported JSON file that contains all the course information.

## Python Classes

`MajorInfo`: Stores information related to a major such as required and elective courses.
`CourseInfo`: Stores detailed information about individual courses.

## Dependencies

Python 3.x
CSV module
JSON module

## Usage

1. Make sure you have Python installed.
2. Run the script.

```
python your_script_name.py
```

This will generate a JSON file courses_2023-2024.json in the ./CourseCurriculum directory.
