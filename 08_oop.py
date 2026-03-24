class Pintu:
    def __init__(self, state):
        self.state = state

    def buka(self):
        self.state = "terbuka"

p = Pintu("tertutup")
p.buka()
print(p.state)
