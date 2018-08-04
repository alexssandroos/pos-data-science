from mrjob.job import MRJob 


class MRTemperature(MRJob):
    def mapper(self, _, line):
        if not 'PRCP' in line :
            (codigo, tempo, tipo_dado, valor, _, _, _, _) = line.split(",")
            yield tempo, float(valor)
    
    def reducer(self, tempo, valor):
        lista_amigos = list(valor)
        yield tempo, ' MIN %s - MAX %s - OCORRENCIAS %s '% (min(lista_amigos) ,max(lista_amigos), len(lista_amigos) )
        

if __name__ == '__main__':
    MRTemperature.run()

