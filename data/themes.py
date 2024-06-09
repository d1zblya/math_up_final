from .db_session import SqlAlchemyBase
import sqlalchemy as sa

class Themes(SqlAlchemyBase):
    '''Форма создания таблицы тем'''
    __tablename__ = 'themes'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)