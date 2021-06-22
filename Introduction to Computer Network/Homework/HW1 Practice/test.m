m = 4;
n = 4;
A = zeros(4,4);
for k=1:m*n
     row=floor(k-1/n)+1;

     col=mod(k-1,n)+1;

     B()=A(k)+row+col;

end