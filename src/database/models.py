from tortoise import fields, models


class User(models.Model):
    """
    Модель пользователя Telegram.
    """

    telegram_id = fields.BigIntField(pk=True, description="Telegram User ID")
    username = fields.CharField(
        max_length=255, null=True, description="Telegram Username"
    )
    full_name = fields.CharField(
        max_length=255, null=True, description="Полное имя пользователя"
    )
    is_premium = fields.BooleanField(default=False, description="Есть ли подписка")

    # Поля анкеты
    age = fields.IntField(null=True, description="Возраст")
    gender = fields.CharField(max_length=50, null=True, description="Пол")
    complaints = fields.TextField(null=True, description="Жалобы")

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"

    def __str__(self):
        return f"User(id={self.telegram_id}, username={self.username})"


class Analysis(models.Model):
    """
    Модель анализа (медицинского документа).
    """

    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField(
        "models.User", related_name="analyses", description="Пользователь"
    )
    original_file_id = fields.CharField(max_length=255, description="Telegram File ID")
    analysis_text = fields.TextField(description="Результат анализа от LLM")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "analyses"

    def __str__(self):
        return f"Analysis(id={self.id}, user={self.user_id})"
