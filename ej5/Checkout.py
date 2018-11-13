import numpy
import simpy

max_queue_size = 0
actual_server = 0
cashier = 0
round_robin = True

class Checkout(object):
    def __init__(self, env, count, arg):
        self.env = env
        self.count = count
        self.cashiers = [simpy.Resource(env) for x in range(count)]
        round_robin = bool(arg)
    def serve(self, request):
        global cashier
        global round_robin
        if ( round_robin ):
            cashier = self.select_cashier_round_robin()
        else:
            cashier = self.select_cashier()
			
        with cashier.request() as req:
            yield req
            yield self.env.timeout(request.get_pay_duration())

    def select_cashier(self):
        queues = []
		
        for x in self.cashiers:
            #x = self.cashiers[i]
            if (x.count == 0) and (len(x.queue) == 0):
               # print('Queue number: %d' % x)
               # print('Queue size: %d' % len((self.cashiers[x]).queue))
                return x
            else:
                queues.append(len(x.queue))
               # print('Queue number: %d' % x)
               # print('Queue size: %d' % len(self.cashiers[x].queue))
                global max_queue_size            
                max_queue_size = max(max_queue_size, len(x.queue))
				
        return self.cashiers[numpy.array(queues).argmin()]

    def get_max_queue_size(self):
        return max_queue_size

    def get_cashier(self):
	    return cashier

    def select_cashier_round_robin(self):
        global actual_server
        
        cashier_to_return = self.cashiers[actual_server]
        actual_server += 1;
        if ( actual_server > 4 ):
            actual_server = 0
			
        #print('Queue number: %d' % actual_server)
        #print('Queue size: %d' % len(cashier_to_return.queue))
        global max_queue_size            
        max_queue_size = max(max_queue_size, len(cashier_to_return.queue))
        return cashier_to_return
