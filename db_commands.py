"""DB commands"""

create_table = """
CREATE TABLE IF NOT EXISTS experiments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  gen_alg TEXT,
  ex_time FLOAT NOT NULL,
  q_size INT NOT NULL,
  aff BOOL,
  one_simple BOOL
);
"""

add_new_exp = """
INSERT INTO
  experiments (gen_alg, ex_time, q_size, aff, one_simple)
VALUES
  (:gen_alg,
  :ex_time,
  :q_size,
  :aff,
  :one_simple);
"""
