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
        self.assertEqual(max_list_iter(tlist), None) #Tests output for an empty list

    def test_max_list_iter_norm(self):
        """Tests potential lists"""
        alist = [1, 2, 3] #Various combinations
        blist = [2, 3, 1]
        clist = [3, 2, 1]
        dlist = [-1, 0, 1] #negatives involved
        elist = [1, -1, 0]
        flist = [1, 1, 1] #all the same num
        glist = [0, 0, 0]
        self.assertEqual(max_list_iter(alist), 3)
        self.assertEqual(max_list_iter(blist), 3)
        self.assertEqual(max_list_iter(clist), 3)
        self.assertEqual(max_list_iter(dlist), 1)
        self.assertEqual(max_list_iter(elist), 1)
        self.assertEqual(max_list_iter(flist), 1)
        self.assertEqual(max_list_iter(glist), 0)



    def test_reverse_rec(self):
        """Tests to see if list is reversed using recursion"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([2, 4, 6, 8, 10]),[10, 8, 6, 4, 2]) #larger list
        self.assertEqual(reverse_rec([1, 2]),[2,1]) #list size 2
        self.assertEqual(reverse_rec([]), []) #empty lists
        self.assertEqual(reverse_rec([1]), [1]) #list size 1

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0) #Testing end case
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8) #testing other end
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7) #testing middle-ish number
        self.assertEqual(bin_search(9, 0, 3, list_val), None) #Testing it outside index
        self.assertEqual(bin_search(1, 2, 4, list_val), None)
        self.assertEqual(bin_search(3, 3, 3, list_val), 3) #Testing for the same number
        self.assertEqual(bin_search(4, 3, 4, list_val), 4) #Testing for small index range
        list_empty = []
        self.assertEqual(bin_search(4, 0, len(list_empty)-1, list_empty), None) #Testing empty list

if __name__ == "__main__":
        unittest.main()

    
