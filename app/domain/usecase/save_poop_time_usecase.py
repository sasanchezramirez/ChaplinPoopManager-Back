import domain.gateway.persistence_gateway as persistence_gateway
import logging


def execute():
    logging.info("Calling save_poop_time_usecase")

    return persistence_gateway.PersistenceGateway().save_poop_times()
