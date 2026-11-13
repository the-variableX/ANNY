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
def mat_print(matrix):
     print()
     for p in matrix:
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
def augment(matrix_1, matrix_2):
    separate_marix = []
    for row in range(len(matrix_1)):
        separate_marix_row = []
        for col in range(len(matrix_1[0])):
            separate_marix_row.append(matrix_1[row][col])
        for temp_col in range(len(matrix_2[0])):
            separate_marix_row.append(matrix_2[row][temp_col])
        separate_marix.append(separate_marix_row)
    return separate_marix
def strip_aug(augmented_matrix,col_right_matrix):
    right_matrix = []
    for row in range(len(augmented_matrix)):
        right_matrix_row = []
        for col in range(col_right_matrix):
            val = augmented_matrix[row].pop()
            right_matrix_row.insert(0,val)
        right_matrix.append(right_matrix_row)
    return augmented_matrix, right_matrix
def ref():
    input_matrix = rect_mat()
    import copy     
    original_matrix =copy.deepcopy(input_matrix)
    ask = input("Do you want any matrix(with compatible dimensions) to be augmented as well? (yes/no)") 
    if ask == 'yes':
        while True: 
            right_matrix = rect_mat()
            if len(right_matrix) != len(input_matrix):
                print('number of rows of both the matrices should be equal.')
            else:
                 break
    elif ask == 'no':
        right_matrix = []
        for g in range(len(input_matrix)):
            right_matrix.append([0])
    augmented_matrix = augment(input_matrix, right_matrix)
    piv_col=0
    piv_row=0
    det_sign = 1
    for search_column in range(piv_col,len(input_matrix[0])):
        found = False      
        for search_row in range(piv_row,len(input_matrix)): 
            if augmented_matrix[piv_row][search_column] == 0:
                pivot_row = augmented_matrix[piv_row]               
                if augmented_matrix[search_row][search_column] !=0:
                    found = True
                    piv_col= search_column
                    augmented_matrix[piv_row] = augmented_matrix[search_row]
                    augmented_matrix[search_row] = pivot_row
                    det_sign*= -1
                    break
                elif augmented_matrix[search_row][search_column] == 0:
                    continue
            else:
                found = True
                piv_col= search_column
                break
        if found:
            for m in range(piv_row+1,len(input_matrix)):
                if input_matrix[piv_row][piv_col] != 0:
                    scalar = augmented_matrix[m][piv_col]/augmented_matrix[piv_row][piv_col]
                    for n in range(len(augmented_matrix[0])):               
                        augmented_matrix[m][n] -= scalar*augmented_matrix[piv_row][n]    
            piv_row += 1
        else:
            continue
    return augmented_matrix, len(right_matrix[0]), det_sign, original_matrix
def row_reduction():
    augmented_matrix, col_right_matrix, _, original_matrix= ref()
    for row in range(len(augmented_matrix)-1,-1,-1):
        for col in range(len(augmented_matrix[0])-col_right_matrix):
            if augmented_matrix[row][col] == 0:
                continue
            else:
                pivot_value = augmented_matrix[row][col]
                for t in range(len(augmented_matrix[0])):
                    augmented_matrix[row][t] /= pivot_value
                for r in range(len(augmented_matrix)):
                    scale = augmented_matrix[r][col]/augmented_matrix[row][col]
                    for s in range(len(augmented_matrix[0])):
                        if r!= row:
                            augmented_matrix[r][s] -= scale*augmented_matrix[row][s]
                break                       
    rref, right_matrix = strip_aug(augmented_matrix,col_right_matrix)
    return rref, right_matrix, original_matrix
def rank_nullity_internal(matrix):
    count = 0
    for zero_row in matrix:
        counter = 0
        for zero_col in zero_row:
            if zero_col == 0:
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
    rref, last_part, _ = row_reduction()
    _, nullity = rank_nullity_internal(rref)
    if nullity == 0:
        print("The system of linear equations has a unique solution.")
        print('Solution ↴')
        mat_print(last_part)
    else:
        found = False
        for row in range(len(rref)-1,-1,-1):
            zero_count = 0
            non_zero_counter = 0
            for col in range(len(rref[0])):
                if rref[row][col] == 0 and zero_count< len(rref[0])-1:
                    zero_count +=1
                    continue
                elif rref[row][col] == 0 and zero_count == len(rref[0])-1:
                    if last_part[row][0] == 0:
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
    ref_matrix, _, det = ref()
    if len(ref_matrix) == len(ref_matrix[0]):
        for row in range(len(ref_matrix)):
            for col in range(len(ref_matrix[0])):
                if row == col:
                    det*= ref_matrix[row][col]
                else:
                      continue
        print(f'Determinant  of your input rref = {det}')
    else:
        print('Determinant is possible only for square matrices and this is not one.')
    return det
def column_space_bases():
    rref, _, original_matrix = row_reduction()
    column_bases= []
    for u in range(len(rref)):
        base_row = []
        for v in range(len(rref[0])):
            if rref[u][v] == 0:
                continue
            else:
                for g in range(len(original_matrix)):
                    base_row.append(original_matrix[g][v])
                break
        column_bases.append(base_row)
    print(f'The bases of column space of the input rref are: {column_bases}')
def row_space_bases():
    rref, _, _ = row_reduction()
    rank, _ = rank_nullity_internal(rref)
    row_bases = []
    for d in range(rank):
        row_bases.append(rref[d])
    print(f'The bases of row space of the input rref are: {row_bases}')
def null_space_bases():
    print('You may refrain from appending the zero vector.')
    rref, _, _ = row_reduction()
    pivot_col = []
    for row in range(len(rref)):
        for column in range(len(rref[0])):
            if rref[row][column] == 0:
                continue
            else:
                pivot_col.append(column)
                break
    free_col = []
    for col in range(len(rref[0])):
        if col not in pivot_col:
           free_col.append(col)
        else:
            continue
    null_bases = []
    import copy     
    for free in free_col:
        rref_temp = copy.deepcopy(rref)
        for kat in free_col:
            if free != kat:
                for kit in range(len(rref)):
                  rref_temp[kit][kat] = 0
            else:
                continue
        basis = []
        for col in range(len(rref[0])):
            if free == col:
                basis.append(1)
            elif col in pivot_col:
                basis.append(-1*rref_temp[pivot_col.index(col)][free])
            else:
                basis.append(0)
        null_bases.append(basis)
    print(null_bases)
