C = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1];
 for i = 1:10000000
     a = strrep(dec2bin(i),' ','');
     for j = 1:length(a)
         q(j) = str2num(a(j));
     end
     b = conv(C,q);
     for i = 1:length(b)
            b(i) = mod(b(i),2)
     end
     less = ten_ones(b);
     if(less)
         fprintf("here comes the result:)\n");
         fprintf("there are %d ones\n", ones);
         fprintf("type b to see the result\n");
         break;
     end
 end