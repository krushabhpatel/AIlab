list_concat([],L,L).
list_concat([X1|L1],L2,[X1|L3]):-list_concat(L1,L2,L3).

list_rev([],[]).
list_rev([Head|Tail],Reversed):-list_rev(Tail, RevTail),list_concat(RevTail, [Head],Reversed).

list_length([],0).
list_length([_|TAIL],N) :- list_length(TAIL,N1), N is N1 + 1.
