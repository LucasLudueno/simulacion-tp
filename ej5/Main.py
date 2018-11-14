import random
import simpy
import sys

from Checkout import Checkout
from Request import Request

arrival_rate = 45/1000
server_count = 5
max_wait_time = 0
acum = 0

simulation_time = 10000

def generate_clients(environment, interval, checkout):
    index = 1
    while True:
        request = Request(env)
        environment.process(request.pay(checkout))
        t = random.expovariate(1.0 / interval)
        yield environment.timeout(t)
        global acum
        global max_wait_time
        acum += t
        if len(checkout.get_cashier().queue) == 0:
            max_wait_time = max(max_wait_time, acum)
            acum = 0
        index = index + 1
		
env = simpy.Environment()
if (len(sys.argv)< 2):
    print (' Falta argumento, 1 para round_robin, 0 para menor carga' )
    sys.exit()
if ( sys.argv[1] != '1' and sys.argv[1]!= '0' ):
    print (' Argumento inválido, 1 para round_robin, 0 para menor carga, ingresó: %s' % (sys.argv[1]) )
    sys.exit()
checkout = Checkout(env, server_count, sys.argv[1])
env.process(generate_clients(env, arrival_rate, checkout))
env.run(until=simulation_time)

print ('Max queue size: %d' % checkout.get_max_queue_size())
print ('Max wait time: %s: ' % str(max_wait_time))