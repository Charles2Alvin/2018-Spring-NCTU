function bo = is_all_zeros(array);
len = length(array);
zeros = count_zeros(array);
if (zeros == len)
    bo = 1;
else
    bo = 0;
end