from argparse import ArgumentTypeError
import unittest

import app.cli

class TestCLIMethods(unittest.TestCase):

  """
    positive_int test cases
  """

  def test_positive_int_should_be_invalid_when_input_is_a_negative_number(self):
    value_input = -10
    with self.assertRaises(ArgumentTypeError) as context:
      app.cli.positive_int(value_input)
    self.assertEqual("should be > 0", str(context.exception))

  def test_positive_int_should_be_invalid_when_input_is_a_alpha_string(self):
    value_input = "asd"
    with self.assertRaises(ArgumentTypeError) as context:
      app.cli.positive_int(value_input)
    self.assertEqual("should be numeric", str(context.exception))

  def test_positive_int_should_be_valid_when_input_is_a_number(self):
    value_input = 10
    case = app.cli.positive_int(value_input)
    self.assertEqual(10, case)

  def test_positive_int_should_be_valid_when_input_is_not_a_numeric_string(self):
    value_input = "10"
    case = app.cli.positive_int(value_input)
    self.assertEqual(10, case)


  """
    port_int test cases
  """

  def test_port_int_should_be_invalid_when_input_is_out_of_port_range(self):
    value_input_a = 99999
    value_input_b = 0
    with self.assertRaises(ArgumentTypeError) as context_a:
      app.cli.port_int(value_input_a)
    self.assertEqual("should be between 1... 65535", str(context_a.exception))

    with self.assertRaises(ArgumentTypeError) as context_b:
      app.cli.port_int(value_input_b)
    self.assertEqual("should be between 1... 65535", str(context_b.exception))

  def test_port_int_should_be_invalid_when_input_is_not_a_numeric_string(self):
    value_input = "asv"
    with self.assertRaises(ArgumentTypeError) as context:
      app.cli.port_int(value_input)
    self.assertEqual("should be numeric", str(context.exception))

  def test_port_int_should_be_valid_when_input_is_a_numeric_string(self):
    value_input = "10"
    result = app.cli.port_int(value_input)
    self.assertEqual(10, result)

  def test_port_int_should_be_valid_when_input_is_a_numeric(self):
    value_input = 1000
    result = app.cli.port_int(value_input)
    self.assertEqual(1000, result)


if __name__ == '__main__':
    unittest.main()