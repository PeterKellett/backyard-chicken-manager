from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import EggCollection, FeedingTime, CoopCleaning, Feeds


# Create an Egg Collection form
class EggCollectionForm(forms.ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollection
        fields = ('date', 'flock', 'qty_egg_trays',
                  'qty_egg_singles', 'qty_eggs_damaged',
                  'qty_eggs_damaged', 'qty_eggs_broken',
                  'qty_eggs_personal_use', 'qty_eggs_given_free',
                  'weight_total_eggs_laid', 'notes', 'images'
                  )

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
            'qty_egg_trays': forms.TextInput(attrs={'class':
                                                    'egg-collection-qty-input \
                                                    saleable-eggs-input \
                                                    average-weight-input',
                                                    'id': 'qty-egg-trays',
                                                    'name': 'qty_egg_trays',
                                                    'placeholder':
                                                    'Qty Laid - Trays',
                                                    'value': ''}),
            'qty_egg_singles': forms.TextInput(attrs={'class':
                                                      'egg-collection-qty-input \
                                                      saleable-eggs-input \
                                                      average-weight-input',
                                                      'id':
                                                      'qty-egg-singles',
                                                      'name':
                                                      'qty_egg_singles',
                                                      'placeholder':
                                                      'Qty Laid - Single',
                                                      'value': ''}),
            'qty_total_eggs_laid': forms.TextInput(attrs={'class':
                                                          'text-end \
                                                          h-style-input',
                                                          'id':
                                                          'qty-total-eggs-laid',
                                                          'name':
                                                          'qty_total_eggs_laid',
                                                          'placeholder':
                                                          'Qty Laid - Single',
                                                          'value': '0',
                                                          'disabled': 'true'}),
            'qty_eggs_damaged': forms.TextInput(attrs={'class':
                                                       'saleable-eggs-input',
                                                       'id':
                                                       'qty-eggs-damaged',
                                                       'name':
                                                       'qty_eggs_damaged',
                                                       'placeholder':
                                                       'Qty of Eggs Damaged (OK for personal use)',
                                                       'value': '',
                                                       'step': '1',
                                                       'min': '0'}),
            'qty_eggs_broken': forms.TextInput(attrs={'class':
                                                      'saleable-eggs-input \
                                                      average-weight-input',
                                                      'id':
                                                      'qty-eggs-broken',
                                                      'name':
                                                      'qty_eggs_broken',
                                                      'placeholder':
                                                      'Qty of Eggs Broken (Unuseable)',
                                                      'value': '',
                                                      'step': '1',
                                                      'min': '0'}),
            'qty_eggs_personal_use': forms.TextInput(attrs={'class':
                                                            'saleable-eggs-input',
                                                            'id':
                                                            'qty-eggs-personal-use',
                                                            'name':
                                                            'qty_eggs_personal_use',
                                                            'placeholder':
                                                            'Qty of Eggs Taken for Personal Use)',
                                                            'value': '',
                                                            'min': '0',
                                                            'step': '1'}),
            'qty_eggs_given_free': forms.TextInput(attrs={'class':
                                                          'saleable-eggs-input',
                                                          'id':
                                                          'qty-eggs-given-free',
                                                          'name':
                                                          'qty_eggs_given_free',
                                                          'placeholder':
                                                          'Qty of Eggs Given Away Free',
                                                          'value': '',
                                                          'min': '0',
                                                          'step': '1'}),
            'weight_total_eggs_laid': forms.TextInput(attrs={'class':
                                                             'average-weight-input',
                                                             'id':
                                                             'weight-total-eggs-laid',
                                                             'name':
                                                             'weight_total_eggs_laid',
                                                             'placeholder':
                                                             'Laid Eggs Weight (excl. Broken)',
                                                             'value': '',
                                                             'min': '0',
                                                             'oninput':
                                                             'this.value = \
                                                             Math.abs(this.value)'
                                                             }),
            'avg_egg_weight': forms.TextInput(attrs={'class':
                                                     'text-end h-style-input',
                                                     'id':
                                                     'avg-egg-weight',
                                                     'name':
                                                     'avg_egg_weight',
                                                     'placeholder':
                                                     'Total weight of \
                                                     eggs laid (excl. \
                                                     Broken)',
                                                     'value': '0',
                                                     'min': '0',
                                                     'disabled': 'true'}),
            'qty_saleable_eggs': forms.TextInput(attrs={'class':
                                                        'text-end h-style-input',
                                                        'id':
                                                        'qty-saleable-eggs',
                                                        'name':
                                                        'qty_saleable_eggs',
                                                        'placeholder':
                                                        'Eggs Saleable Qty',
                                                        'value': '0',
                                                        'disabled': 'true'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-egg-collection',
                                           'name': 'notes_eggs_collection',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'title': 'Click to add an image',
                                                      'id': 'images-egg-collection',
                                                      'name': 'images_egg_collection'})
        }


