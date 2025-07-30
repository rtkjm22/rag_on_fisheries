from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# ───── .env 読み込み ─────
load_dotenv()

# ───── Alembic config ─────
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ───── パス追加 ─────
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ───── モデルのBase読み込み ─────
from app.models.db import Base

target_metadata = Base.metadata

# ───── .envからURLを渡す ─────
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))  # type: ignore


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
