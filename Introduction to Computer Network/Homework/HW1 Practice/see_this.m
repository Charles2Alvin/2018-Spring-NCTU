C = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1];   
a = [1,0,1];
b = conv(C,a);
for i = 1:length(b)
    b(i) = mod(b(i),2);
end
d = long_division_remainder(b,C)