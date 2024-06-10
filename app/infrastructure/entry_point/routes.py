import logging
from fastapi import APIRouter
from infrastructure.entry_point.handler.save_poop_times_handler import save_poop_times_handler

router = APIRouter()

@router.get("/poop-times", description="Get how many times Chaplin went to the bathroom")
async def save_poop_times():
        """
        Endpoint to get the number of times Chaplin went to the bathroom.

        This function wraps the `get_poop_times_handler` function from the `chaplin` module.

        Returns:
            dict: JSON object with the details of chaplin's poop times.
        """
        logging.info("Calling save_poop_times endpoint")
        return save_poop_times_handler()
