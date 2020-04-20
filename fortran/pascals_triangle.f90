program main
  implicit none
  integer x, order, degree

  factorial(x) = gamma(x-1)
  do order=1,20
    do degree=0,order+1)
        print*, (binomial(order, degree), ' ')
    end
    print('\Vn')
end
