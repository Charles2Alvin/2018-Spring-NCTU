load network_A.mat A
n = 100;%nΪͼ�Ķ������
flag = zeros(1,n);%����Ԫ�ذ��������Ѽ����������Ľ��
tree = zeros(n,n);%��¼������
aj = A;%�ڽӾ���
count = 2
% 1. ��ʼ��
flag(1) = 1%��һ��������Ǹ��ڵ�
for i = 1:n
    if(aj(1,i) == 1) %�������ڵ�����������������
        flag(count) = i
        count = count + 1
        tree(1,i) = 1%�����������
        tree(i,1) = 1
    end
end

%2.�����������������
while(count < n+1)
    for i = 1:n
        if (any(flag==i))%���i�Ѿ����������������Թ�
            continue;
        else
            fprintf("see %d\n",i);
            for j = 1:n%ɨ��i�Ƿ����������ڵ�����j����
                if(any(flag == j))
                    fprintf("%d is in tree\n",j)
                    if (aj(i,j) == 1)
                        fprintf("add %d and %d\n",i,j)
                        flag(count) = i%������������������
                        count = count + 1;
                        tree(i,j) = 1;
                        tree(j,i) = 1;
                        break;
                    end
                end
            end
        end
    end
end
    
    
   