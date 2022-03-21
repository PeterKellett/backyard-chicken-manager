from django import forms
from .models import EggCollection, FeedingTime, CoopCleaning



# Create an Egg Collection form
class EggCollectionForm(forms.ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollection
        fields = '__all__'


# Create a Feeding Time form
class FeedingTimeForm(forms.ModelForm):
    """ Create a feeding time form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = FeedingTime
        fields = ('date', 'food_type',
                  'amount_food_rem', 'amount_food_added',
                  'amount_water_rem', 'amount_water_added',
                  'feeding_notes', 'image_url')

        widgets = {
            'food_type': forms.TextInput(attrs={'id': 'feed-type',
                                                'name': 'feed_type',
                                                'placeholder': 'Feed Name'}),
            'amount_food_rem': forms.NumberInput(attrs={'id': 'amount-food-rem',
                                                        'name': 'amount_food_rem',
                                                        'placeholder': 'Amount of Food Remaining',
                                                        'value': '',
                                                        'step': '1',
                                                        'min': '0',
                                                        'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_food_added': forms.NumberInput(attrs={'id':
                                                          'amount-food-added',
                                                          'name':
                                                          'amount_food_added',
                                                          'placeholder':
                                                          'Amount of Food Added',
                                                          'value': '',
                                                          'step': '1',
                                                          'min': '0',
                                                          'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_water_rem': forms.NumberInput(attrs={'id':
                                                         'amount-water-rem',
                                                         'name': 'amount_water_rem',
                                                         'placeholder':
                                                         'Amount of Water Remaining',
                                                         'value': '',
                                                         'step': '1',
                                                         'min': '0',
                                                         'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_water_added': forms.NumberInput(attrs={'id':
                                                          'amount-water-added',
                                                          'name':
                                                          'amount_water_added',
                                                          'placeholder':
                                                          'Amount of Water Added',
                                                          'value': '',
                                                          'step': '1',
                                                          'min': '0',
                                                          'oninput': 'this.value = Math.abs(this.value)'}),
            'feeding_notes': forms.TextInput(attrs={'id': 'feeding-notes',
                                                           'name': 'feeding_notes',
                                                           'placeholder':
                                                           "Today's Feeding \
                                                           Time Notes"}),
            'image_url': forms.TextInput(attrs={'class': 'class-name',
                                                'id': 'image-url',
                                                'name': 'image_url'})
        }


# Create a Coop Cleaning form
class CoopCleaningForm(forms.ModelForm):
    """ Create a coop cleaning form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = CoopCleaning
        fields = ('date',
                  'disinfected', 'disinfectant',
                  'coop_cleaning_notes', 'image_url')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'disinfected': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                      'id': 'disinfected',
                                                      'name': 'disinfected'}),
            'disinfectant': forms.TextInput(attrs={'class': '',
                                                   'id': 'disinfectant',
                                                   'name': 'disinfectant',
                                                   'placeholder': 'Disinfectant Name'}),
            'coop_cleaning_notes': forms.TextInput(attrs={'id': 'coop-cleaning-notes',
                                                          'name': 'coop_cleaning_notes',
                                                          'placeholder':
                                                          "Today's Coop \
                                                          Cleaning Notes"}),
            'image_url': forms.TextInput(attrs={'class': 'class-name',
                                                'id': 'image-url',
                                                'name': 'image_url'})
        }

