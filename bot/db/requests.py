from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from bot.db.models import Users


async def register_check(db_session: AsyncSession, user_id: int):
    async with db_session() as session:
        result = await session.execute(select(Users).where(Users.user_id == user_id))
        user = result.one_or_none()
        if user is not None:
            return True
        else:
            return False


async def add_user(db_session: AsyncSession, user_id: int):
    async with db_session() as session:
        user = Users(user_id=user_id)
        await session.merge(user)
        await session.commit()


async def set_active(db_session: AsyncSession, user_id: int, active):
    async with db_session() as session:
        stmt = await session.execute(update(Users).where(Users.user_id == user_id).values(active=active))
        await session.commit()
        return stmt


async def get_users(db_session: AsyncSession):
    async with db_session() as session:
        stmt = await session.execute(select(Users.user_id, Users.active))
        return stmt.fetchall()