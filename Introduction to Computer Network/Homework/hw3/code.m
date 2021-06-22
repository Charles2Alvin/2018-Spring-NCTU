load network_A.mat A
n = 100
visit = zeros(1,n);%��Ƕ����Ƿ񱻷���
queue = zeros(1,n);%���д洢ÿһ��Ķ���
tree = zeros(n,n);
btag = 1%���ױ��
etag = 2%��β���
visit(1) = 1
queue(1) = 1
while(btag <= etag && etag <= n)
    t = queue(btag);%ȡ������
    for i = 1:n
        if(~visit(i))
            if(A(i,t) == 1)%��δ���ʵģ�������������Ķ���������
                queue(etag) = i;
                etag = etag + 1;
                visit(i) = 1;
                tree(i,t) = 1;%�������������
                tree(t,i) = 1;
            end
        end
    end
    btag = btag+1
end
save result.mat tree