% m为被除数array1的位长
% n为除数array2的位长
% temp数组存放余数，长度为n
% k从头到尾扫描到array1的元素
% array_1 = [1, 1, 0, 1, 0, 0, 1, 1];
%array_2 = [1, 1, 1, 0];
%temp = [0, 0, 0, 0];
array_1 = packet;
array_2 = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1];
temp = zeros(1,33);
m = length(array_1);
n = length(array_2);
k = n+1;
% 1.构造temp的初值，以后只对temp与array2进行异或
for i = 1:n %i从0变化到n-1
    temp(i) = xor(array_1(i), array_2(i));
end
flag = 1;
fprintf('%d %d %d %d\n', temp);
fprintf("开始\n");
while (k <= m && flag)
    % 2.找到1的最大索引j
    j = 1;
    while (j<=n && temp(j)==0)
        j = j+1;
    end
    %异常排除
    if (j > n) %如果全0，表示整除
        break;
	end
    %fprintf("j=%d\n",j);
    if (j-1 > m-k+1)        %如果剩余位数不足，凑齐后输出
        t = m-k+1;        %t表示可补充的位数
        for i = 0:n-j %把后面的元素往前挪，空出t位
            temp(j-t+i) = temp(j+i);
        end
        for i = 0:t-1   %向后取t位补齐
            temp(n-i) = array_1(m-i);
        end
        break;
	end
    %排除完毕

    % 3. j-1 恰好是缺少的位数,把后面的元素往前挪，空出j位
    for i = 0:n-j      %i从0变化到n-j-1
        temp(1+i) = temp(j+i);
	end

    % 4.向后取 j-1 位补齐
    t=j-1;
    for i = 1:t
        temp(n-t+i) = array_1(k+i-1);
    end
    k = k+j-1;         %令k永远指向下一位要借的数
    %print("k= "+str(k));
    if (k > m)          %k跑出边界说明没有可以借的数
        flag = 0;
	end
    %fprintf("补齐之后 ");
    %fprintf('%d %d %d %d\n', temp);
    % 5.n位的按位异或
    for i = 1:n     %i从1变化到n
        temp(i) = xor(temp(i), array_2(i));
    end
    %fprintf("异或之后 ");
    %fprintf('%d %d %d %d\n', temp);
end

fprintf("remainder = \n");
fprintf('%d %d %d %d\n',temp);
remainder = temp;
extend_zeros = zeros(1,32);
P = [packet, extend_zeros]; % this is P(x)
p = length(P);
q = length(remainder);
fprintf("p = %d, q = %d \n", p, q);
for i = 0:q-1
    P(p-i) = xor(P(p-i), remainder(q-i));
end
codepacket = P;
fprintf("Length of remainder = %d\n", length(remainder))
fprintf("Length of C(x) = %d", length(array_2))