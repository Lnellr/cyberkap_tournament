from django.contrib import admin
from .models import CustomUser, Team, TeamMember, Tournament, TournamentRegistration, Match, Winner

admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Tournament)
admin.site.register(TournamentRegistration)
admin.site.register(Match)
admin.site.register(Winner)