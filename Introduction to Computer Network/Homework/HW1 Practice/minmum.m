load network_A.mat A
n = 100;%nΪͼ�Ķ������
cost = zeros(1,n);%�洢ÿ��������뼯�ϵ���С����
flag = zeros(1,n);%��¼����Ƿ��Ѿ�����������
tree = zeros(n,n);%��¼������
inf = 1000;%��ʾ�����
aj = A;%�ڽӾ���

% 0. ��ʼ��
for i = 2:n
    cost(i) = aj(1,i);%������ʼ��δ�붥��1�����Ŀ���
end
flag(1) = 1;

for k = 1:n-1  %ɨ�趥�㲻����������
    
% 1. �ҳ����������������С�Ķ���
min = inf;
for i = 1:n
    if(flag(i) == 0)
        %fprintf("i = %d\n", i);
        for j = 1:n %�ҳ�δ���뼯�ϵĶ����У��뼯�ϵ�����������С�ĵ�
            if(aj(i,j) < min && aj(i,j) ~= 0 && flag(j) == 1)
                min = aj(i,j);
                row = i;
                col = j;
            end
        end
    end
end
%fprintf("i = %d j = %d min = %d\n",row,col,min);
% 2. ��ѡ�н���������������ǣ���������������
flag(row) = 1;
tree(row,col) = min;
tree(col,row) = min;



end