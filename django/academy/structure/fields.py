from django.core.exceptions import ValidationError
from django.db import models


class PositiveTinyAutoField(models.AutoField):
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if not (0 <= value < 256):
            raise ValidationError('value for this field should be between 0 and 255')
        return value

    def db_type(self, connection):
        return 'tinyint unsigned auto_increment'

    def rel_db_type(self, connection):
        return 'tinyint unsigned'


class PositiveMediumAutoField(models.AutoField):
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if not (0 <= value < 16777216):
            raise ValidationError('value for this field should be between 0 and 16777215')
        return value

    def db_type(self, connection):
        return 'tinyint unsigned auto_increment'

    def rel_db_type(self, connection):
        return 'tinyint unsigned'


