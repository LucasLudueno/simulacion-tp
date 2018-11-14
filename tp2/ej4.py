import random
import simpy
import numpy

simulation_time_1 = 2*3600
simulation_time_2 = 3*3600
simulation_time_3 = 4*3600
arrival_rate_1 = 240
arrival_rate_2 = 120
arrival_rate_3 = 360

max_queue_size = 0
max_wait_time = 0
acum = 0

class Client(object):

    process_duration = {
        '1': 240,
        '2': 120,
        '3': 360
    }

    pay_variance = {
        '1': 180,
        '2': 60,
        '3': 120
    }
    
    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['1', '2', '3'], p=[0.1, 0.7, 0.2])

    def pay(self, atm):
	# Automatic release
        with atm.request() as req:
            yield req
            yield self.env.timeout(self.get_process_duration())

	# Manual release
        # request = atm.request()
        # yield request
        # yield self.env.timeout(self.get_process_duration())
        # atm.release(request)

        #print("%.2f Client type %s attended" % (self.env.now, self.type))

    def get_process_duration(self):
        return self.process_duration[self.type] + numpy.random.uniform(-self.pay_variance[self.type], self.pay_variance[self.type])


def generate_clients(environment, interval):
    atm = simpy.Resource(env, capacity = 1)
    index = 1

    while True:
        print('Client %d' % index)
        print('Queue Size %d' % len(atm.queue))
        global max_queue_size 
        max_queue_size = max(len(atm.queue),max_queue_size)
        client = Client(env)
        environment.process(client.pay(atm))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)
        global max_wait_time
        global acum
        acum += t
        if len(atm.queue) == 0:
            max_wait_time = max(max_wait_time, acum)
            acum = 0
        index = index + 1

env = simpy.Environment()

env.process(generate_clients(env, arrival_rate_1))
env.run(until=simulation_time_1)

env.process(generate_clients(env, arrival_rate_2))
env.run(until=simulation_time_2)

env.process(generate_clients(env, arrival_rate_3))
env.run(until=simulation_time_3)

print ('Max queue size %d' % max_queue_size)

print ('Max wait time %s: ' % str(max_wait_time))