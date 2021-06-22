%{
D = zeros(32,65);
A1 = [1,2,3;4,5,6;7,8,9];
A2 = A1';
A3 = A2 - A1;
B = cat(3,A1,A2,A3)
%}
C = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1]; 
C = [zeros(1,32), C];
len = length(C);
D = zeros(1,65,3);
for i = 1:32
    D(:,:,i) = shift(C,i);
end

for t1 = 1:32
for t2 = t1+1:32
for t3 = t2+1:32
for t4 = t3+1:32
for t5 = t4+1:32
for t6 = t5+1:32
for t7 = t6+1:32
%for t8 = t7+1:32
        m1 = xor(D(:,:,t1),D(:,:,t2));
        m2 = xor(m1, D(:,:,t3));
        m3 = xor(m2, D(:,:,t4));
        m4 = xor(m3, D(:,:,t5));
        m5 = xor(m4, D(:,:,t6));
        m6 = xor(m5, D(:,:,t7))
        %m7 = xor(m6, D(:,:,t8));
        if(less_than_ten_ones(m6))
            fprintf("Ha\n");
            break;
        end
%end
end
end
end
end
end
end
end
fprintf("Done");


