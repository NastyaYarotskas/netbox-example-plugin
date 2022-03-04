import django_tables2 as tables
from .models import Animal
from utilities.tables import BaseTable, ToggleColumn


class AnimalTable(BaseTable):

    id = tables.LinkColumn()
    name = tables.LinkColumn()
    sound = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Animal
        fields = ('id', 'name', 'sound')
