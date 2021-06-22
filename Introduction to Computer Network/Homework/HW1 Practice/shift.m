function array = shift(a,b);
len = length(a);
array = zeros(1,len);
for i = len:-1:1+b
    %fprintf("i = %d\n", i);
    array(i-b) = a(i);
end
