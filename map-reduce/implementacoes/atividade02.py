from mrjob.job import MRJob 


class MRSocialNetworkFriends(MRJob):
    def mapper(self, _, line):
        (codigo, nome, idade,amigos) = line.split(",")
        yield idade, float(amigos)
    
    def reducer(self, idade, amigos):
        lista_amigos = list(amigos)
        yield idade, round(sum(lista_amigos) / len(lista_amigos) ,2)
        

if __name__ == '__main__':
    MRSocialNetworkFriends.run()