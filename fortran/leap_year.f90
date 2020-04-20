program m
  do n=1800,2400
  if(mod(n,4)==0 .xor. mod(n,100)==0 .xor. mod(n,400)==0) print'(i4)',n
  enddo
end
