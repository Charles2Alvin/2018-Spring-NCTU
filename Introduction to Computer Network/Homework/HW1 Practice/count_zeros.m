function num = count_zeros(array)
num = 0;
len = length(array);
for i = 1:len
    if (array(i) == 0)
        num = num + 1;
    end
end