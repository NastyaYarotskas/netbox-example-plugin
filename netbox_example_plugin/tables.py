import django_tables2 as tables
from .models import Animal
from utilities.tables import BaseTable, ToggleColumn, ChoiceFieldColumn


__all__ = (
    'AnimalTable',
)


class AnimalTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    sound = tables.LinkColumn()
    status = ChoiceFieldColumn()

    class Meta(BaseTable.Meta):
        model = Animal
        fields = ('pk', 'name', 'sound', 'status')
