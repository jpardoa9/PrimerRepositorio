class Galleta():

    def __init__(self, nombre, forma):
            self.nombre = nombre
            self.forma = forma

    def hornear(self):
        print('Esta {} ha sido horneada en forma de {}.\n¡Buen provecho!'.format(self.nombre,self.forma))

if __name__=='__main__':
    galleta_1 = Galleta("galleta con chispas de chocolate", "estrella")
    ##galleta_1.hornear()
    print(dir(galleta_1))








