def rect_mat():
         mat_rect = []
         t=1
         while 0< t:
               entry_rect = input(f'your row{t}: ')
               if entry_rect != 'stop' :
                   row_rect = [float(x) for x in entry_rect.split(',')]
                   if t==1:
                     exp = len(row_rect) 
                   if len(row_rect) == exp :
                       mat_rect.append(row_rect)
                       t += 1
                   else:
                       print('Row size mismatch.')
                       continue                     
               else:
                   break
         return mat_rect
def sq_mat():
    mat_sq = []
    q=1
    ext = 2
    while 0< q<= ext:
            entry_sq = input(f'your row{q} of your square rref: ')
            row_sq = [float(y) for y in entry_sq.split(',')]
            if q==1:
                ext = len(row_sq) 
            if len(row_sq) == ext :
                mat_sq.append(row_sq)
                q += 1
            else:
                print('Row size mismatch!')
                continue             
    return mat_sq
def mat_print(rref):
     print()
     for p in rref:
         for q in p:
             print(q,end='   ')    
         print()
def add_subt_mat():
    num = int(input('How many matrices do you want to enter? '))
    list_matrices = []
    if num<2:
        print('We need altelast two matrices for this function.')
    else:
        for ind in range(num):
            print(f'Enter your number{ind+1} matrix.')
            print("And remember the order of entering matrices. Because they'll be added or subtracted accordingly.")
            list_matrices.append(rect_mat())
    result = list_matrices[0]
    fun = input('Do you want to "add" or "subtract" them ? ')
    fun.lower()
    for o in range(1,num):
        new_matrix = []
        for m in range(len(list_matrices[0])):
            new_row = []
            for n in range(len(list_matrices[0][0])):
                if fun == 'add' :
                    new_row.append(result[m][n] + list_matrices[o][m][n])
                elif fun == 'subtract':
                    new_row.append(result[m][n] - list_matrices[o][m][n])
            new_matrix.append(new_row)
        result = new_matrix
    print()
    print('Here is your final matrix:')
    mat_print(result)
    return result
def scalar_mult():
    c = float(input("scalar input : "))
    print("Enter the rref.")
    org = rect_mat()
    for p in range(len(org)):
        for q in range(len(org[0])):
            org[p][q] *= c
    print()
    print('Here is your final matrix:')
    mat_print(org)
    return org
def mat_mult():
    mun = int(input("How many matrices do you wanna multiply: "))
    mat_store = []
    i = 0
    while 0<= i<= mun-1 :
        inp_mat = rect_mat()
        if i==0 :
            mat_store.append(inp_mat)
            i+=1
        elif 0< i and len(mat_store[i-1][0]) == len(inp_mat):
            mat_store.append(inp_mat)
            i+=1
        else:
            print('Multiplication not possible.')
            print(' A m x n matrix is multiplicable only with a n x r matrix.')
            continue       
    mult = mat_store[0]
    for r in range(1,mun):
        new_mult = []
        for s in range(len(mult)):
            mult_row = []
            for u in range(len(mat_store[r][0])):
                sum = 0
                for t in range(len(mat_store[r])):
                    sum+= mult[s][t] * mat_store[r][t][u]
                mult_row.append(sum)
            new_mult.append(mult_row)
        mult = new_mult
    print()
    print('Here is your final matrix:')
    mat_print(mult)
    return mult
def transpose():
    inp = rect_mat()
    transp_mat = []
    for g in range(len(inp[0])):
        transp_row = []
        for h in range(len(inp)):
            transp_row.append(inp[h][g])
        transp_mat.append(transp_row)
    print()
    print('Here is your final matrix:')
    mat_print(transp_mat)
    return transp_mat
def augment(motu, patlu):
    jhatka = []
    for flat in range(len(motu)):
        jhatka_row = []
        for pole in range(len(motu[0])):
            jhatka_row.append(motu[flat][pole])
        for stick in range(len(patlu[0])):
            jhatka_row.append(patlu[flat][stick])
        jhatka.append(jhatka_row)
    return jhatka
def strip_aug(john,lawn):
    ghasita_ram = []
    for hor in range(len(john)):
        ghasita_ram_row = []
        for ded in range(lawn):
            val = john[hor].pop()
            ghasita_ram_row.insert(0,val)
        ghasita_ram.append(ghasita_ram_row)
    return john, ghasita_ram
def ref():
    rock = rect_mat()
    import copy     
    jeez =copy.deepcopy(rock)
    ask = input("Do you want any matrix(with compatible dimensions) to be augmented as well? (yes/no)") 
    if ask == 'yes':
        while True: 
            sand = rect_mat()
            if len(sand) != len(rock):
                print('number of rows of both the matrices should be equal.')
            else:
                 break
    elif ask == 'no':
        sand = []
        for g in range(len(rock)):
            sand.append([0])
    aug = augment(rock, sand)
    picol=0
    pirow=0
    det_sign = 1
    for ser_col in range(picol,len(rock[0])):
        found = False      
        for ser_row in range(pirow,len(rock)): 
            if aug[pirow][ser_col] == 0:
                pivot_row = aug[pirow]               
                if aug[ser_row][ser_col] !=0:
                    found = True
                    picol= ser_col
                    aug[pirow] = aug[ser_row]
                    aug[ser_row] = pivot_row
                    det_sign*= -1
                    break
                elif aug[ser_row][ser_col] == 0:
                    continue
            else:
                found = True
                picol= ser_col
                break
        if found:
            for m in range(pirow+1,len(rock)):
                if rock[pirow][picol] != 0:
                    scalar = aug[m][picol]/aug[pirow][picol]
                    for n in range(len(aug[0])):               
                        aug[m][n] -= scalar*aug[pirow][n]    
            pirow += 1
        else:
            continue
    return aug, len(sand[0]), det_sign, jeez
