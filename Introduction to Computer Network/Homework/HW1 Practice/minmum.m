load network_A.mat A
n = 100;%n为图的顶点个数
cost = zeros(1,n);%存储每个顶点加入集合的最小开销
flag = zeros(1,n);%记录结点是否已经加入生成树
tree = zeros(n,n);%记录生成树
inf = 1000;%表示无穷大
aj = A;%邻接矩阵

% 0. 初始化
for i = 2:n
    cost(i) = aj(1,i);%开销初始化未与顶点1相连的开销
end
flag(1) = 1;

for k = 1:n-1  %扫描顶点不包括根顶点
    
% 1. 找出集合外产生开销最小的顶点
min = inf;
for i = 1:n
    if(flag(i) == 0)
        %fprintf("i = %d\n", i);
        for j = 1:n %找出未加入集合的顶点中，与集合点相连开销最小的点
            if(aj(i,j) < min && aj(i,j) ~= 0 && flag(j) == 1)
                min = aj(i,j);
                row = i;
                col = j;
            end
        end
    end
end
%fprintf("i = %d j = %d min = %d\n",row,col,min);
% 2. 将选中结点加入生成树，标记，并调整距离数组
flag(row) = 1;
tree(row,col) = min;
tree(col,row) = min;



end