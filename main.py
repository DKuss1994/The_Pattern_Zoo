#Singelton
import animals


class TierFactory:
    def create_tier (art, name, weight):
        if art == "Löwe":
            pass



tier = TierFactory.create_tier("Löwe", "Simba", 200)