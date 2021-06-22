% m为被除数array1的位长
% n为除数array2的位长
% temp数组存放余数，长度为n
% k从头到尾扫描到array1的元素
array_1 = [1 1 0 1 1];
array_2 = [1 0 ];
temp = zeros(1, 4);
m = length(array_1);
n = length(array_2);
k = m-n+1;
while(k >=1 )
	% 1.n位的按位异或
	for i = 1:n
		temp(i) = xor(array_1(k+i-1), array_2(i));
    end
    k = k - 1;
	% 2.找到1的最大索引j
    j = n;
    while(temp(j) ~= 0)
        j = j -1;
    end
	% 3.移动数组
	for i = 0:j - 1
		temp(n-i) = temp(j-i);
    end
    temp(1) = array_1(k);
    
end
fprintf('%d',temp);

