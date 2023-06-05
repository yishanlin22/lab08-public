# CarInventory.py

from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    
    def __init__(self):
        self.root = None
        self.totalPrice = 0

    def addCar(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
            self.totalPrice += car.price
        else: 
            self._put(car, self.root)

    def _put(self, car, currentNode):
        if car.make == currentNode.getMake() and car.model == currentNode.getModel():
            currentNode.cars.append(car)
            self.totalPrice += car.price
        elif car < currentNode.cars[0]:
            if currentNode.getLeft() is not None:
                self._put(car, currentNode.left)
            else:
                currentNode.setLeft(CarInventoryNode(car))
                self.totalPrice += car.price
        else:
            if currentNode.getRight() is not None:
                self._put(car, currentNode.right)
            else:
                currentNode.setRight(CarInventoryNode(car))
                self.totalPrice += car.price

    
    def doesCarExist(self, car):
        if self.root:
            res = self._get(car, self.root)
            if res:
                return True
            else:
                return False
        else:
            return False

    def _get(self, car, currentNode):
        if not currentNode:
            return False
        elif car.make == currentNode.getMake() and car.model == currentNode.getModel():
            return car in currentNode.cars
        elif car < currentNode.cars[0]:
            return self._get(car, currentNode.left)
        else:
            return self._get(car, currentNode.right)

    def inOrder(self):
        ret = ""
        if self.root:
            ret += self._inOrder(self.root)
        return ret

    def _inOrder(self, currentNode):
        ret = ""
        if currentNode.left:
            ret += self._inOrder(currentNode.left)
        ret += str(currentNode)
        if currentNode.right:
            ret += self._inOrder(currentNode.right)
        return ret

    def preOrder(self):
        ret = ""
        if self.root:
            ret += self._preOrder(self.root)
        return ret
    
    def _preOrder(self, currentNode):
        ret = ""
        ret += str(currentNode)
        if currentNode.left:
            ret += self._preOrder(currentNode.left)
        if currentNode.right:
            ret += self._preOrder(currentNode.right)
        return ret

    def postOrder(self):
        ret = ""
        if self.root:
            ret += self._postOrder(self.root)
        return ret
    
    def _postOrder(self, currentNode):
        ret = ""
        if currentNode.left:
            ret += self._postOrder(currentNode.left)
        if currentNode.right:
            ret += self._postOrder(currentNode.right)
        ret += str(currentNode)
        return ret

    def getBestCar(self, make, model):
        if make is None or model is None:
            return None
        else:
            make = make.upper()
            model = model.upper()
            if self.root:
                CarNode = self.searchCar(make, model, self.root)
                if CarNode:
                    best = CarNode.cars[0]
                    for i in CarNode.cars:
                        if i > best:
                            best = i
                    return best
            return None

    def getWorstCar(self, make, model):
        if make is None or model is None:
            return None
        else:
            make = make.upper()
            model = model.upper()
            if self.root:
                CarNode = self.searchCar(make, model, self.root)
                if CarNode:
                    worst = CarNode.cars[0]
                    for i in CarNode.cars:
                        if i < worst:
                            worst = i
                    return worst
            return None


    def searchCar(self, make, model, currentNode):
        if make is None or model is None:
            return None
        if not currentNode:
            return None
        elif make == currentNode.getMake() and model == currentNode.getModel():
            return currentNode
        elif make < currentNode.getMake() or (make == currentNode.getMake() and model < currentNode.getModel()):
            return self.searchCar(make, model, currentNode.left)
        else:
            return self.searchCar(make, model, currentNode.right)
        
    def getTotalInventoryPrice(self):
        return self.totalPrice
