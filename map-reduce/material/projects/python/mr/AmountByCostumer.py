from mrjob.job import MRJob


class MRAmoutByCustomer(MRJob):
    def mapper(self, _, line):
        (customer_id, item, amount) = line.split(",")
        yield int(customer_id), float(amount)
    
    def reducer(self, customer_id, amounts):
        yield int(customer_id), sum(amounts)

if __name__ == '__main__':
    MRAmoutByCustomer.run()
