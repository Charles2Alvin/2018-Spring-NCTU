load network_A.mat A
n = 100;%n为图的顶点个数
flag = zeros(1,n);%数组元素包含所有已加入生成树的结点
tree = zeros(n,n);%记录生成树
aj = A;%邻接矩阵
count = 2
% 1. 初始化
flag(1) = 1%第一个加入的是根节点
for i = 1:n
    if(aj(1,i) == 1) %如果与根节点相连，加入生成树
        flag(count) = i
        count = count + 1
        tree(1,i) = 1%输出到生成树
        tree(i,1) = 1
    end
end

%2.将其他点加入生成树
while(count < n+1)
    for i = 1:n
        if (any(flag==i))%如果i已经加入生成树，则略过
            continue;
        else
            fprintf("see %d\n",i);
            for j = 1:n%扫描i是否与生成树内的任意j相连
                if(any(flag == j))
                    fprintf("%d is in tree\n",j)
                    if (aj(i,j) == 1)
                        fprintf("add %d and %d\n",i,j)
                        flag(count) = i%若相连，加入生成树
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
    
    
   