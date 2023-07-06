import sqlite3
from sqlalchemy import create_engine, Column, Integer, Text, and_, or_
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class DictRowFactory(dict):
    def __init__(self, __cursor: sqlite3.Cursor, __data: tuple):
        super().__init__(sqlite3.Row(__cursor, __data))


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)
    job_title = Column(Text)
    department = Column(Text)
    manager_id = Column(Integer)
    years_of_service = Column(Integer)
    pay_band = Column(Integer)
    on_leave = Column(Integer)

    def __repr__(self) -> str:
        return f'Employee(id={self.id}, name="{self.name}", age={self.age}, job_title="{self.job_title}", department="{self.department}", manager_id={self.manager_id}, years_of_service={self.years_of_service}, pay_band={self.pay_band}, on_leave={self.on_leave})'

    def __eq__(self, other_employee) -> bool:
        if not isinstance(other_employee, Employee):
            return False
        return bool(self.id == other_employee.id)


def select_all_employees_using_sqlite3() -> list[dict]:
    return []


def select_all_employees_using_sqlalchemy() -> list[Employee]:
    return []


def select_employee_with_id_51708_using_sqlite3() -> dict | None:
    return None


def select_employee_with_id_51708_using_sqlalchemy() -> Employee | None:
    return None


def select_first_10_employees_using_sqlite3() -> list[dict]:
    return []


def select_first_10_employees_using_sqlalchemy() -> list[Employee]:
    return []


def select_all_employees_in_ascending_name_order_using_sqlite3() -> list[dict]:
    return []


def select_all_employees_in_ascending_name_order_using_sqlalchemy() -> list[Employee]:
    return []


def select_all_employees_in_descending_name_order_using_sqlite3() -> list[dict]:
    return []


def select_all_employees_in_descending_name_order_using_sqlalchemy() -> list[Employee]:
    return []


def select_employees_in_consulting_department_using_sqlite3() -> list[dict]:
    return []


def select_employees_in_consulting_department_using_sqlalchemy() -> list[Employee]:
    return []


def select_employees_below_pay_band_5_using_sqlite3() -> list[dict]:
    return []


def select_employees_below_pay_band_5_using_sqlalchemy() -> list[Employee]:
    return []


def select_employees_below_pay_band_5_and_with_less_than_3_years_of_service_using_sqlite3() -> (
    list[dict]
):
    return []


def select_employees_below_pay_band_5_and_with_less_than_3_years_of_service_using_sqlalchemy() -> (
    list[Employee]
):
    return []


def select_employees_with_id_51708_or_manager_id_51708_using_sqlite3() -> list[dict]:
    return []


def select_employees_with_id_51708_or_manager_id_51708_using_sqlalchemy() -> (
    list[Employee]
):
    return []


def select_distinct_non_null_departments_using_sqlite3() -> list[str]:
    return []


def select_distinct_non_null_departments_using_sqlalchemy() -> list[str]:
    return []


if __name__ == "__main__":
    # Try out your functions here
    pass
