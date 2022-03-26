class PID:
    def __init__(self, setValue):
        self.setValue = setValue

    def P(self, P, constanteP):
        manipulatedVariable = constanteP*(self.setValue-P)
        return manipulatedVariable

    def PI(self, P, I, constanteP):
        pass

