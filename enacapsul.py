class Super:
    x=None
    _y=None
    __z=None
    def __init__(self,x,y,z):
        self.x=x         #public
        self._y=y        #protected
        self.__z=z       #private

    def displayPublicMembers(self):
          print("Public Data Member: ", self.x)
    def _displayProtectedMembers(self):
          print("Protected Data Member: ", self._y)
    def __displayPrivateMembers(self):
          print("Private Data Member: ", self.__z)

    def accessprivatemenmeberfunction(self):
        self.__displayPrivateMembers()

class Sub(Super):
    def __init__(self,x,y,z):
        Super.__init__(self,x,y,z)
    def accessprotedmembers(self):
        self._displayProtectedMembers()

obj= Sub("Gangesh",4, "gaur!")
obj.displayPublicMembers()
obj.accessprotedmembers()
obj.accessprivatemenmeberfunction()
print(obj._y)
# print(obj.__z)
