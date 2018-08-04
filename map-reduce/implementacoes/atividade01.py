from mrjob.job import MRJob 


class MRValuesOfOrders(MRJob):
    def mapper(self, _, line):
        (customer, item, order_value) = line.split(",")
        yield int(customer), float(order_value)
    
    def reducer(self, customer, order_value):
        yield int(customer), sum(order_value)


if __name__ == '__main__':
    MRValuesOfOrders.run()
