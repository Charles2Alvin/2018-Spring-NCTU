load network_A.mat A
n = 100;
inf = 1000000;
for i = 1:n
    for j = 1:n
        if(A(i,j) == 0)
            A(i,j) = inf; %A(i,j)=0表明距离为无穷，修改后方便运算
        end
    end
end

for k = 1:n
    for i = 1:n
        for j = 1:n
            if(A(i,k)+A(k,j) < A(i,j))
                A(i,j) = A(i,k)+A(k,j);%插点法，插点后距离减小则更新
            end
        end
    end
end

for i = 1:n
    A(i,i) = 0; %对角线元素应为0
end

d = A;
save result.mat d


