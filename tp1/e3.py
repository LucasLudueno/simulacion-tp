# import statistics 
# import seaborn as sns
# import math
# def gcl(X, times, numbers):
# 	for x in range(0, times):
# 		a = 1013904223
# 		c = 1664525 
# 		m = 2**32
# 		rand = (a*X + c) % m
# 		numbers.append(rand)
# 		X=rand
	
# numbers=list()
# gcl(int((93081+95475)/2), 6, numbers)
# print(numbers)

# num=list()
# gcl(int((93081+95475)/2), 100000, num)
# newList = [x / float(2**32) for x in num]

# sns.set_style('darkgrid')

# lamb = 1/float(15)
# newInvList = [-1*math.log(1-x)/lamb for x in newList]

# total = 0

# list2 = []

# for x in range(len(newList)):
#     total += newList[x]
#     list2.append(x)

# def accumu(lis):
#     tot = 0
#     for x in range(len(lis)):
#         tot += lis[x]
#         yield tot
       
# acumPre = [x / float(total) for x in newList]
# acumulada = list(accumu(acumPre))

# #f = interpolate.interp1d(list2,acumulada)
# #y=f(acumulada)
# nuevaAc = []
# indice = []

# for x in range(0,100000,100):
#     nuevaAc.append(acumulada[x])
#     indice.append(x)
    
# print "la mediana es: ",statistics.median(acumulada)
# print("la varianza es % s" 
#       %(statistics.variance(acumulada))) 
# sns.distplot(indice,nuevaAc)
