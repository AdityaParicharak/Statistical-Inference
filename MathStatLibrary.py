

class math_N_stat():

    def sqRT(num):
        val = (num)**(1/2)
        return val
    
    def Sum_Data_values(data):
        x = len(data)
        sum = 0
        for val in range(x):
            add = data[val]
            sum += add
        return sum
    
    def mean(data):
         size = len(data)
         sum_val = math_N_stat.Sum_Data_values(data)
         xBar = sum_val / size
         return xBar
    
    def variance(data):
         size = len(data)
         numerator = 0
         xBar = math_N_stat.mean(data)
         for x in range(size):
             xi_minus_xBar_sq = (data[x] - xBar) ** 2
             numerator += xi_minus_xBar_sq 
         var = numerator / (size - 1)
         return var
    
    def standardDeviation(data):
         s_sqared = math_N_stat.variance(data)
         s = s_sqared ** (1/2)
         return s
    

    





             
    

