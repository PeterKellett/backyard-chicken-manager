from django import forms
from django.forms import ModelForm
from .models import EggRoadsideSales, EggCollectionSales, EggDeliverySalesDashboard, EggDeliverySales, EggMarketSales

# Create an Egg Roadside Sales form
class EggRoadsideSalesForm(ModelForm):
    """ Create a Roadside Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggRoadsideSales
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
                  'qty_trays_of_eggs_added',
                  'amount_paid_eggs_roadside',
                  'sales_amount_eggs_roadside',
                  'sales_paid_difference_eggs_roadside',
                  'loses_eggs_roadside')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'single_egg_price': forms.TextInput(attrs={'class': '',
                                                       'id': 'single-egg-price',
                                                       'name': 'single_egg_price',
                                                       'placeholder':
                                                       "Single Eggs Price",
                                                       'value': ''}),
            'half_dozen_eggs_price': forms.TextInput(attrs={'class': '',
                                                            'id': 'half-dozen-eggs-price',
                                                            'name': 'half_dozen_eggs_price',
                                                            'placeholder':
                                                            "Half Dozen Eggs Price",
                                                            'value': ''}),
            'ten_eggs_price': forms.TextInput(attrs={'class': '',
                                                     'id': 'ten-eggs-price',
                                                     'name': 'ten_eggs_price',
                                                     'placeholder':
                                                     "10 Eggs Price",
                                                     'value': ''}),
            'dozen_eggs_price': forms.TextInput(attrs={'class': '',
                                                       'id': 'dozen-eggs-price',
                                                       'name': 'dozen_eggs_price',
                                                       'placeholder':
                                                       "Dozen Eggs Price",
                                                       'value': ''}),
            'trays_of_eggs_price': forms.TextInput(attrs={'class': '',
                                                          'id': 'trays-of-eggs-price',
                                                          'name': 'trays_of_eggs_price',
                                                          'placeholder':
                                                          "Tray of Eggs Price",
                                                          'value': ''}),

            'qty_single_eggs_remaining': forms.TextInput(attrs={'class': '',
                                                          'id': 'qty-single-eggs-remaining',
                                                          'name': 'qty_single_eggs_remaining',
                                                          'placeholder':
                                                          "Qty of Single Eggs Remaining",
                                                          'value': ''}),
            'qty_single_eggs_added': forms.TextInput(attrs={'class': '',
                                                          'id': 'qty-single-eggs-added',
                                                          'name': 'qty_single_eggs_added',
                                                          'placeholder':
                                                          "Qty of Single Eggs Added",
                                                          'value': ''}),
            'qty_half_dozen_egg_boxes_remaining': forms.TextInput(attrs={'class': '',
                                                                         'id': 'qty-half-dozen-egg-boxes-remaining',
                                                                         'name': 'qty_half_dozen_egg_boxes_remaining',
                                                                         'placeholder':
                                                                         "Qty of Half Dozens Remaining",
                                                                         'value': ''}),
            'qty_half_dozen_egg_boxes_added': forms.TextInput(attrs={'class': '',
                                                                     'id': 'qty-half-dozen-egg-boxes-added',
                                                                     'name': 'qty_half_dozen_egg_boxes_added',
                                                                     'placeholder':
                                                                     "Qty of Half Dozens Added",
                                                                     'value': ''}),
            'qty_ten_egg_boxes_remaining': forms.TextInput(attrs={'class': '',
                                                                  'id': 'qty-ten-egg-boxes-remaining',
                                                                  'name': 'qty_ten_egg_boxes_remaining',
                                                                  'placeholder':
                                                                  "Qty of 10's Remaining",
                                                                  'value': ''}),
            'qty_ten_egg_boxes_added': forms.TextInput(attrs={'class': '',
                                                              'id': 'qty-ten-egg-boxes-added',
                                                              'name': 'qty_ten_egg_boxes_added',
                                                              'placeholder':
                                                              "Qty of 10's Added",
                                                              'value': ''}),
            'qty_dozen_egg_boxes_remaining': forms.TextInput(attrs={'class': '',
                                                                    'id': 'qty-dozen-egg-boxes-remaining',
                                                                    'name': 'qty_dozen_egg_boxes_remaining',
                                                                    'placeholder':
                                                                    "Qty of Dozens Remaining",
                                                                    'value': ''}),
            'qty_dozen_egg_boxes_added': forms.TextInput(attrs={'class': '',
                                                                'id': 'qty-dozen-egg-boxes-added',
                                                                'name': 'qty_dozen_egg_boxes_added',
                                                                'placeholder':
                                                                "Qty of Dozens Added",
                                                                'value': ''}),
            'qty_trays_of_eggs_remaining': forms.TextInput(attrs={'class': '',
                                                                  'id': 'qty-trays-of-eggs-remaining',
                                                                  'name': 'qty_trays_of_eggs_remaining',
                                                                  'placeholder':
                                                                  "Qty of Trays Remaining",
                                                                  'value': ''}),
            'qty_trays_of_eggs_added': forms.TextInput(attrs={'class': '',
                                                              'id': 'qty-trays-of-eggs-added',
                                                              'name': 'qty_trays_of_eggs_added',
                                                              'placeholder':
                                                              "Qty of Trays Added",
                                                              'value': ''}),
            'amount_paid_eggs_roadside': forms.TextInput(attrs={'class': '',
                                                                'id': 'amount-paid-eggs-roadside',
                                                                'name': 'amount_paid_eggs_roadside',
                                                                'placeholder':
                                                                "€ Amount Collected",
                                                                'value': ''}),
            'sales_amount_eggs_roadside': forms.TextInput(attrs={'class':
                                                                 'text-end h-style-input',
                                                                 'id': 'sales-amount-eggs-roadside',
                                                                 'name': 'sales_amount_eggs_roadside',
                                                                 'placeholder':
                                                                 "Value of Eggs Sold",
                                                                 'value': '# Temp',
                                                                 'disabled': 'true'}),
            'sales_paid_difference_eggs_roadside': forms.TextInput(attrs={'class':
                                                                          'text-end h-style-input',
                                                                          'id': 'sales-paid-difference-eggs-roadside',
                                                                          'name': 'sales_paid_difference_eggs_roadside',
                                                                          'placeholder':
                                                                          "Sales vs Received Difference",
                                                                          'value': '# Temp',
                                                                          'disabled': 'true'}),

            'loses_eggs_roadside': forms.TextInput(attrs={'class': 'class-name',
                                                               'id': 'loses-eggs-roadside',
                                                               'name': 'loses_eggs_roadside',
                                                               'placeholder':
                                                               "Qty of Eggs Broken, Stolen or Lost",
                                                               'value': ''}),
        }

# Create an Egg Collection Sales form
class EggCollectionSalesForm(ModelForm):
    """ Create an Egg Collection Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollectionSales
        fields = ('date',
                  'customer_name_eggs_collection',
                  'normal_order_qty_eggs_collection',
                  'qty_sold_eggs_collection',
                  'qty_given_free_eggs_collection',
                  'amount_paid_eggs_collection',
                  'balance_owed_eggs_collection',
                  'breakages_and_loses_eggs_collection')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'customer_name_eggs_collection': forms.TextInput(attrs={'class':
                                                                    'h-style-input',
                                                                    'id': 'customer-name-eggs-collection',
                                                                    'name': 'customer_name_eggs_collection',
                                                                    'placeholder':
                                                                    "Customer Name",
                                                                    'value': 'Customer Name Temp',
                                                                    'disabled': 'true'}),
            'normal_order_qty_eggs_collection': forms.TextInput(attrs={'class':
                                                                       'text-end h-style-input',
                                                                       'id': 'normal-order-qty-eggs-collection',
                                                                       'name': 'normal_order_qty_eggs_collection',
                                                                       'placeholder':
                                                                       "Normal Order Qty",
                                                                       'value': '# Temp',
                                                                       'disabled': 'true'}),
            'qty_sold_eggs_collection': forms.TextInput(attrs={'class': 'class-name',
                                                               'id': 'qty-sold-eggs-collection',
                                                               'name': 'qty_sold_eggs_collection',
                                                               'placeholder':
                                                               "Qty of Eggs Sold",
                                                               'value': ''}),
            'qty_given_free_eggs_collection': forms.TextInput(attrs={'class': 'class-name',
                                                                     'id': 'qty-given-free-eggs-collection',
                                                                     'name': 'qty_given_free_eggs_collection',
                                                                     'placeholder':
                                                                     "Qty of Eggs Given Free",
                                                                     'value': ''}),
            'amount_paid_eggs_collection': forms.TextInput(attrs={'class': 'class-name',
                                                                  'id': 'amount-paid-eggs-collection',
                                                                  'name': 'amount_paid_eggs_collection',
                                                                  'placeholder':
                                                                  "Dozen Eggs Price",
                                                                  'value': ''}),
            'balance_owed_eggs_collection': forms.TextInput(attrs={'class':
                                                                   'text-end h-style-input',
                                                                   'id': 'balance-owed-eggs-collection',
                                                                   'name': 'balance_owed_eggs_collection',
                                                                   'placeholder':
                                                                   "Balance Owed",
                                                                   'value': '# Temp',
                                                                   'disabled': 'true'}),
            'breakages_and_loses_eggs_collection': forms.TextInput(attrs={'class': 'class-name',
                                                            	          'id': 'breakages-and-loses-eggs-collection',
                                                            	          'name': 'breakages_and_loses_eggs_collection',
                                                            	          'placeholder':
                                                            	          "Qty of Eggs Broken, Stolen or Lost",
                                                            	          'value': ''})
        }

