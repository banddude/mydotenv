import subprocess
import os

def test_mydotenv():
    print("\n=== Testing mike package ===\n")
    
    def run_command(args):
        result = subprocess.run(['mike'] + args, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode == 0
    
    # Test 1: List initial variables
    print("Test 1: Listing initial variables")
    run_command([])
    
    # Test 2: Add a variable
    print("\nTest 2: Adding a variable")
    run_command(['TEST_KEY=test_value'])
    
    # Test 3: Read the variable
    print("\nTest 3: Reading the variable")
    run_command(['TEST_KEY'])
    
    # Test 4: List all variables again
    print("\nTest 4: Listing all variables")
    run_command([])
    
    # Test 5: Delete the variable
    print("\nTest 5: Deleting the variable")
    run_command(['delete', 'TEST_KEY'])
    
    # Test 6: List variables after deletion
    print("\nTest 6: Listing variables after deletion")
    run_command([])
    
    # Test 7: Try to read deleted variable
    print("\nTest 7: Trying to read deleted variable")
    run_command(['TEST_KEY'])

if __name__ == '__main__':
    test_mydotenv() 