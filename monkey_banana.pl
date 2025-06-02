% State: monkey(MonkeyPos), box(BoxPos), monkey_status(MonkeyOnFloorOrBox), has_banana(yes/no)

% Goal state
goal(state(_, _, on_box, yes)).

% Initial state
initial_state(state(at_door, at_window, on_floor, no)).

% Move operations
move(state(Monkey, Box, on_floor, no),
     walk(Monkey, NewPos),
     state(NewPos, Box, on_floor, no)) :-
    location(NewPos),
    Monkey \= NewPos.

move(state(Monkey, Box, on_floor, no),
     push(Monkey, NewPos),
     state(NewPos, NewPos, on_floor, no)) :-
    Monkey = Box,
    location(NewPos),
    Box \= NewPos.

move(state(Pos, Pos, on_floor, no),
     climb,
     state(Pos, Pos, on_box, no)).

move(state(Pos, Pos, on_box, no),
     grab,
     state(Pos, Pos, on_box, yes)) :-
    banana_position(Pos).

% Possible positions
location(at_door).
location(at_window).
location(at_middle).

% Bananas are at middle of the room
banana_position(at_middle).

% Plan from initial state to goal
plan(State, [], State) :- goal(State).
plan(State1, [Move|Moves], State3) :-
    move(State1, Move, State2),
    plan(State2, Moves, State3).

% To solve: run ?- solve.
solve :-
    initial_state(State),
    plan(State, Moves, _),
    write('Plan to reach bananas:'), nl,
    write_moves(Moves).

write_moves([]).
write_moves([Move|Rest]) :-
    write('- '), write(Move), nl,
    write_moves(Rest).
