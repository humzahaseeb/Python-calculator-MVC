from model import Model
from view import View



class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def main(self):
        print("in the main of the controller")

if __name__ == '__main__':
    Calculator = Controller()
    Calculator.main()
