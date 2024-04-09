# Course Parsing and Data Management for BroncoDirectMe

## Overview

This repository contains scripts for parsing course and major information from CSV files into JSON format, intended for use with the BroncoDirectMe web extension. The data, extracted from official sources, undergoes transformation to support easy integration and manipulation within the extension's framework.

## Structure

- `/CourseCurriculum`: Contains raw CSV files with scraped data regarding courses and majors.
- `/parsed`: Destination for JSON files generated from CSV data, housing processed information on courses and majors.
- `main.py`: Python script for converting CSV data from `/CourseCurriculum` into structured JSON files located in `/parsed`.
- `/deep-conversions`: Contains (past and) initial attempts at transforming course requirements (corequisites and prerequisites) into a more detailed data format. This is still under development and not currently operational.

## Usage

1. Ensure Python is installed on your system.
2. Execute `main.py` to generate JSON files within the `/parsed` directory:

```bash
python main.py
```

This process populates the `/parsed` folder with JSON files, ready for integration with the BroncoDirectMe extension, facilitating course and major requirement management.
