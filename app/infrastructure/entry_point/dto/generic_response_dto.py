class GenericResponseDto:
    """
    Generic response DTO.
    """

    def __init__(self, data: dict, status_code):
        """
        Initializes a new instance of the `GenericResponseDto` class.

        Args:
            data (dict): The data to be returned in the response.
        """
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        """
        Converts the `GenericResponseDto` object to a dictionary.

        Returns:
            dict: A dictionary representation of the `GenericResponseDto` object.
        """
        return {
            "status_code": self.status_code,
            "data": self.data
        }
