from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Team, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        teams = Team.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in teams]

        self.fields['team'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ Creates form based on review model for registered users """

    class Meta:
        model = Review
        fields = (
            'review_title',
            'review',
            'rating',
            )
