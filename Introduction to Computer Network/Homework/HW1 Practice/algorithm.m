% mΪ������array1��λ��
% nΪ����array2��λ��
% temp����������������Ϊn
% k��ͷ��βɨ�赽array1��Ԫ��
array_1 = [1 1 0 1 1];
array_2 = [1 0 ];
temp = zeros(1, 4);
m = length(array_1);
n = length(array_2);
k = m-n+1;
while(k >=1 )
	% 1.nλ�İ�λ���
	for i = 1:n
		temp(i) = xor(array_1(k+i-1), array_2(i));
    end
    k = k - 1;
	% 2.�ҵ�1���������j
    j = n;
    while(temp(j) ~= 0)
        j = j -1;
    end
	% 3.�ƶ�����
	for i = 0:j - 1
		temp(n-i) = temp(j-i);
    end
    temp(1) = array_1(k);
    
end
fprintf('%d',temp);

