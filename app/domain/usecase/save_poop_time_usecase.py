import domain.gateway.persistence_gateway as persistence_gateway

def save_poop_time():
    return persistence_gateway.PersistenceGateway().save_poop_times()
