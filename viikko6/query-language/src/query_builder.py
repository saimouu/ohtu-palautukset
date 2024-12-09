from matchers import And, PlaysIn, HasAtLeast, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, query=All()) -> None:
        self.query = query

    def build(self):
        return self.query
    
    def plays_in(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))
