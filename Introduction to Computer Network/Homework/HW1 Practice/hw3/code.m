load network_A.mat A
n = 100
visit = zeros(1,n);%标记顶点是否被访问
queue = zeros(1,n);%队列存储每一层的顶点
tree = zeros(n,n);
btag = 1%队首标记
etag = 2%队尾标记
visit(1) = 1
queue(1) = 1
while(btag <= etag && etag <= n)
    t = queue(btag);%取出队首
    for i = 1:n
        if(~visit(i))
            if(A(i,t) == 1)%将未访问的，且与队首相连的顶点加入队列
                queue(etag) = i;
                etag = etag + 1;
                visit(i) = 1;
                tree(i,t) = 1;%输出到生成树中
                tree(t,i) = 1;
            end
        end
    end
    btag = btag+1
end
save result.mat tree