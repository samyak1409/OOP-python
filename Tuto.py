# https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc


# Class:

class Sport:

    class_var = 'in'  # ATTRIBUTE actually.
    no_of_sports = 0
    demo_class_var = 'I am just for illustration purpose.'

    def __init__(self, name, rank, no_of_players, played_in):  # self-> convention
        self.name = name  # self.name-> named same as the name of parameter just by the convention
        self.rank = rank
        self.no_of_players = no_of_players
        self.played_in = played_in
        Sport.no_of_sports += 1

    def desc(self):  # instance method -> automatically takes instance as an argument
        return f'{self.name} is played {self.class_var} {self.played_in} with {self.no_of_players} players!'

    @classmethod  # (decorator)
    def set_demo_class_var(cls, value):  # class method -> automatically takes class as an argument
        cls.demo_class_var = value

    @classmethod
    def from_string(cls, string):
        return cls(*string.split())

    @staticmethod
    def bla():  # static method-> automatically takes nothing as an argument (don't take self as an argument)
        # then you might have a question-> then why is this inside class,
        # -> because it has some logical connection with the class!
        return 'I am a static method of Sport class!'

        # also, we can know whether to make a method normal(i.e. instance) or class or static by
        # checking the usage of instance / class in that method's definition! 👌

    # https://youtu.be/5cvM-crlDvg
    def __repr__(self):  # for unambiguity
        return f"Sport('{self.name}', {self.rank}, {self.no_of_players}, '{self.played_in}')"

    def __str__(self):  # for readability
        return f'{self.name} is on rank {self.rank} which is played with {self.no_of_players} players {self.class_var} {self.played_in}.'

    def __add__(self, other):  # for adding no of players in those games
        return self.no_of_players + other.no_of_players

    def __len__(self):  # for len of the sport name
        return len(self.name)


# Instances: (Objects)

badminton = Sport(name='Badminton', rank=1, no_of_players=2, played_in='court')
cricket = Sport(name='Cricket', rank=2, no_of_players=11, played_in='ground')
tt = Sport(name='Table Tennis', rank=3, no_of_players=2, played_in='table')
# badminton, cricket and tt are instances (objects) of Sport class.

print()
print(badminton.desc())
print(tt.desc())  # self is automatically passed
print(Sport.desc(tt))  # tt.desc() is internally converted in this!
print(cricket.desc())


# Instance variables -> unique for all instances of a class (e.g. here-> name, rank, no_of_players, played_in)
# Class variables -> same for all instances of that class (e.g. here-> class_var, no_of_sports)

print()
print(Sport.class_var, badminton.class_var, tt.class_var)
print(tt.__dict__)  # tt's namespace
tt.class_var = 'on'
print(tt.__dict__)
print(tt.class_var)
# what happens is, first python checks if the variable has that attr or not, if not,
# then it checks it's class for the same, and then parent classes also (if parent class exist).
# and at the end in builtins.object (every class in Python inherits from this internally)
# This process is called Scope Resolution Order!
print(badminton.desc())
print(tt.desc())  # now tt is played 'on' table!

print()
print(Sport.no_of_sports)


# Class Methods:

print()
print(Sport.demo_class_var)
Sport.demo_class_var = 'directly'  # method1
print(Sport.demo_class_var)
Sport.set_demo_class_var(value='by using class method')  # method2
print(Sport.demo_class_var)
# these both methods are doing the same work!

# using class method as a SECONDARY CONSTRUCTOR (__init__):
chess = Sport.from_string(string='Chess 4 2 board')
# e.g. when we have a string of values, we won't want to format that string everytime so made a secondary constructor!
# COOL RIGHT!
chess.class_var = 'on'
print()
print(chess.desc())  # yeah!


# Static Methods:

print()
print(Sport.bla())


# INHERITANCE:

class IndoorSport(Sport):

    def __init__(self, name, rank, no_of_players, played_in, audience_limit):
        super().__init__(name, rank, no_of_players, played_in)
        # Sport.__init__(self, name, rank, no_of_players, played_in)  # if you have multiple parent classes
        self.audience_limit = audience_limit


class OutdoorSport(Sport):

    def __init__(self, name, rank, no_of_players, played_in, rain_matters):
        super().__init__(name, rank, no_of_players, played_in)
        self.rain_matters = rain_matters


tt = IndoorSport(name='Table Tennis', rank=3, no_of_players=2, played_in='table', audience_limit=100)
football = OutdoorSport(name='Football', rank=5, no_of_players=11, played_in='ground', rain_matters=False)

print()
print(tt.audience_limit)
print(football.rain_matters)

print()
print(isinstance(football, Sport))
print(issubclass(IndoorSport, OutdoorSport))


# Magic (Dunder) Methods:

print()
chess.set_demo_class_var('on')
print('repr of chess obj:', repr(chess))  # internally calling __repr__ (repr -> representation)
print('str of chess obj:', str(chess))  # internally calling __str__
print()
# NOW LET ME BLOW YOUR MIND ->
print('total no. of players in badminton and cricket:', badminton + cricket)  # calls Sport.__add__
print(f'length of tt.name ("{tt.name}"):', len(tt))  # calls Sport.__len__


# Property Decorators - Getters, Setters, and Deleters
# https://youtu.be/jCzT9XFZ5bw
