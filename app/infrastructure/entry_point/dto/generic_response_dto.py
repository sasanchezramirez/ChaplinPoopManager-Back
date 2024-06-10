import json
from fastapi import Response
from fastapi.encoders import jsonable_encoder

class GenericResponseDto:
    """
    Generic response DTO.
    """

    def __init__(self, data: dict, status_code: int):
        """
        Initializes a new instance of the `GenericResponseDto` class.

        Args:
            data (dict): The data to be returned in the response.
        """
        self.status_code = status_code
        self.data = data

    def to_response(self) -> Response:
        json_content = json.dumps(jsonable_encoder(self.data))

        return Response(content=json_content, status_code=self.status_code, media_type="application/json")
