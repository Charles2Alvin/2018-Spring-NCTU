function bool = ten_ones(array);
num = 0;
len = length(array);
for i = 1:len
    if (array(i) == 1)
        num = num + 1;
    end
end
bool = 0;
if (num == 10)
    bool = 1;
end