import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test("3",
                     lambda: pinghviny(),
                     lambda out_text: self.assertEqual(out_text, '''   _~_       _~_       _~_    
  (o o)     (o o)     (o o)   
 /  V  \   /  V  \   /  V  \  
/(  _  )\ /(  _  )\ /(  _  )\ 
  ^^ ^^     ^^ ^^     ^^ ^^   '''))

    def test_2(self):
        console_test("1",
                     lambda: pinghviny(),
                     lambda out_text: self.assertEqual(out_text, '''   _~_    
  (o o)   
 /  V  \  
/(  _  )\ 
  ^^ ^^   '''))


if __name__ == '__main__':
    unittest.main()
