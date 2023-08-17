from model import ConnectFourNN

import unittest


class MyTestCase(unittest.TestCase):
    @staticmethod
    def NN_test():
        model = ConnectFourNN()
        print(model)


if __name__ == "__main__":
    unittest.main()
