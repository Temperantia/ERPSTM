# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Action(Base):
    __tablename__ = 'action'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

    role = relationship('Role', secondary='action_role')


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(45))


class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    address = Column(String(45))
    legal_status = Column(String(45))
    turnover = Column(Integer)
    headcounts = Column(Integer)
    authorized = Column(TINYINT)
    status = Column(String(45))


t_action_role = Table(
    'action_role', metadata,
    Column('id_action', ForeignKey('action.id'), primary_key=True, nullable=False, index=True),
    Column('id_role', ForeignKey('role.id'), primary_key=True, nullable=False, index=True)
)


class Request(Base):
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    id_supplier = Column(ForeignKey('supplier.id'), nullable=False, index=True)

    supplier = relationship('Supplier')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    lastname = Column(String(70))
    firstname = Column(String(70))
    internal = Column(TINYINT)
    id_supplier = Column(ForeignKey('supplier.id'), nullable=False, index=True)
    id_role = Column(ForeignKey('role.id'), nullable=False, index=True)

    role = relationship('Role')
    supplier = relationship('Supplier')