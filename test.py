import datastore
import time
import threading

data = datastore.Data()



def test_create(key, value) :
    return data.create(key, value)

def test_delete(key) :
    return data.delete(key)

def test_read(key) :
    return data.read(key)



t1 = threading.Thread(target = test_create, args=(1, {'name':'safwan'}))
t2 = threading.Thread(target = test_create, args=(2, {'name':'nauman'}))
t3 = threading.Thread(target = test_create, args=(3, {'name':'mohit'}))

t1.start()
t2.start()
t3.start()

# print(test_create(6, {'name':4}))

# time.sleep(10)

# print(test_create(1, {'name':'ahay'}))
# print(test_create(2, {'name':'ahay'}))
# print(test_create(3, {'name':'ahay'}))


# print(test_read(2))

# print(test_delete(5))
# print(test_delete(3))


# print(test_read(6))

# print(test_delete(2))





