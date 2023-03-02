from io import StringIO #used to mimic text file input
import answer
import unittest

class TestSolution(unittest.TestCase): 
    def test_solution(self):
        t1 = StringIO('0') #no students
        self.assertEqual(answer.solution(t1),[])

        t2 = StringIO('6 \n 1 S 6 2 \n 1 P 1400 3 \n 1 S 8 8 \n 1 T 101 2 \n 1 P 1345 3 \n 1 P 7654 1') #one student
        self.assertEqual(answer.solution(t2), ['1', 1345, 7654, 7])

        t3 = StringIO('1 \n 1 P 1400 3')#one student & only page
        self.assertEqual(answer.solution(t3),[])

        t4= StringIO('1 \n 1 S 6 2')#one student & only submission
        self.assertEqual(answer.solution(t4),[])

        t5 = StringIO('8 \n 1 P 1400 3 \n 1 S 8 8 \n 1 P 1245 4 \n 1 S 6 2 \n 40 S 400 9 \n 40 P 40 6 \n 40 P 2 8 \n 40 S 6 7') #multiple students
        self.assertEqual(answer.solution(t5), ['40', 2, 2, 203, '1', 1245, 1245, 7])

        t6 = StringIO('8 \n 1 P 1400 3 \n 1 S 8 8 \n 1 P 1245 4 \n 1 S 6 2 \n 40 S 400 9 \n 40 P 40 6 \n 40 P 2 8 \n 40 S 6 7 \n 2 S 20 1') #multiple students w/invlaid student
        self.assertEqual(answer.solution(t6), ['40', 2, 2, 203, '1', 1245, 1245, 7])

        t7 = StringIO('12 \n 1 S 6 2 \n 1 P 1400 3 \n 1 S 8 8 \n 1 T 101 2 \n 1 P 1345 3 \n 1 P 7654 1 \n 5 S 10 2 \n 5 P 1400 3 \n 5 S 90 8 \n 5 T 101 2 \n 6 P 800 3 \n 6 S 700 1 \n 5 P 20 1') #large amount of logs
        self.assertEqual(answer.solution(t7), ['5', 20, 20, 50, '6', 800, 800, 700, '1', 1345, 7654, 7])
                         
if __name__ == '__main__':
    unittest.main()