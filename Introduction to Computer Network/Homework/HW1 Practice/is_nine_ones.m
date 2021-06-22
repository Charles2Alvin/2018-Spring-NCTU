function bool = less_than_ten_ones(array);
num = 0;
len = length(array);
for i = 1:len
    if (array(i) == 1)
        num = num + 1;
    end
end
bool = 0;
if (num == 9)
    bool = 1;
end