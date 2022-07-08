from .models import Agendamentos
from django.forms import ModelForm

class AgendamentosForm(ModelForm):
    class Meta:
        model = Agendamentos
        fields = "__all__"
