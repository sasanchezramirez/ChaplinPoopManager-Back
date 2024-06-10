import infrastructure.driven_adapter.persistance.service.persistence as persistence

class PersistenceGateway:
    def __init__(self):
        self.persistence = persistence

    def save_poop_times(self):
        return self.persistence.save_poop_times()