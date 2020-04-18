recursive function fib(n) result(f)
  implicit none
  integer :: f, n
  if (n == 0) then
    f = 0
  else if (n < 3) then
    f = 1
  else
    f = fib(n-1) + fib(n-2)
  end if
end function

! Notes
! -----
! Return type mismatch: https://stackoverflow.com/questions/24876500/error-return-type-mismatch-of-function-in-fortran-95
! when interface was not used
subroutine functional
  implicit none
  integer :: n
  character(6) :: c
  interface
    recursive function fib(x)
      integer :: fib, x
    end function
  end interface

  do n=0,30
    write (c, "(i6)") fib(n)
    print "(a6)", adjustl(c)
  end do
end subroutine

! Notes
! -----
! Left justifying integers/character arrays:  https://jblevins.org/log/leftjust
subroutine imperative
  implicit none
  integer :: a, b, n, t
  character(6) :: c
  a = 0
  b = 1
  do n=0,30
    write (c, "(i6)") a
    print '(a6)', adjustl(c)
    t = b
    b = a
    a = a + t
  end do
end subroutine

program main
  call functional
  call imperative
end program
