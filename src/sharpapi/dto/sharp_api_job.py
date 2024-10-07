from ..enums.sharp_api_job_status_enum import SharpApiJobStatusEnum
from ..enums.sharp_api_job_type_enum import SharpApiJobTypeEnum
import json


class SharpApiJob:
    def __init__(self, id, type, status, result):
        self.id = id
        self.type = type
        self.status = status
        self.result = result

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_status(self):
        return self.status

    def get_result_json(self):
        return json.dumps(self.result, indent=2) if self.result else None

    def get_result_object(self):
        return self.result

