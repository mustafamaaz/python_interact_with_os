#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

  def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()



# White box test ,the test creator knows how the code works and can write test cases that use the understanding to make sure the everything is performing 
# way its expected to 

# black box test the tester does not know the internal of how the software works 

# unit test can be neither black or white box test 



# this is in jupyter test case we pass arguments  

# class TestCompiler2(unittest.TestCase):
    
#     def test_two(self):
#         testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
#         expected = ['b', 'c']
#         self.assertEqual(LetterCompiler(testcase), expected)

# # EDGE CASES HERE

# unittest.main(argv = ['first-arg-is-ignored'], exit = False)