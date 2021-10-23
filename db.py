#!/usr/bin/env python3
"""Provide access to DB."""

from sqlite3 import connect as sql_connect
from sqlite3 import Error as sql_error

import db_commands as dbc


class dataAccess:
    """Provide access to DB."""

    def __init__(self, path: str = './exp.sqlite') -> None:
        self.con = None
        try:
            self.con = sql_connect(path)
        except sql_error as e:
            print("Error {}".format(e))
        self._create_tables()

    def _execute_query(self, query, **kwargs):
        """Execute the query on SQL."""
        cursor = self.con.cursor()
        cursor.execute(query, kwargs)
        self.con.commit()

    def _read_info(self, query, **kwargs):
        """Read info from db."""
        cursor = self.con.cursor()
        result = None
        try:
            cursor.execute(query, kwargs)
            result = cursor.fetchall()
            return result
        except sql_error as e:
            print("Error {}".format(e))

    def _create_tables(self):
        """Create the initial tables main and notes."""
        self._execute_query(dbc.create_table)

    def add_exp(self, gen_alg: str, ex_time: float, q_size: int, not_aff: bool, one_simple: bool):
        """Add new experiment with given fields."""
        self._execute_query(
            dbc.add_new_exp,
            gen_alg=gen_alg,
            ex_time=ex_time,
            q_size=q_size,
            not_aff=not_aff,
            one_simple=one_simple
        )
    
    def get_exp(self):
        """Get all experiments"""
        return self._read_info(dbc.get_all_exp)
