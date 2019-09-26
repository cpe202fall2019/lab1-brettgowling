import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests a list of type None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty(self):
        """Tests an empty list"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter_norm(self):
        """Tests potential lists"""
        alist = [1, 2, 3]
        blist = [2, 3, 1]
        clist = [3, 2, 1]
        dlist = [-1, 0, 1]
        elist = [1, -1, 0]
        flist = [1, 1, 1]
        glist = [0, 0, 0]
        self.assertEqual(max_list_iter(alist), 3)
        self.assertEqual(max_list_iter(blist), 3)
        self.assertEqual(max_list_iter(clist), 3)
        self.assertEqual(max_list_iter(dlist), 1)
        self.assertEqual(max_list_iter(elist), 1)
        self.assertEqual(max_list_iter(flist), 1)
        self.assertEqual(max_list_iter(glist), 0)



    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([2, 4, 6, 8, 10]),[10, 8, 6, 4, 2])
        self.assertEqual(reverse_rec([1, 2]),[2,1])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([1]), [1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
