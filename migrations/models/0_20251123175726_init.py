from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "telegram_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255),
    "full_name" VARCHAR(255),
    "is_premium" BOOL NOT NULL DEFAULT False,
    "age" INT,
    "gender" VARCHAR(50),
    "complaints" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "users"."telegram_id" IS 'Telegram User ID';
COMMENT ON COLUMN "users"."username" IS 'Telegram Username';
COMMENT ON COLUMN "users"."full_name" IS 'Полное имя пользователя';
COMMENT ON COLUMN "users"."is_premium" IS 'Есть ли подписка';
COMMENT ON COLUMN "users"."age" IS 'Возраст';
COMMENT ON COLUMN "users"."gender" IS 'Пол';
COMMENT ON COLUMN "users"."complaints" IS 'Жалобы';
COMMENT ON TABLE "users" IS 'Модель пользователя Telegram.';
CREATE TABLE IF NOT EXISTS "analyses" (
    "id" UUID NOT NULL PRIMARY KEY,
    "original_file_id" VARCHAR(255) NOT NULL,
    "analysis_text" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" BIGINT NOT NULL REFERENCES "users" ("telegram_id") ON DELETE CASCADE
);
COMMENT ON COLUMN "analyses"."original_file_id" IS 'Telegram File ID';
COMMENT ON COLUMN "analyses"."analysis_text" IS 'Результат анализа от LLM';
COMMENT ON COLUMN "analyses"."user_id" IS 'Пользователь';
COMMENT ON TABLE "analyses" IS 'Модель анализа (медицинского документа).';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWW1v2kgQ/iuWP1EpFxljXq6qToKEtFwhnBK4q9qrrMVejBV7Te31Jajiv9++Ga/fCC"
    "Q0cL18WczszHr3eXZmZ8ffVT+woReddxHwVpEbqW+V7yoCPiQPhb4zRQXLZdpDBRjMPKYM"
    "mBbkWrMIh8DCRD4HXgSJyIaRFbpL7AaIav8da0bdom0DstZgbZO1M9oalsL+aKy1pWfW3e"
    "iwts3lSo39WtIgRqpltCQLNpJRZ89AmkCDPyuSMUyVjEbhBXwgnU/gzTldtx1YZOEucn7e"
    "JcbI/RZDEwcOxAsYkoV++UrELrLhA4ySv8s7c+5Cz85sJ9emAzC5iVdLJptOB5dXTJPCNz"
    "OtwIt9lGovV3gRoI16HLv2ObWhfQ5EMAQY2tI2Q7HniR2ZiPiMiQCHMdxM1U4FNpyD2KOb"
    "VX03j5FF96jC3kQb4ze1sH3pW3J0C5EVILr1XYSZK635qtI1cwejr7r40L2pNVpv2CqDCD"
    "sh62SIqGtmCDDgpgzXFMggdB2XuBvp9KBZBuvFAoTlsJbZ5kAmC3gKvIkgxTf1/QTgBLhs"
    "MJhADzoh8JUrMieFk/s4tqoPHkwPIgcvyF+92dwC9p/dG4Y30WKAByQ68bB1Lbp03keBT4"
    "EGIvKZGD7gIsoTIi1HuWB4bIipC+ua5NptyeVFMJKdnT/vE57ScELshsPRbiRu4WzS/zSh"
    "g/hR9M2TqaqNup8Yi/5K9AzH1+8TdYnai+G4l2PUCiHF2wQldF6SHuz6sJzSrGWOT1uYni"
    "cPL8ruzuFIJWuwx8hbieC3Df3BqH876Y7+yFBw2Z30aY+egT+R1lo559oMovw1mHxQ6F/l"
    "8/i6n495G73JZ5XOCcQ4MFFwbwJbitOJNAEmQ2wcwbA0FPZcZ4Aq3FQyyhFKEHt5B63PpT"
    "NZckrhY1yecdBiRrFj7HTobH/5VdcbjbauNVqdptFuNztah+iypRW72lt2S2/wfnCdcz8q"
    "WK9pNjC/Kz3GKPpFvq6CELoO+ghXjLMBmTdAFizhSKSnUzHMz8rVOtm1iTT1iBDcb/IseT"
    "MTkAg0EPNcoHt70b3sq4yKGbDu7kFomxlOaE+gBznJRrfY5et+XkKOPIehSFdB5yzTU3Kr"
    "SGirvlHQBR38OvF82uZKkq88J+c/+DyekZhjMc7e8TNn+HgMFfv2eVn6I0kk3Vi7J5EvFg"
    "i3JfR0p7PnPRJ52eZJ2aXA9ZD5+1Sa00kk8HPyYnNfZDNGR4a2/KgRyTiXNBUpG7dEaDhU"
    "jDkZJsldahlC3439khAVBB4EqKKOkDHM0Tkjlj8qd9h2VDXTCg1HPTkWxM2qyJ8hSTqF+o"
    "727NtWbzweZlL93iB/nZqOev2bWp2xRpRcnIlu0q3ZKXG3yjNEaD8p/z6wn+kS3vx+rEne"
    "Idja61zR60bb6DRaxuY42Ui2nSJFTAkQdlm2XB3FUouTC2FPCSpNbYeY0tQqQwrtypUCAn"
    "/p8bcVYK2u7GStTgHaVqEww2Hm+3VHsF/rMK91mMPUYZb2E4nNWr4Se1Ri2eQLtZvqCkK+"
    "Zg5LgmpPWF59vIEeYNAWiS755vh/K+ysf2Q5pgtD11qoZZ95ec/Z1o+8qc5jNZlqnznwJ8"
    "TKzPL4RYnd48ZB0sXqAsM/MIyEv+2aP0omR/54tTuKL/BFkLjGHiAK9f8mgHVtl5ybaFUC"
    "yPryWTfCEJUkB7/fjq+rUu6NSQ7IKSIL/GK7Fj5TPDfCX08T1i0o0lVvT67zeXTuZKcD9M"
    "q+s7xktX/9L5F8Xuo="
)
