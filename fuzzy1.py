A{"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6] 
B={"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5} 
print('The First Fuzzy Set is:', A) 
print('The Second Fuzzy Set is:', B) 
union set = {} 
for key in A: 
union_set [key] = max(A[key], B[key]) 
print('Fuzzy Set Union is:', union_set) 
intersection_set = {} 
for key in A: 
intersection set [key] = min(A[key], B[key]) 
print('Fuzzy Set Intersection is:', intersection set) 
complement A = {} 
for key in A: 
complement_A[key] = 1 -A [key] 
print('Complement of A is:', complement_A) 
complement_B = {} 
for key in B: 
complement_B[key] =1 -B[key] 
print('Complement of Bis:', complement_B) 
difference_set = {} 
for key in A: 
difference_set [key] max (0, A[key] - B[key]) = 
print('Fuzzy Set Difference (A -B) is:', difference set) 
symmetzic_diff_set = {} 
for key in A: 
symmetric_diff_set [key] = abs (A [key] B[key]) 
print('Fuzzy Set Symmetric Difference is:', symmetric_diff_set)
