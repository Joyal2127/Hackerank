if __name__ == '__main__':
    n = int(input())  # Number of elements in the tuple
    integer_list = map(int, input().split())  # Space-separated integers
    
    # Create a tuple from the input integers
    t = tuple(integer_list)
    
    # Compute the hash value of the tuple
    result = hash(t)
    
    # Print the result
    print(result)
