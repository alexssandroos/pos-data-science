from mrjob.job import MRJob 
class MRMarketBasketAnalysis(MRJob):
    def generate_combinations(self, items):
        result = []
        
        items.sort()
        
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                a = items[i]
                b = items[j]
                result.append((a, b))
        return result

    def mapper(self, key, line):
        items = line.split(',')
        
        combinations = self.generate_combinations(items)
        
        for combination in combinations:
            yield combination, 1
    
    def combine(self, key, values): 
        yield key , sum(values)
        
    def reducer(self, key, values):
        yield key , sum(values)
        
if __name__ == '__main__':
    MRMarketBasketAnalysis.run()