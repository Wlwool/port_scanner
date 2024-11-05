from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()


class ScanReport(Base):
    __tablename__ = 'scan_reports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)

def create_database():
    Base.metadata.create_all(engine)

def save_report(report):
    """
    Сохраняет открытые порты в базу данных
    """
    for port in report["open_ports"]:
        new_entry = ScanReport(host=report["host"], port=port, timestamp=report["timestamp"])
        session.add(new_entry)
    session.commit()
