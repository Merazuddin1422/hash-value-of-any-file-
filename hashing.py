import hashlib
import sys

def calculate_hash(file_path, algorithm):
    hash_object = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    
    return hash_object.hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        return
    
    file_path = sys.argv[1]
    
    algorithms = ['md5', 'sha1', 'sha256', 'md4', 'sha512']
    
    for algorithm in algorithms:
        hash_value = calculate_hash(file_path, algorithm)
        print(f"{algorithm.upper()}: {hash_value}")

if __name__ == '__main__':
    main()
pcap
