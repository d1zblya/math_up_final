import sqlalchemy as sa
from .db_session import SqlAlchemyBase

class Theory(SqlAlchemyBase):
    '''Форма создания таблицы теории'''
    __tablename__ = 'theory'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    en_name = sa.Column(sa.String)
    theory = sa.Column(sa.String)
    example = sa.Column(sa.BLOB)
    
    