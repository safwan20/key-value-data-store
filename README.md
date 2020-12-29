# Key-Value DataStore

### Problem Statement
Create a Key-Value Datastore that supports CRUD operations (create, delete, read).

### Approach 
I have created simple module in which read, create and delete methods are implemented.

### Methods
1. `create` : user can create key and value pair by passing key and value in the method keep in mind the key expiry time is till 15 minutes.
2. `read `:  user can read value by passing key.
3. `delete` : user can delete specific key from store.

### Technical Stack used
1. Python

### Steps to run
1. Create a python3 virtual enviornment and activate it.
2. Install the requirements via `pip install -r requirements.txt`.
3. `import datastore to use the module.`

### Files
1. `datastore.py` : It is the main module.
2. `test_datastore.py` : UnitTest File.