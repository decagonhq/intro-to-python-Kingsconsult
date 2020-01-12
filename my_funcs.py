import collections

class FirstClass:
    mean = 0.0
    median = 0.0
    mode = 0.0
        
    def calc_mode(self, num):
        data = collections.Counter(num)
        data_list = dict(data)
        
        max_value = max(list(data.values()))
        
        mode_val = [num for num, freq in data_list.items() if freq == max_value]
        if len(mode_val) == len(num):
            print(num)
            return num
        return mode_val
    
    @classmethod
    def calc_median(cls, median):
        sort = sorted(median)
        lent = len(sort)
        if len(sort) % 2 != 0:
            medu = lent // 2
            return sort[medu]
        else:
            med1 = lent // 2
            med2 = (lent // 2 ) - 1
            med = sort[med2] + sort[med1]
            return med / 2
        
    @staticmethod
    def calc_mean(mean):
        return round(sum(mean) / len(mean), 2)
    
    
num =  [1, 3, 4, 2, 8, 1, 3, 3, 1]   
a = FirstClass()
print(a.calc_mode(num))
print(a.calc_median(num))
print(a.calc_mean(num))
