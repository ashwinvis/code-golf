program main
   implicit none
   integer, parameter:: dp=selected_real_kind(p=32)
   real(kind=dp) :: a
   a =  1.0_dp/3
   print *, a
end program
