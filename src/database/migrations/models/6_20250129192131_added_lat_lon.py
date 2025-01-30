from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "club" ADD "coord_lat" DOUBLE PRECISION NOT NULL  DEFAULT 0;
        ALTER TABLE "club" ADD "coord_lon" DOUBLE PRECISION NOT NULL  DEFAULT 0;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "club" DROP COLUMN "coord_lat";
        ALTER TABLE "club" DROP COLUMN "coord_lon";"""
