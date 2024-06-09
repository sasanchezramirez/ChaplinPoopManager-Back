from fastapi import APIRouter
from app.infrastructure.entry_point.handler.get_poop_times_handler import get_poop_times_handler

router = APIRouter()

@router.get("/poop-times", response_model= dict, description="Get how many times Chaplin went to the bathroom")
async def get_poop_times():
        """
        Endpoint to get the number of times Chaplin went to the bathroom.

        This function wraps the `get_poop_times_handler` function from the `chaplin` module.

        Returns:
            dict: JSON object with the details of chaplin's poop times.
        """
        return get_poop_times_handler()
