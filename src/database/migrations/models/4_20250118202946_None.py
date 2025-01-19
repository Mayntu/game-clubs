from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "club" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT,
    "rating" DOUBLE PRECISION,
    "address" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,
    "is_deleted" BOOL NOT NULL  DEFAULT False
);
CREATE TABLE IF NOT EXISTS "clubimage" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "url" VARCHAR(512) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_deleted" BOOL NOT NULL  DEFAULT False,
    "club_id" UUID NOT NULL REFERENCES "club" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "computerconfig" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "cpu" VARCHAR(255),
    "gpu" VARCHAR(255),
    "ram" VARCHAR(255),
    "keyboard" VARCHAR(255),
    "mouse" VARCHAR(255),
    "headset" VARCHAR(255),
    "armchair" VARCHAR(255),
    "monitor" VARCHAR(255),
    "internet" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "service" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "title" VARCHAR(32) NOT NULL,
    "description" TEXT,
    "icon_url" VARCHAR(512) NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "login" VARCHAR(32) NOT NULL,
    "password" VARCHAR(32) NOT NULL
);
CREATE TABLE IF NOT EXISTS "zone" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT,
    "computers_count" INT,
    "club_id_id" UUID NOT NULL REFERENCES "club" ("id") ON DELETE CASCADE,
    "computer_config_id_id" UUID NOT NULL UNIQUE REFERENCES "computerconfig" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "club_services" (
    "club_id" UUID NOT NULL REFERENCES "club" ("id") ON DELETE CASCADE,
    "service_id" UUID NOT NULL REFERENCES "service" ("id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_club_servic_club_id_99ff52" ON "club_services" ("club_id", "service_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
