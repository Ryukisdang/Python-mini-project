import unittest
import cap
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text="tassang"
        result=cap.cap_first_letter(text)
        self.assertEqual(result,"Tassang")
    def test_more_than_two_words(self):
        text="hage tassang"
        result=cap.cap_first_letter_of_group_of_words(text)
        self.assertEqual(result,"Hage Tassang")
if __name__ =="__main__":
    unittest.main()
    
    
