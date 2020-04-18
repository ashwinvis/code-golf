subroutine bash
  call system('ls -1t *.f90 | head -n 1 | xargs cat')
end subroutine
