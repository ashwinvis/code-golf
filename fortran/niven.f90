subroutine printc(i)
  implicit none
  integer i
  character(3) c

  write(c, '(i3)') i
  print '(a)', adjustl(c)
end subroutine
program main
    implicit none
    integer i, d1, d10
    do i = 1, 9
      call printc(i)
    end do
    do i = 10,99
      d1 = mod(i, 10)
      d10 = i / 10
      if (mod(i, d1 + d10) == 0) then
        call printc(i)
      end if
    end do
    call printc(100)
end program
