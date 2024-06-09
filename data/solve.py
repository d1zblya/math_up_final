import sqlalchemy as sa
from .db_session import SqlAlchemyBase

class Solve(SqlAlchemyBase):
    __tablename__ = 'solve'
    
    id = sa.Column(sa.Integer, primary_key=True) # , autoincrement=True
    easy = sa.Column(sa.String)
    medium = sa.Column(sa.String)
    hard = sa.Column(sa.String)
    easy_sol = sa.Column(sa.String)
    medium_sol = sa.Column(sa.String)
    hard_sol = sa.Column(sa.String)
    
    