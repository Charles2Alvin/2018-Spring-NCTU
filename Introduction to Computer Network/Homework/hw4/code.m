load network_A.mat A
n = 100;
inf = 1000000;
for i = 1:n
    for j = 1:n
        if(A(i,j) == 0)
            A(i,j) = inf; %A(i,j)=0��������Ϊ����޸ĺ󷽱�����
        end
    end
end

for k = 1:n
    for i = 1:n
        for j = 1:n
            if(A(i,k)+A(k,j) < A(i,j))
                A(i,j) = A(i,k)+A(k,j);%��㷨����������С�����
            end
        end
    end
end

for i = 1:n
    A(i,i) = 0; %�Խ���Ԫ��ӦΪ0
end

d = A;
save result.mat d


