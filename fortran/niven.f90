program main
    implicit none
    character(3) c
    integer i, j, s
    do i = 1, 100
      s = 0
      j = i
      do while (j > 0)
        s = s + mod(j, 10)
        j = j / 10
      end do
      if (mod(i, s) == 0) then
        write(c, '(i3)') i
        print '(a)', adjustl(c)
      end if
    end do
end program
