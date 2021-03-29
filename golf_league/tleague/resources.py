from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *


class TeamNameResource(resources.ModelResource):
    team_name = fields.Field(
       column_name='team_name',
       attribute='team_name',
       widget=ForeignKeyWidget(Player, 'team_name')
       )

    class Meta:
        fields = ('team',)



class TeamResource(resources.ModelResource):
    team = fields.Field(
        column_name='team',
        attribute='team',
        widget=ForeignKeyWidget(Team, 'team')
        )
    class Meta:
        model = Team
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('team',)
        fields = ('team','points',)