# Create an Egg Delivery Sales form
class EggDeliverySalesForm(ModelForm):
    """ Create an Egg Delivery Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggDeliverySales
        fields = ('date',
                  'customer_name_eggs_delivery',
                  'normal_order_qty_eggs_delivery',
                  'delivery_due_date',
                  'delivery_not_made',
                  'delivery_not_made_reason',
                  'qty_sold_eggs_delivery',
                  'qty_given_free_eggs_delivery',
                  'amount_paid_eggs_delivery',
                  'balance_owed_eggs_delivery')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'customer_name_eggs_delivery': forms.TextInput(attrs={'class':
                                                                  'h-style-input',
                                                                  'id': 'customer-name-eggs-delivery',
                                                                  'name': 'customer_name_eggs_delivery',
                                                                  'placeholder':
                                                                  "Customer Name",
                                                                  'value': 'Customer Name Temp',
                                                                  'disabled': 'true'}),
            'normal_order_qty_eggs_delivery': forms.TextInput(attrs={'class':
                                                                     'text-end h-style-input',
                                                                     'id': 'normal-order-qty-eggs-delivery',
                                                                     'name': 'normal_order_qty_eggs_delivery',
                                                                     'placeholder':
                                                                     "Normal Order Qty",
                                                                     'value': '# Temp',
                                                                     'disabled': 'true'}),
            'delivery_due_date': forms.DateInput(attrs={'class':
                                                        'text-end h-style-input',
                                                        'id': 'delivery-due-date',
                                                        'name': 'delivery_due_date',
                                                        'placeholder':
                                                        "Delivery Due Date",
                                                        'value': 'dd/mm/yy Temp',
                                                        'disabled': 'true'}),
            'delivery_not_made': forms.CheckboxInput(attrs={'class': 'click-to-show',
                                                            'id': 'delivery-not-made',
                                                            'name': 'delivery_not_made',
                                                            'placeholder':
                                                            "Delivery Not Made",
                                                            'value': ''}),
            'delivery_not_made_reason': forms.TextInput(attrs={'class': '',
                                                               'id': 'delivery-not-made-reason',
                                                               'name': 'delivery_not_made_reason',
                                                               'placeholder':
                                                               "Delivery Not Made Reason",
                                                               'value': ''}),
            'qty_sold_eggs_delivery': forms.TextInput(attrs={'class': 'class-name',
                                                             'id': 'qty-sold-eggs-delivery',
                                                             'name': 'qty_sold_eggs_delivery',
                                                             'placeholder':
                                                             "Qty of Eggs Sold",
                                                             'value': ''}),
            'qty_given_free_eggs_delivery': forms.TextInput(attrs={'class': 'class-name',
                                                                   'id': 'qty-given-free-eggs-delivery',
                                                                   'name': 'qty_given_free_eggs_delivery',
                                                                   'placeholder':
                                                                   "Qty of Eggs Given Free",
                                                                   'value': ''}),
            'amount_paid_eggs_delivery': forms.TextInput(attrs={'class': 'class-name',
                                                                'id': 'amount-paid-eggs-delivery',
                                                                'name': 'amount_paid_eggs_delivery',
                                                                'placeholder':
                                                                "Amount Paid",
                                                                'value': ''}),
            'balance_owed_eggs_delivery': forms.TextInput(attrs={'class':
                                                                 'text-end h-style-input',
                                                                 'id': 'balance-owed-eggs-delivery',
                                                                 'name': 'balance_owed_eggs_delivery',
                                                                 'placeholder':
                                                                 "Balance Owed",
                                                                 'value': '# Temp',
                                                                 'disabled': 'true'})
        }

# Create an Egg Delivery Sales Dashboard form
class EggDeliverySalesDashboardForm(ModelForm):
    """ Create an Egg Delivery Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggDeliverySalesDashboard
        fields = ('date',
                  'breakages_and_loses_eggs_delivery')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'breakages_and_loses_eggs_delivery': forms.TextInput(attrs={'class': 'class-name',
                                                            	        'id': 'breakages-and-loses-eggs-delivery',
                                                            	        'name': 'breakages_and_loses_eggs_delivery',
                                                            	        'placeholder':
                                                            	        "Qty of Eggs Broken, Stolen or Lost",
                                                            	        'value': ''})
        }

