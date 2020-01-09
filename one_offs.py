def one_offs(*arg, **karg):
    sum_of_arg = sum(arg)
    sum_of_karg = sum(karg.values())
    
    print(f"The sum of the positional arguments is: {sum_of_arg}")
    print(f"The sum of the keywoard arguments is: {sum_of_karg}\n") 
    
one_offs(1, 2, 3, 4, kk=8, yy=9)
one_offs(jj=5)
one_offs(7)