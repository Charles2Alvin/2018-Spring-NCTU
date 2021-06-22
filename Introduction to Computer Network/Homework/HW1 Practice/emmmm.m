C = [1, 0,0,0,0,  0,1,0,0,  1,1,0,0,  0,0,0,1,  0,0,0,1,  1,1,0,1,  1,0,1,1,  0,1,1,1];    
%E_ones = count_ones(E);
%fprintf('%d\n', E_ones)
%fprintf("E is %d %d %d", E);
for i = 0:1
    for j = 0:1
        for k = 0:1
            for p = 0:1
                for q = 0:1
                    for r = 0:1
                        for m = 0:1
                            for n = 0:1
                                for o = 0:1
                                    for x = 0:1
                                        E = [i,j,k,p,q,r,m,n,o,x];
                                         [code,remainder] = CRC(E,C);
                                         num_ones = count_ones(code);
                                             %fprintf("code ones %d  E zeros %d  E length  %d\n", num_ones, num_zeros, code_len);
                                         if(num_ones < 10 && ~(count_zeros(E) == length(E)))
                                           %if(num_ones < 10 )
                                          fprintf("Here comes the E %d\n", E);
                                             fprintf('The num of ones is %d', num_ones);
                                            break;
                       end
            end
            end
            end
            end
            end
            end
            end
        end
    end 
end



            