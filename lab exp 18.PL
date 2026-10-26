person(ravi, date(15, 5, 2002)).
person(priya, date(20, 8, 2003)).
person(ajay, date(10, 12, 2001)).
person(anu, date(25, 3, 2004)).
dob(Name, DOB) :-
    person(Name, DOB).