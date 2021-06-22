function bool = is_divisible(array);
C = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1];    
a = long_division_remainder(array, C);
bool = is_all_zeros(a);