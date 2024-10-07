class JobDescriptionParameters:
    def __init__(
        self,
        name,
        company_name=None,
        minimum_work_experience=None,
        minimum_education=None,
        employment_type=None,
        required_skills=None,
        optional_skills=None,
        country=None,
        remote=None,
        visa_sponsored=None,
        voice_tone=None,
        context=None,
        language=None,
    ):
        self.name = name
        self.company_name = company_name
        self.minimum_work_experience = minimum_work_experience
        self.minimum_education = minimum_education
        self.employment_type = employment_type
        self.required_skills = required_skills
        self.optional_skills = optional_skills
        self.country = country
        self.remote = remote
        self.visa_sponsored = visa_sponsored
        self.voice_tone = voice_tone
        self.context = context
        self.language = language

    def to_dict(self):
        return {
            'name': self.name,
            'company_name': self.company_name,
            'minimum_work_experience': self.minimum_work_experience,
            'minimum_education': self.minimum_education,
            'employment_type': self.employment_type,
            'required_skills': self.required_skills,
            'optional_skills': self.optional_skills,
            'country': self.country,
            'remote': self.remote,
            'visa_sponsored': self.visa_sponsored,
            'voice_tone': self.voice_tone,
            'context': self.context,
            'language': self.language,
        }

