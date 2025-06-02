% Facts
male(john).
male(paul).
male(mike).
female(lisa).
female(susan).
female(mary).

parent(john, paul).
parent(john, lisa).
parent(mary, paul).
parent(mary, lisa).
parent(paul, mike).
parent(susan, mike).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
siblings(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Sample Queries (run in Prolog interpreter)
% ?- father(john, paul).
% ?- mother(mary, lisa).
% ?- siblings(paul, lisa).
% ?- grandparent(john, mike).
