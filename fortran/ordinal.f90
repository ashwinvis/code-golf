subroutine print_suffix(c)
    implicit none
    character(9) c, suffix
    integer n, r10, r100

    ! write (n, '(a)') nc
    read (c, '(i9)') n
    r10 = mod(n, 10)
    r100 = mod(n, 100)

    if (r100 == 11 .or. r100 == 12 .or. r100 == 13) then
      suffix = 'th'
    else if (r10 == 1) then
      suffix = 'st'
    else if (r10 == 2) then
      suffix = 'nd'
    else if (r10 == 3) then
      suffix = 'rd'
    else
      suffix = 'th'
    end if

    print '(a,a2)', trim(c), suffix
end subroutine

program main
    integer n
    character(9) arg
    do i = 1, iargc()
      call getarg(i, arg)
      call print_suffix(arg)
    end do
end program
