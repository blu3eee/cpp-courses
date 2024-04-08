import pandas as pd
from pandas import DataFrame

from typing import List

class MajorInfo:
    def __init__(self, name, units):
        self.name = name
        self.units = units

        self.major_required: int | None = None
        self.major_electives: int | None = None
        self.certificate_required: int | None = None
        self.option_required: int | None = None
        self.specialization: int | None = None
        self.dissertation_seminar: int | None = None
        self.dissertation: int | None = None
        self.culminating_experience: int | None = None
        self.professional_practice_requirement: str | None = None
        self.general_standing: int | None = None
        self.credential_required: int | None = None

        self.note: str = None

    def __repr__(self):
        return f"MajorInfo(name={self.name}, units={self.units}"

def extract_major_info(df: DataFrame):
    major_dicts = {}
    for row in df.itertuples(index=False):
        major_name = row._0
        requirements_row = row.Requirements
        
        try:
            # Split the major_name by ':' to separate units from the rest
            parts = major_name.split(":")
            major = parts[0].strip()
            units = parts[-1].strip() if len(parts) > 1 else None
            
            # Create a MajorInfo object with major, units, and requirements
            major_dicts[major] = {
                "name": major,
                "units": units
            }
            if str(requirements_row) != 'nan':
                requirements = str(requirements_row).split(',')
                for requirement in requirements:
                    if ':' in requirement:
                        req_type, req_units = str(requirement).split(':')
                        major_dicts[major].update({req_type.strip(): req_units.strip()})
                    else:
                        major_dicts[major].update({'notes': requirement})
        except Exception as e:
            # print(e)
            print(requirements_row)
            break
        
    # Export dictionaries to JSON
    import json
    with open('./CourseCurriculum/requirements_2023-2024.json', 'w') as f:
        json.dump(major_dicts, f, indent=4)
    
    
    return major_dicts

# Load the CSV file
df = pd.read_csv("./CourseCurriculum/2023-2024_Requirements.csv")

extract_major_info(df)
