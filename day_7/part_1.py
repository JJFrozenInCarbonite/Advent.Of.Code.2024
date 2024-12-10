import itertools

source = 'day_7\\input.txt'
    
def getAnswer(line) -> int:
    return int(line.split(': ')[0])

def getTerms(line) -> list[int]:
    terms = line.split(': ')[1].split(' ') 
    return [int(term) for term in terms]

def execute(operation, terms):
    result = terms[0]
    print(terms[0], end=' ')
    for i, term in enumerate(terms[1:]):
        print(operation[i], end=' ')
        print(term, end=' ')
        if operation[i] == '*':
            result *= term
        elif operation[i] == '+':
            result += term
        else:
            print("Impossible:", operation[i])
            exit(1)
    print(result)
    return result
    

        
        

if __name__ == '__main__':
    operators = ['*', '+']
    data = open(source).read()
    result = 0
    for line in data.split('\n'):
        answer = getAnswer(line)
        terms = getTerms(line)
        operations = list(itertools.product(operators, repeat=len(terms) - 1))
        
        for operation in operations:
            print(answer, end = ' ')

            if answer == execute(operation, terms):
                result += answer
                break
    print(result)