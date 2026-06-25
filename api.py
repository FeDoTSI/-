from django.contrib.gis.db import models
import uuid

class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255, db_index=True)

class Entrance(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="entrances")
    number = models.PositiveSmallIntegerField()

class Floor(models.Model):
    entrance = models.ForeignKey(Entrance, on_delete=models.CASCADE, related_name="floors")
    number = models.SmallIntegerField()
