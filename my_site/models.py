from my_site import db
from sqlalchemy.orm import Mapped, mapped_column

class ClassMembers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column()
    middlename: Mapped[str] = mapped_column()
    lastname: Mapped[str] = mapped_column()