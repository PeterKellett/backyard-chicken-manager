from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import EggCollection, FeedingTime, WateringTime, CoopCleaning, Feeds


# Create an Egg Collection form
class EggCollectionForm(forms.ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollection
        fields = ('date', 'flock', 'qty_egg_trays',
                  'qty_egg_singles', 'qty_eggs_damaged',
                  'qty_eggs_broken', 'qty_eggs_personal_use',
                  'qty_eggs_given_free', 'weight_total_eggs_laid',
                  'notes', 'images'
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
                                                    'oninput': "doCalculations()",
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
                                                      'oninput': "doCalculations()",
                                                      'value': ''}),
            'qty_eggs_damaged': forms.TextInput(attrs={'class':
                                                       'saleable-eggs-input',
                                                       'id':
                                                       'qty-eggs-damaged',
                                                       'name':
                                                       'qty_eggs_damaged',
                                                       'placeholder':
                                                       'Qty of Eggs Damaged (OK for personal use)',
                                                       'oninput': "doCalculations()",
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
                                                      'oninput': "doCalculations()",
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
                                                            'Qty of Eggs Taken for Personal Use',
                                                            'oninput': "doCalculations()",
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
                                                          'oninput': "doCalculations()",
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
                                                             'oninput': "doCalculations()"
                                                             }),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes',
                                           'name': 'notes',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'title': 'Click to add an image',
                                                      'id': 'images-egg-collection',
                                                      'name': 'images_egg_collection'})
        }


FeedingTimeFormSet = modelformset_factory(FeedingTime,
                                          fields=('feed_name',
                                                  'amount_food_rem',
                                                  'amount_food_added'))


# Create a Medicines Name form
class FeedsForm(forms.ModelForm):
    """ Create a Feeds Name form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = Feeds
        fields = "__all__"


# Create a Feeding Time form
class FeedingTimeForm(forms.ModelForm):
    """ Create a feeding time form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = FeedingTime
        fields = ('date', 'flock',
                  'feed_name',
                  'amount_food_rem',
                  'amount_food_added',
                  'feeder_amount',
                  'amount_food_consumed',
                  'notes',
                  'images'
                  )

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
            'feed_name': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                'id': 'feed-name',
                                                'name': 'feed_name',
                                                'value': '',
                                                'onkeyup': "showSuggestionsFeeds(this.value, 'feed-type-label')",
                                                'placeholder':
                                                "Feed Type"}),
            'amount_food_rem': forms.NumberInput(attrs={'id': 'amount-food-rem',
                                                        'name': 'amount_food_rem',
                                                        'placeholder': 'Amount of Food Remaining',
                                                        'value': '',
                                                        'min': '0'}),
            'amount_food_added': forms.NumberInput(attrs={'id':
                                                          'amount-food-added',
                                                          'name':
                                                          'amount_food_added',
                                                          'placeholder':
                                                          'Amount of Food Added',
                                                          'value': '',
                                                          'min': '0'}),
            'feeder_amount': forms.NumberInput(attrs={'id':
                                                      'feeder-amount',
                                                      'name':
                                                      'feeder_amount',
                                                      'placeholder':
                                                      'Amount of Food in Feeder',
                                                      'value': '',
                                                      'min': '0'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes',
                                           'name': 'notes',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-feeding-time',
                                                      'name': 'images_feeding_time'})
        }


# Create a Watering Time form
class WateringTimeForm(forms.ModelForm):
    """ Create a feeding time form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = WateringTime
        fields = ('date',
                  'flock',
                  'amount_water_rem',
                  'amount_water_added',
                  'amount_water_consumed',
                  'water_total',
                  'notes',
                  'images'
                  )

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
            'amount_water_rem': forms.NumberInput(attrs={'id':
                                                         'amount-water-rem',
                                                         'name': 'amount_water_rem',
                                                         'placeholder':
                                                         'Amount of Water Remaining',
                                                         'value': '',
                                                         'min': '0'}),
            'amount_water_added': forms.NumberInput(attrs={'id':
                                                           'amount-water-added',
                                                           'name':
                                                           'amount_water_added',
                                                           'placeholder':
                                                           'Amount of Water Added',
                                                           'value': '',
                                                           'min': '0'}),
            'water_total': forms.NumberInput(attrs={'id':
                                                           'water-total',
                                                           'name':
                                                           'water_total',
                                                           'placeholder':
                                                           'Amount of Water in Total',
                                                           'value': '',
                                                           'min': '0'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes',
                                           'name': 'notes',
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
                  'disinfectant_name',
                  'notes', 'images'
                  )

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
            'disinfected': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                      'id': 'disinfected',
                                                      'name': 'disinfected'}),
            'disinfectant_name': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                        'id': 'disinfectant-name',
                                                        'name': 'disinfectant_name',
                                                        'value': '',
                                                        'onkeyup': "showSuggestionsDisinfectants (this.value, 'disinfectant-type-label')",
                                                        'placeholder': 'Disinfectant Name'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes',
                                           'name': 'notes',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-coop-cleaning',
                                                      'name': 'images_coop_cleaning'})
        }
