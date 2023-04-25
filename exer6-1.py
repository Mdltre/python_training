def mtable (*args):
    if len(args)<1:
        raise ValueError("Provide one or two arguments!")
    elif len(args) > 2:
        raise ValueError("Provide one or two arguments!")
    elif len(args)==1:
        cols = args[0] 
        rows = cols  
    else:
        cols = args[0] 
        rows = args[1] 
    for i in range(1, rows+1):
            row = []
            for j in range(1, cols+1):
                row.append(i*j)
    
            print(row) 
       
mtable(4,5)
