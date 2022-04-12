from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import PurchasesCategory, Purchases


# Create a Medicines Name form
class PurchasesCategoryForm(forms.ModelForm):
    """ Create a Purchases Category form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = PurchasesCategory
        fields = "__all__"


# Create a Medicine form
class PurchasesForm(forms.ModelForm):
    """ Create a Purchases form """

    def __init__(self, *args, **kwargs):
        super(PurchasesForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Category'
        self.fields['category'].initial = "Category"
        self.fields['category'].show_hidden_initial = True
        self.fields['payment_method'].empty_label = 'Payment Method'
        self.fields['payment_method'].initial = "Payment Method"
        self.fields['payment_method'].show_hidden_initial = True

    class Meta:
        """ Meta Class Docstring here as required """
        model = Purchases
        fields = ('date', 'flock',
                  'category', 'product',
                  'total_cost', 'amount_purchased',
                  'unit_of_measurement',
                  'payment_method', 'receipt_reference',
                  'seller_name',
                  'notes', 'images')

        widgets = {
            'date': forms.DateTimeInput,
            'flock': forms.CheckboxInput,
            'category': forms.Select(attrs={'class': '',
                                            'id': 'category',
                                            'name': 'category',
                                            'value': '',
                                            'onclick': "displaySelectLabel('purchases-category-label')",
                                            'onkeyup': "showSuggestionsCategories(this.value, 'category')",
                                            'placeholder':
                                            "Category"}),
            'product': forms.TextInput(attrs={'class': '',
                                              'id': 'product',
                                              'name': 'product',
                                              'value': '',
                                              'onkeyup': "showSuggestionsProducts(this.value, 'product')",
                                              'placeholder':
                                              "Product Name"}),
            'total_cost': forms.TextInput(attrs={'class': '',
                                                 'id': 'total-cost',
                                                 'name': 'total_cost',
                                                 'value': '',
                                                 'placeholder':
                                                 "Total Cost"}),
            'amount_purchased': forms.TextInput(attrs={'class': '',
                                                       'id': 'amount-purchased',
                                                       'name': 'amount_purchased',
                                                       'value': '',
                                                       'placeholder':
                                                       "Amount Purchased"}),
            'unit_of_measurement': forms.TextInput(attrs={'class': '',
                                                          'id': 'unit-of-measurement',
                                                          'name': 'unit_of_measurement',
                                                          'value': '',
                                                          'placeholder':
                                                          "Unit of Measurement"}),
            'payment_method': forms.Select(attrs={'class': '',
                                                  'id': 'payment-method',
                                                  'name': 'payment_method',
                                                  'onchange': "displaySelectLabel('select-administration-label')",
                                                  'placeholder':
                                                  "Payment Method"}),
            'receipt_reference': forms.TextInput(attrs={'class': '',
                                                        'id': 'receipt-reference',
                                                        'name': 'receipt_reference',
                                                        'value': '',
                                                        'onclick': "displaySelectLabel('select-receipt-reference-label')",
                                                        'onkeyup': "showSuggestionsDiseases(this.value, 'product')",
                                                        'placeholder':
                                                        "Receipt/Invoice Reference"}),
            'seller_name': forms.TextInput(attrs={'class': '',
                                                  'id': 'seller-name',
                                                  'name': 'seller_name',
                                                  'value': '',
                                                  'onclick': "displaySelectLabel('select-seller-name-label')",
                                                  'onkeyup': "showSuggestionsDiseases(this.value, 'product')",
                                                  'placeholder':
                                                  "Seller Name"}),
            'notes': forms.Textarea(attrs={'class': 'hide-placeholder',
                                           'id': 'notes-coop-cleaning',
                                           'name': 'notes_coop_cleaning',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-coop-cleaning',
                                                      'name': 'images_coop_cleaning'})
        }

