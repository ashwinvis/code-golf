program main
      real x, fact

      fact(x) = round(gamma(x-1))

      print *, fact(3.0)
end
