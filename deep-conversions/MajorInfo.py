from typing import List
class MajorInfo:
    def __init__(self, name, units = None):
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

        self.required_courses: List[str] = []
        self.elective_courses: List[str] = []