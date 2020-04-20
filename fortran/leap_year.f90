program m
  logical d
  d(i)=mod(n,i)==0
  do n=1800,2400
  if(d(4).xor.d(100).xor.d(400)) print'(i4)',n
  enddo
end
