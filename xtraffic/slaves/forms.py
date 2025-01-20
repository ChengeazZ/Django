from django import forms
from .models import Slave

from django import forms
from .models import Slave

class SlaveForm(forms.ModelForm):
    class Meta:
        model = Slave
        fields = ['name', 'age', 'durability', 'race', 'photo', 'price', 'description']
