from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Supplements, SupplementsName, Medicines, MedicinesName, Vaccines, VaccinesName, DiseasesName


# Create a Supplement form
class SupplementsForm(forms.ModelForm):
    """ Create an Supplement Administration form """

    # def __init__(self, *args, **kwargs):
    #     super(MedicinesForm, self).__init__(*args, **kwargs)
    #     self.fields['administration_method'].empty_label = 'Select Administration Method'
    #     self.fields['administration_method'].initial = "Select Administration Method"
    #     self.fields['administration_method'].show_hidden_initial = True

    class Meta:
        """ Meta Class Docstring here as required """
        model = Supplements
        fields = ('date',
                  'flock',
                  'supplement_name',
                  'qty_hens',
                  'qty_chicks',
                  'qty_cocks',
                  'dosage_amount',
                  'vet_administered',
                  'vet_name',
                  'notes',
                  'images')

        widgets = {
            'date': forms.DateTimeInput,
            'flock': forms.CheckboxInput,
            'supplement_name': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                      'id': 'supplement-name',
                                                      'name': 'supplement_name',
                                                      'value': '',
                                                      'onclick': "displaySelectLabel('supplement-type-label')",
                                                      'onkeyup': "showSuggestionsSupplements(this.value, 'supplement-type-label')",
                                                      'placeholder':
                                                      "Supplement Name"}),
            'dosage_amount': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                    'id': 'dosage-amount',
                                                    'name': 'dosage_amount',
                                                    'placeholder':
                                                    "TOTAL Amount Administered"}),
            'vet_administered': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                           'id': 'vet-administered',
                                                           'name': 'vet_administered'}),
            'vet_name': forms.TextInput(attrs={'class': '',
                                               'id': 'vet-name',
                                               'name': 'vet_name',
                                               'placeholder':
                                               "VET Name",
                                               'value': ''}),
            'notes': forms.Textarea(attrs={'class': 'hide-placeholder',
                                           'id': 'notes',
                                           'name': 'notes',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-coop-cleaning',
                                                      'name': 'images_coop_cleaning'})
        }


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

    def __init__(self, *args, **kwargs):
        super(MedicinesForm, self).__init__(*args, **kwargs)
        # self.fields['disease_protected_against'].empty_label = 'Select Disease Protected Against'
        # self.fields['disease_protected_against'].initial = "Select Disease Protected Against"
        # self.fields['disease_protected_against'].show_hidden_initial = True
        self.fields['administration_method'].empty_label = 'Select Administration Method'
        self.fields['administration_method'].initial = "Select Administration Method"
        self.fields['administration_method'].show_hidden_initial = True

    class Meta:
        """ Meta Class Docstring here as required """
        model = Medicines
        fields = ('date', 'flock',
                  'medicine_name',
                  'disease_protected_against',
                  'qty_hens', 'qty_chicks',
                  'qty_cocks', 'doseage_amount',
                  'administration_method',
                  'vet_administered', 'vet_name',
                  'notes', 'images')

        widgets = {
            'date': forms.DateTimeInput,
            'flock': forms.CheckboxInput,
            'medicine_name': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                    'id': 'medicine-name',
                                                    'name': 'medicine_name',
                                                    'value': '',
                                                    'onclick': "displaySelectLabel('select-medicine-label')",
                                                    'onkeyup': "showSuggestionsMedicines(this.value, 'select-medicine-label')",
                                                    'placeholder':
                                                    "Medicine Name"}),
            'disease_protected_against': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                                'id': 'disease-protected-against',
                                                                'name': 'disease_protected_against',
                                                                'value': '',
                                                                'onclick': "displaySelectLabel('select-dpa-label')",
                                                                'onkeyup': "showSuggestionsDiseases(this.value, 'select-dpa-label')",
                                                                'placeholder':
                                                                "Disease Protected Against"}),
            'doseage_amount': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                     'id': 'doseage-amount',
                                                     'name': 'doseage_amount',
                                                     'type': 'number',
                                                     'placeholder':
                                                     "TOTAL Amount Administered"}),
            'administration_method': forms.Select(attrs={'class': '',
                                                         'id': 'administration-method',
                                                         'name': 'administration_method',
                                                         'onclick': "displaySelectLabel('select-administration-label')",
                                                         'placeholder':
                                                         "Administration Method PH"}),
            'vet_administered': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                           'id': 'vet-administered',
                                                           'name': 'vet_administered'}),
            'vet_name': forms.TextInput(attrs={'class': '',
                                               'id': 'vet-name',
                                               'name': 'vet_name',
                                               'placeholder':
                                               "VET Name",
                                               'value': ''}),
            'notes': forms.Textarea(attrs={'class': 'hide-placeholder',
                                           'id': 'notes',
                                           'name': 'notes',
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

    def __init__(self, *args, **kwargs):
        super(VaccinesForm, self).__init__(*args, **kwargs)
        # This removes the default ------ that displays instead of a label because the input is a dropdown
        self.fields['administration_method'].empty_label = 'Select Administration Method'
        self.fields['administration_method'].initial = "Select Administration Method"
        self.fields['administration_method'].show_hidden_initial = True

    class Meta:
        """ Meta Class Docstring here as required """
        model = Vaccines
        fields = ('date', 'flock',
                  'vaccine_name',
                  'virus_protected_against',
                  'qty_hens', 'qty_chicks',
                  'qty_cocks', 'doseage_amount',
                  'administration_method',
                  'vet_administered', 'vet_name',
                  'notes', 'images')

        widgets = {
            'date': forms.DateTimeInput,
            'flock': forms.CheckboxInput,
            'vaccine_name': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                   'id': 'vaccine-name',
                                                   'name': 'vaccine_name',
                                                   'value': '',
                                                   'onclick': "displaySelectLabel('select-vaccine-label')",
                                                   'onkeyup': "showSuggestionsVaccines(this.value, 'select-vaccine-label')",
                                                   'placeholder':
                                                   "Vaccine Name"}),
            'virus_protected_against': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                              'id': 'virus-protected-against',
                                                              'name': 'virus_protected_against',
                                                              'value': '',
                                                              'onclick': "displaySelectLabel('select-vpa-label')",
                                                              'onkeyup': "showSuggestionsViruses(this.value, 'select-vpa-label')",
                                                              'placeholder':
                                                              "Virus Protected Against"}),
            'doseage_amount': forms.TextInput(attrs={'class': 'hide-placeholder',
                                                     'id': 'doseage-amount',
                                                     'name': 'doseage_amount',
                                                     'type': 'number',
                                                     'placeholder':
                                                     "TOTAL Amount Administered"}),
            'administration_method': forms.Select(attrs={'class': '',
                                                         'id': 'administration-method',
                                                         'name': 'administration_method',
                                                         'onclick': "displaySelectLabel('select-administration-label')",
                                                         'placeholder':
                                                         "Administration Method PH"}),
            'vet_administered': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                           'id': 'vet-administered',
                                                           'name': 'vet_administered'}),
            'vet_name': forms.TextInput(attrs={'class': '',
                                               'id': 'vet-name',
                                               'name': 'vet_name',
                                               'placeholder':
                                               "VET Name",
                                               'value': ''}),
            'notes': forms.Textarea(attrs={'class': 'hide-placeholder',
                                           'id': 'notes',
                                           'name': 'notes',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-coop-cleaning',
                                                      'name': 'images_coop_cleaning'})
        }


# Create a Vaccines Name form
class VaccinesNameForm(forms.ModelForm):
    """ Create a Vaccines Name form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = VaccinesName
        fields = "__all__"
