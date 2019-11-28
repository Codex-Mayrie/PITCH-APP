import unittest
from models import Pitch

class PitchTest(unittest.TestCase):
  """
  Test Class to test the behavior of the Pitch class
  """
  
  def setUp(self):
    """
    Set up method that will run before every Test
    """
    self.new_pitch = Pitch(1234,'Interview','I love interviews','Mary',12/2/2019)
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_pitch, Pitch))
    