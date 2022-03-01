from django import forms
from django.forms import ModelForm
from .models import RoadsideSales

# Create a Roadside Sales form
class RoadsideSalesForm(ModelForm):
    """ Create a Roadside Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = RoadsideSales
        fields = ('date',
                  'single_egg_price',
                  'half_dozen_eggs_price',
                  'ten_eggs_price',
                  'dozen_eggs_price',
                  'trays_of_eggs_price',
                  'qty_single_eggs_remaining',
                  'qty_single_eggs_added',
                  'qty_half_dozen_egg_boxes_remaining',
                  'qty_half_dozen_egg_boxes_added',
                  'qty_ten_egg_boxes_remaining',
                  'qty_ten_egg_boxes_added',
                  'qty_dozen_egg_boxes_remaining',
                  'qty_dozen_egg_boxes_added',
                  'qty_trays_of_eggs_remaining',
                  'qty_trays_of_eggs_added')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'single_egg_price': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'single-egg-price',
                                                          'name': 'single_egg_price',
                                                          'placeholder':
                                                          "Single Eggs Price",
                                                          'value': ''}),
            'half_dozen_eggs_price': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'half_dozen-eggs-price',
                                                          'name': 'half_dozen_eggs_price',
                                                          'placeholder':
                                                          "Half Dozen Eggs Price",
                                                          'value': ''}),
            'ten_eggs_price': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'ten-eggs-price',
                                                          'name': 'ten_eggs_price',
                                                          'placeholder':
                                                          "10 Eggs Price",
                                                          'value': ''}),
            'dozen_eggs_price': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'dozen-eggs-price',
                                                          'name': 'dozen_eggs_price',
                                                          'placeholder':
                                                          "Dozen Eggs Price",
                                                          'value': ''}),
            'trays_of_eggs_price': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'trays-of-eggs-price',
                                                          'name': 'trays_of_eggs_price',
                                                          'placeholder':
                                                          "Tray of Eggs Price",
                                                          'value': ''}),

            'qty_single_eggs_remaining': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-single-eggs-remaining',
                                                          'name': 'qty_single_eggs_remaining',
                                                          'placeholder':
                                                          "Qty of Single Eggs Remaining",
                                                          'value': ''}),
            'qty_single_eggs_added': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-single-eggs-added',
                                                          'name': 'qty_single_eggs_added',
                                                          'placeholder':
                                                          "Qty of Single Eggs Added",
                                                          'value': ''}),
            'qty_half_dozen_egg_boxes_remaining': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-half-dozen-egg-boxes-remaining',
                                                          'name': 'qty_half_dozen_egg_boxes_remaining',
                                                          'placeholder':
                                                          "Qty of Half Dozens Remaining",
                                                          'value': ''}),
            'qty_half_dozen_egg_boxes_added': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-half-dozen-egg-boxes-added',
                                                          'name': 'qty_half_dozen_egg_boxes_added',
                                                          'placeholder':
                                                          "Qty of Half Dozens Added",
                                                          'value': ''}),
            'qty_ten_egg_boxes_remaining': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-ten-egg-boxes-remaining',
                                                          'name': 'qty_ten_egg_boxes_remaining',
                                                          'placeholder':
                                                          "Qty of 10's Remaining",
                                                          'value': ''}),
            'qty_ten_egg_boxes_added': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-ten-egg-boxes-added',
                                                          'name': 'qty_ten_egg_boxes_added',
                                                          'placeholder':
                                                          "Qty of 10's Added",
                                                          'value': ''}),
            'qty_dozen_egg_boxes_remaining': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-dozen-egg-boxes-remaining',
                                                          'name': 'qty_dozen_egg_boxes_remaining',
                                                          'placeholder':
                                                          "Qty of Dozens Remaining",
                                                          'value': ''}),
            'qty_dozen_egg_boxes_added': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-dozen-egg-boxes-added',
                                                          'name': 'qty_dozen_egg_boxes_added',
                                                          'placeholder':
                                                          "Qty of Dozens Added",
                                                          'value': ''}),
            'qty_trays_of_eggs_remaining': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-trays-of-eggs-remaining',
                                                          'name': 'qty_trays_of_eggs_remaining',
                                                          'placeholder':
                                                          "Qty of Trays Remaining",
                                                          'value': ''}),
            'qty_trays_of_eggs_added': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-trays-of-eggs-added',
                                                          'name': 'qty_trays_of_eggs_added',
                                                          'placeholder':
                                                          "Qty of Trays Added",
                                                          'value': ''}),
        }