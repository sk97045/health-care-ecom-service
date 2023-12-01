import json
from typing import Any
from fastapi import Response
from bson import ObjectId

"""
Custom handler to convert ObjectIds to String.
"""
def default(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError

"""
Custom class to auto handle ObjectIDs
"""
class OK(Response):
    media_type = "application/json"

    def __init__(self, content: Any = None):
        super().__init__(content, 200)

    def render(self, content) -> bytes:
        # This method is called when using custom serialisers.
        return json.dumps(content, default=default)