FeedingTimeFormSet = modelformset_factory(FeedingTime,
                                          fields=('feed_type',
                                                  'amount_food_rem',
                                                  'amount_food_added'))


# Create a Feeding Time form
class FeedingTimeForm(forms.ModelForm):
    """ Create a feeding time form """

    class Meta:
        """ Meta Class Docstring here as required """
        model = FeedingTime
        fields = ('date', 'flock', 'feed_type',
                  'food_total_setup',
                  'amount_food_rem', 'amount_food_added',
                  'water_total_setup',
                  'amount_water_rem', 'amount_water_added',
                  'notes', 'images'
                  )

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
            'food_total_setup': forms.TextInput(attrs={'id': 'food-total-setup',
                                                       'name': 'food_total_setup',
                                                       'placeholder': 'Total Feed Amount',
                                                       'value': '',
                                                       'step': '1',
                                                       'min': '0',
                                                       'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_food_rem': forms.TextInput(attrs={'id': 'amount-food-rem',
                                                      'name': 'amount_food_rem',
                                                      'placeholder': 'Amount of Food Remaining',
                                                      'value': '',
                                                      'step': '1',
                                                      'min': '0',
                                                      'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_food_added': forms.TextInput(attrs={'id':
                                                        'amount-food-added',
                                                        'name':
                                                        'amount_food_added',
                                                        'placeholder':
                                                        'Amount of Food Added',
                                                        'value': '',
                                                        'step': '1',
                                                        'min': '0',
                                                        'oninput': 'this.value = Math.abs(this.value)'}),
            'water_total_setup': forms.TextInput(attrs={'id': 'water-total-setup',
                                                       'name': 'water_total_setup',
                                                       'placeholder': 'Total Water Amount',
                                                       'value': '',
                                                       'step': '1',
                                                       'min': '0',
                                                       'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_water_rem': forms.TextInput(attrs={'id':
                                                       'amount-water-rem',
                                                       'name': 'amount_water_rem',
                                                       'placeholder':
                                                       'Amount of Water Remaining',
                                                       'value': '',
                                                       'step': '1',
                                                       'min': '0',
                                                       'oninput': 'this.value = Math.abs(this.value)'}),
            'amount_water_added': forms.TextInput(attrs={'id':
                                                         'amount-water-added',
                                                         'name':
                                                         'amount_water_added',
                                                         'placeholder':
                                                         'Amount of Water Added',
                                                         'value': '',
                                                         'step': '1',
                                                         'min': '0',
                                                         'oninput': 'this.value = Math.abs(this.value)'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-feeding-time',
                                           'name': 'notes_feeding_time',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-feeding-time',
                                                      'name': 'images_feeding_time'})
        }


# Create a Coop Cleaning form
class CoopCleaningForm(forms.ModelForm):
    """ Create a coop cleaning form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = CoopCleaning
        fields = ('date', 'coop', 'disinfected',
                  'disinfectant',
                  'notes', 'images'
                  )

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
            'disinfected': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                      'id': 'disinfected',
                                                      'name': 'disinfected'}),
            'disinfectant': forms.TextInput(attrs={'class': '',
                                                   'id': 'disinfectant',
                                                   'name': 'disinfectant',
                                                   'placeholder': 'Disinfectant Name'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-coop-cleaning',
                                           'name': 'notes_coop_cleaning',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-coop-cleaning',
                                                      'name': 'images_coop_cleaning'})
        }
