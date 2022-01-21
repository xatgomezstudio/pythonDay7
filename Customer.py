class Customer:
    def __init__(self, name, age, purchaseAmount):
        self.name = name
        self.age = age
        self.purchaseAmount = purchaseAmount

    def got_reward_points(self):
        if self.purchaseAmount >= 25:
            return True
        else:
            return False