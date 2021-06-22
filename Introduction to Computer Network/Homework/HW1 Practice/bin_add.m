function result = bin_add(a,b);
len = length(a);
result = zeros(1,len);
%suppose two arrays has the same lengths
%fprintf("len is %d\n", len);
flag = 0;
for i = len:-1:1
    if (a(i) == 1 && b(i) == 1 && flag == 1)
        %fprintf("one i is %d\n", i);
        result(i) = 1;
        continue;
    end
    if (a(i) == 1 && b(i) == 1 && flag == 0)
        %fprintf("two i is %d\n", i);
        result(i) = 0;
        flag = 1;
        continue;
    end
    if ((a(i) == 0 && b(i) == 1 && flag == 1) ||(a(i) == 1 && b(i) == 0 && flag == 1))
        %fprintf("three i is %d\n", i);
        result(i) = 0;
        flag = 1;
        continue;
    end
    if ((a(i) == 0 && b(i) == 1 && flag == 0) ||(a(i) == 1 && b(i) == 0 && flag == 0))
        %fprintf("four i is %d\n", i);
        result(i) = 1;
        continue;
    end
    if (a(i) == 0 && b(i) == 0 && flag == 1)
        %fprintf("five i is %d\n", i);
        result(i) = 1;
        flag = 0;
        continue;
    end
    if (a(i) == 0 && b(i) == 0 && flag == 0)
        %fprintf("six i is %d\n", i);
        result(i) = 0;
        continue;
    end
end
