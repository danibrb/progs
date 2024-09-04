#! all

def arithmetic_arranger(problems, show_answers=False):
    numbers_of_problems = len(problems)
    print(numbers_of_problems)
    problem_list = [problem.split() for problem in problems]
    print(problem_list)
    """ prob = problems[0]
    probl = prob.split()
    print(probl)
    plen = [len(s) for s in probl]
    print(plen)
    st = (' '*(plen[2] - plen[0] + 2) + probl[0] + '\n' + probl[1] + ' ' + probl[2] + '\n' + '-'*(plen[2] + 2))
    print(st) """
    
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')