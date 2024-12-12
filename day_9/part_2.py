import os

source =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')     

if __name__ == '__main__':
    data = open(source).read()
    