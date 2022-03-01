from django import forms
from django.forms import ModelForm
from .models import EggCollection, FeedingTime, CoopCleaning


# Create an Egg Collection form
class EggCollectionForm(ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollection
        fields = ('date', 'qty_egg_trays',
                  'qty_egg_singles', 'qty_total_eggs_laid',
                  'qty_eggs_damaged', 'qty_eggs_broken', 'qty_eggs_personal_use',
                  'qty_eggs_given_free', 'weight_total_eggs_laid',
                  'avg_egg_weight', 'qty_saleable_eggs',
                  'egg_collection_notes')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'qty_egg_trays': forms.NumberInput(attrs={'class':
                                                      'egg-collection-qty-input \
                                                      saleable-eggs-input \
                                                      average-weight-input',
                                                      'id': 'qty-egg-trays',
                                                      'name': 'qty_egg_trays',
                                                      'placeholder':
                                                      'Qty Laid Trays',
                                                      'value': ''}),
            'qty_egg_singles': forms.NumberInput(attrs={'class':
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
            'qty_total_eggs_laid': forms.NumberInput(attrs={'class':
                                                            'text-end \
                                                            h-style-input',
                                                            'id':
                                                            'qty-total-eggs-laid',
                                                            'name':
                                                            'qty_total_eggs_laid',
                                                            'placeholder':
                                                            'Qty Laid - Single',
                                                            'value': '0'}),
            'qty_eggs_damaged': forms.NumberInput(attrs={'class':
                                                         'saleable-eggs-input',
                                                         'id':
                                                         'qty-eggs-damaged',
                                                         'name':
                                                         'qty_eggs_damaged',
                                                         'placeholder':
                                                         'Qty of Eggs Damaged (OK \
                                                         for personal use)',
                                                         'value': '',
                                                         'step': '1',
                                                         'min': '0'}),
            'qty_eggs_broken': forms.NumberInput(attrs={'class':
                                                   'saleable-eggs-input \
                                                   average-weight-input',
                                                   'id':
                                                   'qty-eggs-broken',
                                                   'name':
                                                   'qty_eggs_broken',
                                                   'placeholder':
                                                   'Qty of Eggs Broken \
                                                   (Unuseable)',
                                                   'value': '',
                                                   'step': '1',
                                                   'min': '0'}),
            'qty_eggs_personal_use': forms.NumberInput(attrs={'class':
                                                              'saleable-eggs-input',
                                                              'id':
                                                              'qty-eggs-personal-use',
                                                              'name':
                                                              'qty_eggs_personal_use',
                                                              'placeholder':
                                                              'Qty of Eggs Taken \
                                                              for Personal Use)',
                                                              'value': '',
                                                              'min': '0',
                                                              'step': '1'}),
            'qty_eggs_given_free': forms.NumberInput(attrs={'class':
                                                            'saleable-eggs-input',
                                                            'id':
                                                            'qty-eggs-given-free',
                                                            'name':
                                                            'qty_eggs_given_free',
                                                            'placeholder':
                                                            'Qty of Eggs Given \
                                                            Away Free',
                                                            'value': '',
                                                            'min': '0',
                                                            'step': '1'}),
            'weight_total_eggs_laid': forms.NumberInput(attrs={'class':
                                                               'average-weight-input',
                                                               'id':
                                                               'weight-total-eggs-laid',
                                                               'name':
                                                               'weight_total_eggs_laid',
                                                               'placeholder':
                                                               'Total weight of \
                                                               eggs laid \
                                                               (excl. Broken)',
                                                               'value': '',
                                                               'min': '0',
                                                               'oninput':
                                                               'this.value = \
                                                               Math.abs(this.value)'
                                                               }),
            'avg_egg_weight': forms.NumberInput(attrs={'class':
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
                                                       'min': '0'}),
            'qty_saleable_eggs': forms.NumberInput(attrs={'class':
                                                          'text-end \
                                                          h-style-input',
                                                          'id':
                                                          'qty-saleable-eggs',
                                                          'name':
                                                          'qty_saleable_eggs',
                                                          'placeholder':
                                                          'Eggs Saleable Qty',
                                                          'value': '0'}),
            'egg_collection_notes': forms.TextInput(attrs={'id': 'egg-collection-notes',
                                                           'name': 'egg_collection_notes',
                                                           'placeholder':
                                                           "Today's Egg \
                                                           Collection Notes"}),
            # 'image_url': forms.TextInput(attrs={'class': 'class-name',
            #                                     'id': 'image-url',
            #                                     'name': 'image_url'})
        }


# Create a Feeding Time form
class FeedingTimeForm(ModelForm):
    """ Create a feeding time form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = FeedingTime
        fields = ('date', 'food_type',
                  'amount_food_rem', 'amount_food_added',
                  'amount_water_rem', 'amount_water_added',
                  'feeding_notes', 'image_url')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
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
class CoopCleaningForm(ModelForm):
    """ Create a coop cleaning form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = CoopCleaning
        fields = ('date',
                  'disinfected', 'disinfectant',
                  'coop_cleaning_notes', 'image_url')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'disinfected': forms.CheckboxInput(attrs={'class': 'col-css-element',
                                                      'name': 'disinfected'}),
            'disinfectant': forms.TextInput(attrs={'id': 'disinfectant',
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

