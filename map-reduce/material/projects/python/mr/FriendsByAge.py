from mrjob.job import MRJob

class MRFriendsByAge(MRJob):
    def mapper(self, _, line):
        (ID, name, age, numberOfFriends) = line.split(',')

        yield age, float(numberOfFriends)
        
    def reducer(self, age, values):
        total = 0
        numberOfElements = 0

        for x in values:
            total += x
            numberOfElements += 1

        yield age, total / numberOfElements

if __name__ == '__main__':
    MRFriendsByAge.run()