def row_reduction():
    aug, lawn, _, jeez= ref()
    for row in range(len(aug)-1,-1,-1):
        for col in range(len(aug[0])-lawn):
            if aug[row][col] == 0:
                continue
            else:
                piv = aug[row][col]
                for t in range(len(aug[0])):
                    aug[row][t] /= piv
                for r in range(len(aug)):
                    scale = aug[r][col]/aug[row][col]
                    for s in range(len(aug[0])):
                        if r!= row:
                            aug[r][s] -= scale*aug[row][s]
                break                       
    rref, last_part = strip_aug(aug,lawn)
    return rref, last_part, jeez
def rank_nullity_internal(matrix):
    count = 0
    for zerow in matrix:
        counter = 0
        for zecol in zerow:
            if zecol == 0:
                counter += 1
            else:
                break
        if counter == len(matrix[0]):
            count += 1
        else:
            continue
    rank = len(matrix) - count
    nullity = len(matrix[0]) - rank
    print(f'Rank of the matrix: {rank}')
    print(f'Nullity of the matrix: {nullity}')
    return rank, nullity
def rank_nullity():
    rref, _, _ = row_reduction()
    rank, nullity = rank_nullity_internal(rref)
    return rank, nullity
def inverse():
    rref, inverse, _ = row_reduction()
    _, nullity = rank_nullity_internal(rref)
    if nullity == 0:
        mat_print(inverse)
    else:
        print()
        print('The input matrix is not invertible.')
    return inverse
def linear_system_solver():
    apple, banana, _ = row_reduction()
    _, nullity = rank_nullity_internal(apple)
    if nullity == 0:
        print("The system of linear equations has a unique solution.")
        print('Solution ↴')
        mat_print(banana)
    else:
        found = False
        for knife in range(len(apple)-1,-1,-1):
            zero_count = 0
            non_zero_counter = 0
            for gun in range(len(apple[0])):
                if apple[knife][gun] == 0 and zero_count< len(apple[0])-1:
                    zero_count +=1
                    continue
                elif apple[knife][gun] == 0 and zero_count == len(apple[0])-1:
                    if banana[knife][0] == 0:
                        continue
                    else:
                        found = True
                        print('The system of linear equations has no solution.')
                        break
                else:
                    if non_zero_counter<1:
                        non_zero_counter+=1
                        continue
                    else:
                        found = True        
                        print('The system of linear equations has infinitely many solutions.')
                        break
            if found:
                break
            else:
                continue
def determinant():
    hamza, _, det = ref()
    if len(hamza) == len(hamza[0]):
        for ding in range(len(hamza)):
            for dong in range(len(hamza[0])):
                if ding == dong:
                    det*= hamza[ding][dong]
                else:
                      continue
        print(f'Determinant  of your input rref = {det}')
    else:
        print('Determinant is possible only for square matrices and this is not one.')
    return det
def column_space_bases():
    alam, _, jeez = row_reduction()
    column_bases= []
    for u in range(len(alam)):
        base_row = []
        for v in range(len(alam[0])):
            if alam[u][v] == 0:
                continue
            else:
                for g in range(len(jeez)):
                    base_row.append(jeez[g][v])
                break
        column_bases.append(base_row)
    print(f'The bases of column space of the input rref are: {column_bases}')
def row_space_bases():
    soda, _, _ = row_reduction()
    rank, _ = rank_nullity_internal(soda)
    row_bases = []
    for d in range(rank):
        row_bases.append(soda[d])
    print(f'The bases of row space of the input rref are: {row_bases}')
def null_space_bases():
    print('You may refrain from appending the zero vector.')
    pen, _, _ = row_reduction()
    pivot_col = []
    for row in range(len(pen)):
        for column in range(len(pen[0])):
            if pen[row][column] == 0:
                continue
            else:
                pivot_col.append(column)
                break
    free_col = []
    for col in range(len(pen[0])):
        if col not in pivot_col:
           free_col.append(col)
        else:
            continue
    null_bases = []
    import copy     
    for free in free_col:
        pen_temp = copy.deepcopy(pen)
        for kat in free_col:
            if free != kat:
                for kit in range(len(pen)):
                  pen_temp[kit][kat] = 0
            else:
                continue
        basis = []
        for coolie in range(len(pen[0])):
            if free == coolie:
                basis.append(1)
            elif coolie in pivot_col:
                basis.append(-1*pen_temp[pivot_col.index(coolie)][free])
            else:
                basis.append(0)
        null_bases.append(basis)
    print(null_bases)
