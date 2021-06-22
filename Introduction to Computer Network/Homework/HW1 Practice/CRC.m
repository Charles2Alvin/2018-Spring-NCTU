function [result,remain] = CRC(array_1,array_2)
%array_1 is the packet poly to be CRCed
%array_2 is the C(x)
len_1 = length(array_2)-1;   %the degree of C(x)
result = [array_1, zeros(1,len_1)];   %zero extension
remain = long_division_remainder(result, array_2);
p = length(result);
q = length(remain);
for i = 0:q-1
    result(p-i) = xor(result(p-i), remain(q-i));
end