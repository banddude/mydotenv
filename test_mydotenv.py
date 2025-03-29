import mike
import os

def test_mydotenv():
    print("\n=== Testing mydotenv package ===\n")
    
    # Test 1: List initial variables
    print("Test 1: Listing initial variables")
    mike.main()
    
    # Test 2: Add a variable
    print("\nTest 2: Adding a variable")
    mike.main(['TEST_KEY=test_value'])
    
    # Test 3: Read the variable
    print("\nTest 3: Reading the variable")
    mike.main(['TEST_KEY'])
    
    # Test 4: List all variables again
    print("\nTest 4: Listing all variables")
    mike.main()
    
    # Test 5: Delete the variable
    print("\nTest 5: Deleting the variable")
    mike.main(['delete TEST_KEY'])
    
    # Test 6: List variables after deletion
    print("\nTest 6: Listing variables after deletion")
    mike.main()
    
    # Test 7: Try to read deleted variable
    print("\nTest 7: Trying to read deleted variable")
    mike.main(['TEST_KEY'])

if __name__ == '__main__':
    test_mydotenv() 