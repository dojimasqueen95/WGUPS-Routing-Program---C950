class HashTable:
    # Creating the constructor
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity = 20):
        # Initializes table with empty bucket list entries
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])
    
    # Citing: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    # Creating the insert method
    def insert(self, key, item):  # Inserts and updates
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Updates key if already in bucket
        for kv in bucket_list: # O(N) time complexity
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # If not in bucket, inserts item at end of bucket list    
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
    
    # Search method
    def search(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None
    
    # Remove method
    def remove(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[slot]

        # If key found in hash table, removes item
        if key in bucket_list:
            destination.remove(key)
