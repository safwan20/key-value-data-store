import unittest
import datastore
import threading
import time

class TestDataStore(unittest.TestCase) :
    
    @classmethod
    def setUpClass(cls):
        cls.data = datastore.Data('datastore') 

    def test_create(self) :
        print('test_create')

        '''
        1. test the create method.

        '''

        self.assertEqual(
            self.data.create(1, {'name':'abc'}), 
            '1'
        )
        self.assertEqual(
            self.data.create(1, {'name':'xyz'}), 
            '1'
        )
        self.assertEqual(
            self.data.create(2, {'name':'pqr'}), 
            '2'
        )

    def test_read(self) :
        print('test_read')


        '''
        test the read method 

        1. error occur if the time expire to read the key.
        2. error occur when key is not present in the store.
        3. else returns the value based on key.

        *Note : time is taken 5 secs for testing purpose.

        '''

        self.assertRaises(
            Exception, 
            self.data.read, 
            8
        )

        self.assertEqual(
            self.data.read(1),
            {'name':'xyz'}
        )

        time.sleep(20)

        self.assertRaises(
            Exception, 
            self.data.read, 
            1
        )



    def test_delete(self) :
        print('test_delete')

        '''
        test the delete method 

        1. error occur if the time expire to read the key.
        2. error occur when key is not present in the store.
        3. else returns the key once deleted.

        '''

        self.assertRaises(
            Exception, 
            self.data.delete, 
            9
        )

        self.assertEqual(
            self.data.delete(2),
            '2'
        )


        time.sleep(10)

        self.assertRaises(
            Exception, 
            self.data.delete, 
            2
        )


    def test_threading(self) :
        '''
        test the multhreading methods in multithreading enviornment. 
        
        '''

        t1 = threading.Thread(target = self.data.create, args=(11, {'name':'lop'}))
        t2 = threading.Thread(target = self.data.create, args=(21, {'name':'mnn'}))
        t3 = threading.Thread(target = self.data.create, args=(35, {'name':'eez'}))

        t1.start()
        t2.start()
        t3.start()



if __name__ == '__main__' :
    unittest.main()