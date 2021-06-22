C = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1];
fprintf("¿ªÊ¼");
flag = 0;
for t1 = 0:1
for t2 = 0:1
for t3 = 0:1
for t4 = 0:1
for t5 = 0:1
    
for t6 = 0:1
for t7 = 0:1
for t8 = 0:1
for t9 = 0:1
for t10 = 0:1

for t11 = 0:1
for t12 = 0:1
for t13 = 0:1
for t14 = 0:1
for t15 = 0:1

for t16 = 0:1
for t17 = 0:1
for t18 = 0:1
for t19 = 0:1
for t20 = 0:1
    
for t21 = 0:1
for t22 = 0:1
for t23 = 0:1
for t24 = 0:1
for t25 = 0:1

for t26 = 0:1
for t27 = 0:1
for t28 = 0:1
for t29 = 0:1
for t30 = 0:1
    
for t31 = 0:1
for t32 = 0:1
for t33 = 0:1
for t34 = 0:1
for t35 = 0:1

for t36 = 0:1
for t37 = 0:1
for t38 = 0:1
for t39 = 0:1
for t40 = 0:1
        if(flag)
            break;
        end
        a =[t1, t2, t3, t4, t5, t6,t7, t8, t9, t10, ...
            t11, t12, t13, t14, t15, t16, t17, t18, t19, t20,...
            t21, t22, t23, t24, t25, t26, t27, t28, t29, t30,...
            t31, t32, t33, t34, t35, t36, t37, t38, t39, t40]
        b = conv(C,a);
        for i = 1:length(b)
            b(i) = mod(b(i),2);
        end
        less= ten_ones(b);
        %fprintf("there are %d ones\n", ones);
        check = is_all_zeros(b);
        if (less == 1 && ~check)
                flag = 1;
                fprintf("here comes the result:)\n");
                fprintf("there are ten ones\n");
                fprintf("type b to see the result\n");
                break;
        end         
end
end
end
end
end

end
end
end
end
end
% 10 ends
end
end
end
end
end

end
end
end
end
end
% 20 ends
end
end
end
end
end

end
end
end
end
end
% 30 ends
end
end
end
end
end

end
end
end
end
end
% 40 ends
fprintf('It is done');

re = long_division_remainder(a,C)


