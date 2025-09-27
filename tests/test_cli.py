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

  """
    host_type test cases
  """

  def test_host_type_should_be_invalid_when_input_is_invalid_ip(self):
    value_input = "10.10"
    with self.assertRaises(ArgumentTypeError) as context:
      app.cli.host_type(value_input)
    self.assertEqual("should be literal valid ip or hostname", str(context.exception))

  def test_host_type_should_be_valid_when_input_is_a_literal_ip(self):
    value_input = "127.0.0.1"
    result = app.cli.host_type(value_input)
    self.assertEqual("127.0.0.1", result)

  def test_host_type_should_be_valid_when_input_is_a_hostname(self):
    value_input_a = "http://localhost:8000"
    value_input_b = "https://localhost:8000"
    result_a = app.cli.host_type(value_input_a)
    result_b = app.cli.host_type(value_input_b)
    self.assertEqual("http://localhost:8000", result_a)
    self.assertEqual("https://localhost:8000", result_b)

if __name__ == '__main__':
    unittest.main()