function temp = long_division_remainder(array_1, array_2)
% This is function calculate the remainder of long division
% mΪ������array1��λ��
% nΪ����array2��λ��
% temp����������������Ϊn
% k��ͷ��βɨ�赽array1��Ԫ��
m = length(array_1);
n = length(array_2);
k = n+1;
temp = zeros(1,n);
% 1.����temp�ĳ�ֵ���Ժ�ֻ��temp��array2�������
for i = 1:n %i��0�仯��n-1
    temp(i) = xor(array_1(i), array_2(i));
end
flag = 1;
%fprintf('%d %d %d %d\n', temp);
%fprintf("��ʼ\n");
while (k <= m && flag)
    % 2.�ҵ�1���������j
    j = 1;
    while (j<=n && temp(j)==0)
        j = j+1;
    end
    %�쳣�ų�
    if (j > n) %���ȫ0����ʾ����
        break;
	end
    %fprintf("j=%d\n",j);
    if (j-1 > m-k+1)        %���ʣ��λ�����㣬��������
        t = m-k+1;        %t��ʾ�ɲ����λ��
        for i = 0:n-j %�Ѻ����Ԫ����ǰŲ���ճ�tλ
            temp(j-t+i) = temp(j+i);
        end
        for i = 0:t-1   %���ȡtλ����
            temp(n-i) = array_1(m-i);
        end
        break;
	end
    %�ų����

    % 3. j-1 ǡ����ȱ�ٵ�λ��,�Ѻ����Ԫ����ǰŲ���ճ�jλ
    for i = 0:n-j      %i��0�仯��n-j-1
        temp(1+i) = temp(j+i);
	end

    % 4.���ȡ j-1 λ����
    t=j-1;
    for i = 1:t
        temp(n-t+i) = array_1(k+i-1);
    end
    k = k+j-1;         %��k��Զָ����һλҪ�����
    %print("k= "+str(k));
    if (k > m)          %k�ܳ��߽�˵��û�п��Խ����
        flag = 0;
	end
    %fprintf("����֮�� ");
    %fprintf('%d %d %d %d\n', temp);
    % 5.nλ�İ�λ���
    for i = 1:n     %i��1�仯��n
        temp(i) = xor(temp(i), array_2(i));
    end
    %fprintf("���֮�� ");
    %fprintf('%d %d %d %d\n', temp);
end


