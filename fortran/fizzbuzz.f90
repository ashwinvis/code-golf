program main
      implicit none
      integer i
      logical m3, m5
      do i=1,100
        m3 = mod(i, 3) == 0
        m5 = mod(i, 5) == 0
        if (m3 .and. m5) then
          print "(a8)", "FizzBuzz"
        else if (m3) then
          print "(a4)", "Fizz"
        else if (m5) then
          print "(a4)", "Buzz"
        else if (i<10) then
          print '(i1)', i
        else
          print '(i2)', i
        end if
      end do
end program
