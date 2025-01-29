from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
)

from shop_app.core.config import database_url  # Импортируем URL базы данных


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,  # Логирование SQL-запросов (удобно для отладки)
        pool_size: int = 5,  # Размер пула соединений
        max_overflow: int = 10,  # Максимальное количество соединений сверх пула
    ) -> None:
        # Создаем асинхронный движок для работы с базой данных
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,  # Логирование SQL-запросов
            pool_size=pool_size,  # Размер пула соединений
            max_overflow=max_overflow,  # Максимальное количество соединений сверх пула
        )

        # Создаем фабрику сессий
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,  # Отключаем автоматический flush
            autocommit=False,  # Отключаем автоматический commit
            expire_on_commit=False,  # Отключаем expire объектов после commit
        )

    async def dispose(self) -> None:
        """Закрывает все соединения с базой данных."""
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Генератор асинхронных сессий для использования в зависимостях."""
        async with self.session_factory() as session:
            yield session


# Создаем экземпляр DatabaseHelper с настройками из config.py
db_helper = DatabaseHelper(
    url=database_url,  # Используем URL базы данных из настроек
    echo=True,  # Включаем логирование SQL-запросов (можно отключить в продакшене)
    pool_size=5,  # Размер пула соединений
    max_overflow=10,  # Максимальное количество соединений сверх пула
)








