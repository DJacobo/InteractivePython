# Superclass, BinaryGate, and UnaryGate are children
# AndGate Is-A Binary Gate, Is-A LogicGate
class LogicGate:
    def __init__(self, lab='LogicGate'):
        self.label = lab
        # print('Created Gate: %s' % self.label)
        self.output = None

    def getLabel(self):
        return str(self.label)

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
    def performGateLogic(self):
        raise('LogicGate superclass does not perform logic')

# ==================================================
class BinaryGate(LogicGate):
    def __init__(self, lab='BinaryGate'):
        LogicGate.__init__(self, lab) # super(BinaryGate,self).__init__(n).
        
        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            return int(input('Please enter Pin A input for gate %s: ' % self.getLabel()))
        elif self.pinA == 0 or self.pinA == 1:
            return self.pinA
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB == None:
            return int(input('Please enter Pin B input for gate %s: ' % self.getLabel()))
        elif self.pinB == 0 or self.pinB == 1:
            return self.pinB
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('No available pins')

# ==================================================
class AndGate(BinaryGate):
    def __init__(self, lab='AndGate'):
        BinaryGate.__init__(self, lab)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # print('result for gate %s: %s' % (self.label, a==1 and b==1))
        if a == 1 and b == 1:
            return 1
        else:
            return 0

# ===========================================
class OrGate(BinaryGate):
    def __init__(self, lab='OrGate'):
        BinaryGate.__init__(self, lab)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # print('result for gate %s: %s' % (self.label, a==1 or b==1))
        if a == 1 or b == 1:
            return 1
        else:
            return 0

# ==================================================    
class NandGate(BinaryGate):
    def __init__(self, lab='NandGate'):
        BinaryGate.__init__(self, lab)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # print('result for gate %s: %s' % (self.label, a==0 or b==0))
        if a == 0 or b == 0:
            return 1
        else:
            return 0

# ==================================================
class NorGate(BinaryGate):
    def __init__(self, lab='NorGate'):
        BinaryGate.__init__(self, lab)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # print('result for gate %s: %s' % (self.label, a==0 and b==0))
        if a == 0 and b == 0:
            return 1
        else:
            return 0

# ==================================================
class XorGate(BinaryGate):
    def __init__(self, lab='XorGate'):
        BinaryGate.__init__(self, lab)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        # print('result for gate %s: %s' % (self.label, a!=b))
        if a != b:
            return 1
        else:
            return 0

# ==================================================
class UnaryGate(LogicGate):
    def __init__(self, lab='UnaryGate'):
        LogicGate.__init__(self, lab) # super(UnaryGate,self).__init__(n).

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input('Please enter Pin B input for gate %s: ' % self.getLabel()))
        elif self.pin == 0 or self.pin == 1:
            return self.pin
        else:
            return self.pin

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source.getFrom().getOutput()
        else:
            raise RuntimeError('No pin Available')

# =======================================
class NotGate(UnaryGate):
    def __init__(self, lab='NotGate'):
        UnaryGate.__init__(self, lab)

    def performGateLogic(self):
        a = self.getPin()
        # print('result for gate %s: %s' % (self.label, not a))
        if a == 0:
            return 1
        else:
            return 0
        
# ================================================