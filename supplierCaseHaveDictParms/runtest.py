import unittest

test_dir="./testCaseHaveDictParms"

discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_0*.py")
# discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_01_SsoLogin.py")



if __name__ == "__main__":
    runer=unittest.TextTestRunner()
    runer.run(discover)