# Create an Egg Market Sales form
class EggMarketSalesForm(ModelForm):
    """ Create an Egg Market Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggMarketSales
        fields = ('date',
                  'venue_location_eggs_market',
                  'single_egg_price',
                  'half_dozen_eggs_price',
                  'ten_eggs_price',
                  'dozen_eggs_price',
                  'trays_of_eggs_price',
                  'qty_single_eggs_sold',
                  'qty_half_dozen_egg_boxes_sold',
                  'qty_ten_egg_boxes_sold',
                  'qty_dozen_egg_boxes_sold',
                  'qty_trays_of_eggs_sold',
                  'amount_paid_eggs_market',
                  'sales_amount_eggs_roadside',
                  'sales_paid_difference_eggs_roadside',
                  'loses_eggs_market')

        widgets = {
            'date': forms.DateInput(attrs={'class': 'class-name'}),
            'venue_location_eggs_market': forms.TextInput(attrs={'class': 'class-name',
                                                                 'id': 'venue-location-eggs-market',
                                                                 'name': 'venue_location_eggs_market',
                                                                 'placeholder':
                                                                 "Market Venue/Location",
                                                                 'value': ''}),
            'single_egg_price': forms.TextInput(attrs={'class': 'class-name',
                                                       'id': 'single-egg-price',
                                                       'name': 'single_egg_price',
                                                       'placeholder':
                                                       "Single Eggs Price",
                                                       'value': ''}),
            'half_dozen_eggs_price': forms.TextInput(attrs={'class': 'class-name',
                                                            'id': 'half-dozen-eggs-price',
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

            'qty_single_eggs_sold': forms.TextInput(attrs={'class': 'class-name',
                                                          'id': 'qty-single-eggs-sold',
                                                          'name': 'qty_single_eggs_sold',
                                                          'placeholder':
                                                          "Qty of Single Eggs Sold",
                                                          'value': ''}),
            'qty_half_dozen_egg_boxes_sold': forms.TextInput(attrs={'class': 'class-name',
                                                                         'id': 'qty-half-dozen-egg-boxes-sold',
                                                                         'name': 'qty_half_dozen_egg_boxes_sold',
                                                                         'placeholder':
                                                                         "Qty of Half Dozens Sold",
                                                                         'value': ''}),
            'qty_ten_egg_boxes_sold': forms.TextInput(attrs={'class': 'class-name',
                                                                  'id': 'qty-ten-egg-boxes-sold',
                                                                  'name': 'qty_ten_egg_boxes_sold',
                                                                  'placeholder':
                                                                  "Qty of 10's Sold",
                                                                  'value': ''}),
            'qty_dozen_egg_boxes_sold': forms.TextInput(attrs={'class': 'class-name',
                                                                    'id': 'qty-dozen-egg-boxes-sold',
                                                                    'name': 'qty_dozen_egg_boxes_sold',
                                                                    'placeholder':
                                                                    "Qty of Dozens Sold",
                                                                    'value': ''}),
            'qty_trays_of_eggs_sold': forms.TextInput(attrs={'class': 'class-name',
                                                                  'id': 'qty-trays-of-eggs-sold',
                                                                  'name': 'qty_trays_of_eggs_sold',
                                                                  'placeholder':
                                                                  "Qty of Trays Sold",
                                                                  'value': ''}),
            'amount_paid_eggs_market': forms.TextInput(attrs={'class': 'class-name',
                                                                'id': 'amount-paid-eggs-market',
                                                                'name': 'amount_paid_eggs_market',
                                                                'placeholder':
                                                                "€ Amount Collected",
                                                                'value': ''}),
            'sales_amount_eggs_roadside': forms.TextInput(attrs={'class':
                                                                 'text-end h-style-input',
                                                                 'id': 'sales-amount-eggs-roadside',
                                                                 'name': 'sales_amount_eggs_roadside',
                                                                 'placeholder':
                                                                 "Value of Eggs Sold",
                                                                 'value': '# Temp',
                                                                 'disabled': 'true'}),
            'sales_paid_difference_eggs_roadside': forms.TextInput(attrs={'class':
                                                                          'text-end h-style-input',
                                                                          'id': 'sales-paid-difference-eggs-roadside',
                                                                          'name': 'sales_paid_difference_eggs_roadside',
                                                                          'placeholder':
                                                                          "Sales vs Received Difference",
                                                                          'value': '# Temp',
                                                                          'disabled': 'true'}),

            'loses_eggs_market': forms.TextInput(attrs={'class': 'class-name',
                                                               'id': 'loses-eggs-market',
                                                               'name': 'loses_eggs_market',
                                                               'placeholder':
                                                               "Qty of Eggs Broken, Stolen or Lost",
                                                               'value': ''}),
        }