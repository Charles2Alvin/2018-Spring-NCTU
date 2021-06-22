function num_ones = count_ones(array)
num_ones = 0;
len = length(array);
for i = 1:len
    if (array(i) == 1)
        num_ones = num_ones + 1;
    end
end
%fprintf('ones %d\n',num_ones);