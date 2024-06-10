import domain.usecase.save_poop_time_usecase as save_poop_time_usecase
import logging
import infrastructure.entry_point.dto.generic_response_dto as generic_response_dto

def save_poop_times_handler():
    logging.info("Calling save_poop_times handler")

    response = save_poop_time_usecase.execute()
    if response:
        status_code = 200
        data = {"response": "Was able to save the poop times"}
    else:
        status_code = 500
        data = {"error": "Internal Server Error"}
    
    response_dto = generic_response_dto.GenericResponseDto(data = data, status_code = status_code)
        
    return response_dto.to_response()
