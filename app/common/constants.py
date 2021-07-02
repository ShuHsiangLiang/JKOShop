from enum import Enum


class Message(Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    UNKNOWN_USER = " unknown use"
    EXISTING_USER = "user already existing"
    NOT_FOUND = "not found"
