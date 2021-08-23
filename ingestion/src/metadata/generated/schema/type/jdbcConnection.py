# generated by datamodel-codegen:
#   filename:  schema/type/jdbcConnection.json
#   timestamp: 2021-08-23T15:40:00+00:00

from __future__ import annotations

from pydantic import AnyUrl, BaseModel, Field


class DriverClass(BaseModel):
    __root__: str = Field(..., description='Type used for JDBC driver class')


class ConnectionUrl(BaseModel):
    __root__: AnyUrl = Field(..., description='Type used for JDBC connection URL')


class JdbcInfo(BaseModel):
    driverClass: DriverClass
    connectionUrl: ConnectionUrl


class JdbcConnection(BaseModel):
    driverClass: DriverClass = Field(..., description='JDBC driver class')
    connectionUrl: ConnectionUrl = Field(..., description='JDBC connection URL')
    userName: str = Field(..., description='Login user name.')
    password: str = Field(..., description='Login password.')
