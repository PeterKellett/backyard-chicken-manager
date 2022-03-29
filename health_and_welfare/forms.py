from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Supplements, SupplementsName, Medicines, MedicinesName, Vaccines, VaccinesName, DiseasesName

# Create a Supplement form
class SupplementsForm(forms.ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = Supplements
        fields = "__all__"


# Create a Supplement Name form
class SupplementsNameForm(forms.ModelForm):
    """ Create an Egg Collection form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = SupplementsName
        fields = "__all__"


# Create a Medicine form
class MedicinesForm(forms.ModelForm):
    """ Create a Medicines form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = Medicines
        fields = ('date', 'flock',
                  'medicine_name',
                  'disease_protected_against',
                  'qty_hens', 'qty_chicks',
                  'qty_cocks', 'dose',
                  'vet_administered',
                  'notes', 'images')

        widgets = {
            'date': forms.DateTimeInput,
            'flock': forms.CheckboxInput,
            'medicine_name': forms.TextInput,
            'disease_protected_against': forms.TextInput,
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


# Create a Medicines Name form
class MedicinesNameForm(forms.ModelForm):
    """ Create a Medicines Name form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = MedicinesName
        fields = "__all__"


# Create a Vaccines form
class VaccinesForm(forms.ModelForm):
    """ Create a Vaccines form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = Vaccines
        fields = "__all__"


# Create a Vaccines Name form
class VaccinesNameForm(forms.ModelForm):
    """ Create a Vaccines Name form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = VaccinesName
        fields = "__all__"


# Create a Diseases Name form
class DiseasesNameForm(forms.ModelForm):
    """ Create a Diseases Name form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = DiseasesName
        fields = "__all__"
