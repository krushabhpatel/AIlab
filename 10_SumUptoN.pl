sum(0,0).
sum(N,Result):-N>0,Prev is N - 1,sum(Prev, PrevResult),Result is PrevResult + N.
