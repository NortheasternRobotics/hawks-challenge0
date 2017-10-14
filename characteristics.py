#store different characteristics of a water bottle and then aggregate the values into a decision
#eventually combine multiple characteristics to determine percent confidence that the object is a water bottle
class Characteristics():

    def __init__(self):
        self.cap = 0    #try to detect a cap
        self.shape = 0  #try to detect a water bottle like shape


    def set_cap(self, cap_value):
        self.cap = cap_value

    def set_shape(self, shape_value):
        self.shape = shape_value



