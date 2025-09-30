from sqlalchemy import create_engine, Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
import os

# Добавляем родительскую директорию в путь для импорта config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

Base = declarative_base()
engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


class ScanReport(Base):
    __tablename__ = 'scan_reports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    scan_duration = Column(Float, nullable=True)
    total_ports = Column(Integer, nullable=True)
    timeout = Column(Float, nullable=True)
    scan_delay = Column(Float, nullable=True)


def create_database():
    """Создание базы данных и таблиц"""
    try:
        Base.metadata.create_all(engine)
        print("✅ База данных создана/подключена")
    except Exception as e:
        print(f"❌ Ошибка создания базы данных: {e}")
        raise


def save_report(report):
    """
    Сохраняет результаты сканирования в базу данных
    """
    try:
        for port in report["open_ports"]:
            new_entry = ScanReport(
                host=report["host"], 
                port=port, 
                timestamp=report["timestamp"],
                scan_duration=report.get("scan_duration"),
                total_ports=report.get("total_ports"),
                timeout=report.get("settings", {}).get("timeout"),
                scan_delay=report.get("settings", {}).get("scan_delay")
            )
            session.add(new_entry)
        
        session.commit()
        print(f"💾 Сохранено {len(report['open_ports'])} записей в базу данных")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка сохранения в базу данных: {e}")
        raise


def get_reports_by_host(host: str):
    """Получение всех отчетов по хосту"""
    try:
        reports = session.query(ScanReport).filter(ScanReport.host == host).all()
        return reports
    except Exception as e:
        print(f"❌ Ошибка получения отчетов: {e}")
        return []


def get_all_reports():
    """Получение всех отчетов"""
    try:
        reports = session.query(ScanReport).all()
        return reports
    except Exception as e:
        print(f"❌ Ошибка получения отчетов: {e}")
        return []


def clear_reports():
    """Очистка всех отчетов"""
    try:
        session.query(ScanReport).delete()
        session.commit()
        print("🗑️ Все отчеты удалены")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка удаления отчетов: {e}")
        raise
