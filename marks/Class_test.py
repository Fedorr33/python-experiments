from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String

engine = create_engine("sqlite:////home/fyodor/Documents/Python/Classing_of_marks/test_marks.db", echo=False)

class Base(DeclarativeBase):
    pass
class Mark(Base):
    __tablename__ = 'marks'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(30))
    mark: Mapped[int] = mapped_column()
