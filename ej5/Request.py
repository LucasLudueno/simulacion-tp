import numpy


class Request(object):

    pay_duration = {
        '1': 120,
        '2': 240,
        '3': 500
    }
    
    pay_variance = {
        '1': 60,
        '2': 120,
        '3': 300
    }
    
    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['1', '2', '3'], p=[0.7, 0.2, 0.1])

    def pay(self, checkout):
        yield self.env.process(checkout.serve(self))
        #print("%.2f Request type %s attended" % (self.env.now, self.type))

    def get_pay_duration(self):
        return self.pay_duration[self.type] + numpy.random.uniform(-self.pay_variance[self.type], self.pay_variance[self.type])
