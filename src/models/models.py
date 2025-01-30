from tortoise.models import Model
from tortoise import fields
from uuid import uuid4

class Users(Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    login = fields.CharField(max_length=32, null=False)
    password = fields.CharField(max_length=32, null=False)


class Club(Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    title = fields.CharField(max_length=255, null=False)
    description = fields.TextField(null=True)
    rating = fields.FloatField(null=True)
    address = fields.CharField(max_length=255)
    coord_lat = fields.FloatField(null=False, default = 0.0) # X
    coord_lon = fields.FloatField(null=False, default = 0.0) # Y
    city = fields.CharField(max_length=255, null=False)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)
    is_deleted = fields.BooleanField(default=False)

    zones = fields.ReverseRelation["Zone"]
    services = fields.ManyToManyField(
        model_name="models.Service", related_name="clubs", through="club_services"
    )
    images = fields.ReverseRelation["ClubImage"]

class ClubImage(Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    club = fields.ForeignKeyField(
        model_name="models.Club",
        related_name="images",
        on_delete=fields.CASCADE
    )
    url = fields.CharField(max_length=512)
    created_at = fields.DatetimeField(auto_now_add=True)
    is_deleted = fields.BooleanField(default=False)

class Zone(Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    title = fields.CharField(max_length=255, null=False)
    description = fields.TextField(null=True)
    computers_count = fields.IntField(null=True)
    club_id = fields.ForeignKeyField(
        model_name="models.Club",
        related_name="zones",
        on_delete=fields.CASCADE
    )
    computer_config_id = fields.OneToOneField(
        model_name="models.ComputerConfig",
        related_name="zone",
        on_delete=fields.CASCADE
    )

class Service(Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    title = fields.CharField(max_length=32, null=False)
    description = fields.TextField(null=True)
    icon_url = fields.CharField(max_length=512)
    clubs = fields.ReverseRelation["Club"]

class ComputerConfig(Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    cpu = fields.CharField(max_length=255, null=True)
    gpu = fields.CharField(max_length=255, null=True)
    ram = fields.CharField(max_length=255, null=True)
    keyboard = fields.CharField(max_length=255, null=True)
    mouse = fields.CharField(max_length=255, null=True)
    headset = fields.CharField(max_length=255, null=True)
    armchair = fields.CharField(max_length=255, null=True)
    monitor = fields.CharField(max_length=255, null=True)
    internet = fields.CharField(max_length=255, null=True)
    zone = fields.ReverseRelation["Zone"]
