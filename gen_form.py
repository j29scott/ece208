import random
def gen_form(depth = None, max_depth=10,num_literals=5):
    if random.random() < 0.2 or depth == max_depth:
        neg = random.random() > 0.5
        lit = random.randint(1,num_literals)
        if neg:
            return "(-" + str(lit) + ")"
        else:
            return str(lit) 
    else:
        d = depth
        if d == None:
            d = 0
        op = random.choice(['+','.'])
        if d != 0:
            return '(' + gen_form(d+1,max_depth,num_literals) + ' ' + op + ' ' + gen_form(d+1,max_depth,num_literals) + ')'
        else:
            return '(' + gen_form(d+1,max_depth,num_literals) + ' ' + op + ' ' + gen_form(d+1,max_depth,num_literals) + ')'



if __name__ == "__main__":
    for i in range(10):
        print(gen_form())