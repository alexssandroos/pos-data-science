from mrjob.job import MRJob

class MRMinTemperatures(MRJob):
    def mapper(self, _, line):
        (location, date, type, data, x, y, z, w) = line.split(',')

        if (type == 'TMIN'):
            temperature = data
            yield location, temperature
    
    def reducer(self, location, temps):
        yield location, min(temps)

if __name__ == '__main__':
    MRMinTemperatures.run()

