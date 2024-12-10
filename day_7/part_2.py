from datetime import datetime, timedelta
import time
import pytz
import itertools

source = 'day_7\\input.txt'
    
def getAnswer(line) -> int:
    return int(line.split(': ')[0])

def getTerms(line) -> list[int]:
    terms = line.split(': ')[1].split(' ') 
    return [int(term) for term in terms]

def execute(operation, terms):
    result = terms[0]
    for i, term in enumerate(terms[1:]):
        if operation[i] == '*':
            result *= term
        elif operation[i] == '+':
            result += term
        elif operation[i] == '||':
            result = int(str(result) + str(term))
        else:
            print("Impossible:", operation[i])
            exit(1)
    return result
    

if __name__ == '__main__':
    operators = ['*', '+', '||']
    data = open(source).read()
    total_result = 0
    for j, line in enumerate(data.split('\n')):
        print(f"{j}) Evaluating Line:", line)
        start= datetime.now()
        answer = getAnswer(line)
        terms = getTerms(line)
        operations = list(itertools.product(operators, repeat=len(terms) - 1))
        for i, operation in enumerate(operations):
            result = execute(operation, terms)
            if answer == result:
                total_result += result
                break
        print("  Done. Total Time:", datetime.now() - start)
    print(total_result)
    
        

    
    
        
            
        
        
    
        #for i in range(0, len(terms) - 1):
            
    
    """     for i,term in enumerate(terms):
            print(term, end='')
            print(operations)
     """        

    
                
        
        


                


        
            

        

#[[answer], [terms]]
