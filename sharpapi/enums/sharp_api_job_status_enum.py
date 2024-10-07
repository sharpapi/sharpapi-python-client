from enum import Enum


class SharpApiJobStatusEnum(Enum):
    NEW = 'new'
    PENDING = 'pending'
    FAILED = 'failed'
    SUCCESS = 'success'

