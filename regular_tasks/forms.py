from django import forms
from django.forms import ModelForm
from .models import EggCollection


# Create an Egg Collection form
class EggCollectionForm(ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollection
        fields = ('date', 'qty_total_trays',
                  'qty_total_single', 'qty_total_laid',
                  'qty_damaged', 'qty_broken', 'qty_personal_use',
                  'qty_given_free', 'weight_total_laid',
                  'avg_egg_weight', 'qty_saleable_eggs',
                  'egg_collection_notes', 'image_url')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'qty_total_trays': forms.NumberInput(attrs={'class':
                                                        'egg-collection-qty-input \
                                                        saleable-eggs-input \
                                                        average-weight-input',
                                                        'id': 'qty-trays',
                                                        'name': 'qty_trays',
                                                        'placeholder':
                                                        'Qty Laid Trays',
                                                        'value': ''}),
            'qty_total_single': forms.NumberInput(attrs={'class':
                                                         'egg-collection-qty-input \
                                                         saleable-eggs-input \
                                                         average-weight-input',
                                                         'id':
                                                         'qty-singles',
                                                         'name':
                                                         'qty_singles',
                                                         'placeholder':
                                                         'Qty Laid - Single',
                                                         'value': ''}),
            'qty_total_laid': forms.NumberInput(attrs={'class':
                                                       'text-end \
                                                        h-style-input',
                                                       'id':
                                                       'total-eggs-laid',
                                                       'name':
                                                       'total_eggs_laid',
                                                       'placeholder':
                                                       'Qty Laid - Single',
                                                       'value': '0'}),
            'qty_damaged': forms.NumberInput(attrs={'class':
                                                    'saleable-eggs-input',
                                                    'id':
                                                    'eggs-damaged',
                                                    'name':
                                                    'eggs_damaged',
                                                    'placeholder':
                                                    'Qty of Eggs Damaged (OK \
                                                    for personal use)',
                                                    'value': '',
                                                    'step': '1',
                                                    'min': '0'}),
            'qty_broken': forms.NumberInput(attrs={'class':
                                                   'saleable-eggs-input \
                                                   average-weight-input',
                                                   'id':
                                                   'eggs-broken',
                                                   'name':
                                                   'eggs_broken',
                                                   'placeholder':
                                                   'Qty of Eggs Broken \
                                                   (Unuseable)',
                                                   'value': '',
                                                   'step': '1',
                                                   'min': '0'}),
            'qty_personal_use': forms.NumberInput(attrs={'class':
                                                         'saleable-eggs-input',
                                                         'id':
                                                         'eggs-personal-use',
                                                         'name':
                                                         'eggs_personal_use',
                                                         'placeholder':
                                                         'Qty of Eggs Taken \
                                                         for Personal Use)',
                                                         'value': '',
                                                         'step': '1',
                                                         'min': '0'}),
            'qty_given_free': forms.NumberInput(attrs={'class':
                                                       'saleable-eggs-input',
                                                       'id':
                                                       'eggs-given-free',
                                                       'name':
                                                       'eggs_given_free',
                                                       'placeholder':
                                                       'Qty of Eggs Given \
                                                       Away Free',
                                                       'value': '',
                                                       'step': '1',
                                                       'min': '0'}),
            'weight_total_laid': forms.NumberInput(attrs={'class':
                                                          'average-weight-input',
                                                          'id':
                                                          'total-weight-laid',
                                                          'name':
                                                          'total_weight_laid',
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
                                                       'average-egg-weight',
                                                       'name':
                                                       'average_egg_weight',
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
            'egg_collection_notes': forms.TextInput(attrs={'name': 'notes',
                                                           'placeholder':
                                                           "Today's Egg \
                                                           Collection Notes"}),
            'image_url': forms.TextInput(attrs={'class': 'class-name'})
        }
