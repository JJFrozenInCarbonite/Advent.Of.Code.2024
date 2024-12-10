import copy
import itertools

source = 'day_7\\input.txt'

def get_operations(operators, terms):
    transactions = []
    operations = []
    equations = []
    for operator in operators:
        for term in terms[:-1]:
            operations.append(operator)    
    for i in range(0, len(terms) - 1):
        transaction = copy.deepcopy(operations)
        if i > 0:
            temp = transaction.pop(0)
            transaction.append(temp)    
        transactions.append(transaction)    
    operations = []
    for j in range(0, len(transactions[0])):
        operation = []
        for i in range(0, len(transactions)):
            operation.extend(transactions[i][j])
        operations.append(operation)   
    computations = []
    for i in range(0, len(operations)):
        computation = []
        for j in range(len(operations[0])):
            computation.append(terms[j])
            computation.append(operations[i][j])
        computation.append(terms[-1])

        computations.append(computation)
    print(computations)
    exit()
    return computations
    
def getAnswer(line) -> int:
    return int(line.split(': ')[0])

def getTerms(line) -> list[int]:
    terms = line.split(': ')[1].split(' ') 
    return [int(term) for term in terms]

def getOperations(operators, terms):
    operations = []
    temp = ['+', '+','+', '+','+', '+','+', '+','+', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    for i in range(0, (len(terms) - 1) * len(operators)):
        operation = []
        for j in range(len(terms) - 1, -1):
            

    print(terms)
    print(operations)
    print(len(operations))
    exit()
    

        
        

if __name__ == '__main__':
    operators = ['*', '+']
    data = open(source).read()
    numbers = []
    for line in data.split('\n'):
        answer = getAnswer(line)
        terms = getTerms(line)
        equations = getOperations(operators, terms)
        
        

    
    
        
            
        
        
    
        #for i in range(0, len(terms) - 1):
            
    
    """     for i,term in enumerate(terms):
            print(term, end='')
            print(operations)
     """        

    
                
        
        


                


        
            

        

#[[answer], [terms]]
