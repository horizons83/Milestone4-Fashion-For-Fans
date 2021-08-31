from django import forms
from .models import Product, Category, Team


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        teams = Team.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names = [(t.id, t.get_friendly_name()) for t in teams]

        self.fields['category', 'team'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
