import unittest
from unittest.mock import patch, mock_open
import main  # main.py must be in the root directory

class TestSaveLines(unittest.TestCase):

    @patch('builtins.input', return_value='output.txt')
    def test_save_lines(self, mock_input):
        lines = ['Hello world\n']
        m = mock_open()
        with patch('main.open', m):
            main.saveLines(lines)
            m.assert_called_once_with('output.txt', 'w', encoding='UTF-8')
            m().writelines.assert_called_once_with(lines)

if __name__ == '__main__':
    unittest.main()
