from django import forms
from .models import EggRoadsideSales, EggCollectionSales, EggDeliverySalesDashboard, EggDeliverySales, EggMarketSales, Customer


# Create an Egg Roadside Sales form
class EggRoadsideSalesForm(forms.ModelForm):
    """ Create a Roadside Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggRoadsideSales
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
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
            # Below temporarily removed as involves a more complex wiring
            # 'sales_amount_eggs_roadside': forms.TextInput(attrs={'class':
            #                                                      'text-end h-style-input',
            #                                                      'id': 'sales-amount-eggs-roadside',
            #                                                      'name': 'sales_amount_eggs_roadside',
            #                                                      'placeholder':
            #                                                      "Value of Eggs Sold",
            #                                                      'value': '# Temp',
            #                                                      'disabled': 'true'}),
            # 'sales_paid_difference_eggs_roadside': forms.TextInput(attrs={'class':
            #                                                             'text-end h-style-input',
            #                                                             'id': 'sales-paid-difference-eggs-roadside',
            #                                                             'name': 'sales_paid_difference_eggs_roadside',
            #                                                             'placeholder':
            #                                                             "Sales vs Received Difference",
            #                                                             'value': '# Temp',
            #                                                             'disabled': 'true'}),

            'loses_eggs_roadside': forms.TextInput(attrs={'class': '',
                                                          'id': 'loses-eggs-roadside',
                                                          'name': 'loses_eggs_roadside',
                                                          'placeholder':
                                                          "Qty of Eggs Broken, Stolen or Lost",
                                                          'value': ''}),

            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-eggs-roadside',
                                           'name': 'notes_eggs_roadside',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'imagess-eggs-roadside',
                                                      'name': 'imagess_eggs_roadside'})
        }

# Create an Egg Collection Sales form
class EggCollectionSalesForm(forms.ModelForm):
    """ Create an Egg Collection Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollectionSales
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'class-name'}),
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
            'sale_amount_eggs_collection': forms.TextInput(attrs={'class': 
                                                                  'text-end h-style-input',
                                                                  'id': 'sale-amount-eggs-collection',
                                                                  'name': 'sale_amount_eggs_collection',
                                                                  'placeholder':
                                                                  "Qty of Eggs Given Free",
                                                                  'value': '# Temp'}),
            'amount_paid_eggs_collection': forms.TextInput(attrs={'class': 'class-name',
                                                                  'id': 'amount-paid-eggs-collection',
                                                                  'name': 'amount_paid_eggs_collection',
                                                                  'placeholder':
                                                                  "Amount Paid",
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
                                                            	          'value': ''}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-eggs-collection',
                                           'name': 'collection',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-eggs-collection',
                                                      'name': 'images_eggs_collection'})                                                                 
        }


# Create an Egg Collection Sales Dashboard form
# class EggCollectionSalesDashboardForm(forms.ModelForm):
#     """ Create an Egg Collection Sales Dashboard form """
#     class Meta:
#         """ Meta Class Docstring here as required """
#         model = EggCollectionSalesDashboard
#         fields = '__all__'

#         widgets = {
#             'date': forms.DateTimeInput(attrs={'class': ''}),
#             'breakages_and_loses_eggs_delivery' : forms.TextInput(attrs={'class': '',
#                                                                          'id': 'customer-name-eggs-delivery',
#                                                                          'name': 'customer_name_eggs_delivery',
#                                                                          'placeholder':
#                                                                          "Customer Name",
#                                                                          'value': 'Customer Name Temp',
#                                                                          'disabled': 'true'
#                                                                          }),
#             'notes': forms.Textarea(attrs={'class': '',
#                                            'id': 'notes-eggs-delivery',
#                                            'name': 'notes_eggs_delivery',
#                                            'placeholder':
#                                            "Notes",
#                                            'value': ''}),
#             'images': forms.ClearableFileInput(attrs={'class': 'upload',
#                                                       'id': 'images-eggs-delivery',
#                                                       'name': 'images_eggs_delivery'})                                                                
#         }


# Create an Egg Delivery Sales form
class EggDeliverySalesForm(forms.ModelForm):
    """ Create an Egg Delivery Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggDeliverySales
        fields = '__all__'
        
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': ''}),
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
            'delivery_due_date': forms.DateTimeInput(attrs={'class':
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
            'qty_sold_eggs_delivery': forms.TextInput(attrs={'class': '',
                                                                'id': 'qty-sold-eggs-delivery',
                                                                'name': 'qty_sold_eggs_delivery',
                                                                'placeholder':
                                                                "Qty of Eggs Sold",
                                                                'value': ''}),
            'qty_given_free_eggs_delivery': forms.TextInput(attrs={'class': '',
                                                                      'id': 'qty-given-free-eggs-delivery',
                                                                      'name': 'qty_given_free_eggs_delivery',
                                                                      'placeholder':
                                                                      "Qty of Eggs Given Free",
                                                                      'value': ''}),
            'sale_amount_eggs_delivery': forms.TextInput(attrs={'class': 
                                                                 'text-end h-style-input',
                                                                 'id': 'sale-amount-eggs-collection',
                                                                 'name': 'sale_amount_eggs_collection',
                                                                 'placeholder':
                                                                 "Qty of Eggs Given Free",
                                                                 'value': '# Temp'}),
            'amount_paid_eggs_delivery': forms.TextInput(attrs={'class': '',
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
                                                                    'disabled': 'true'}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-eggs-delivery',
                                           'name': 'notes_eggs_delivery',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-eggs-delivery',
                                                      'name': 'images_eggs_delivery'})                                                        
        }


# Create an Egg Delivery Sales Dashboard form
class EggDeliverySalesDashboardForm(forms.ModelForm):
    """ Create an Egg Delivery Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggDeliverySalesDashboard
        fields = '__all__'
        
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': ''}),
            'breakages_and_loses_eggs_delivery': forms.TextInput(attrs={'class': '',
                                                            	        'id': 'breakages-and-loses-eggs-delivery',
                                                            	        'name': 'breakages_and_loses_eggs_delivery',
                                                            	        'placeholder':
                                                            	        "Qty of Eggs Broken, Stolen or Lost",
                                                            	        'value': ''}),
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-eggs-delivery-dash',
                                           'name': 'notes_eggs_delivery_dash',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-eggs-delivery-dash',
                                                      'name': 'images_eggs_delivery_dash'})                                                               
        }
  

# Create an Egg Market Sales form
class EggMarketSalesForm(forms.ModelForm):
    """ Create an Egg Market Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggMarketSales
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': ''}),
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
            'sales_amount_eggs_market': forms.TextInput(attrs={'class':
                                                               'text-end h-style-input',
                                                               'id': 'sales-amount-eggs-market',
                                                               'name': 'sales_amount_eggs_market',
                                                               'placeholder':
                                                               "Value of Eggs Sold",
                                                               'value': '# Temp',
                                                               'disabled': 'true'}),
            'sales_paid_difference_eggs_market': forms.TextInput(attrs={'class':
                                                                        'text-end h-style-input',
                                                                        'id': 'sales-paid-difference-eggs-market',
                                                                        'name': 'sales_paid_difference_eggs_market',
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
            'notes': forms.Textarea(attrs={'class': '',
                                           'id': 'notes-eggs-market',
                                           'name': 'notes_eggs_market',
                                           'placeholder':
                                           "Notes",
                                           'value': ''}),
            'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                      'id': 'images-eggs-market',
                                                      'name': 'images_eggs_market'})                                               
        }


# Create a Customer form
class CustomerForm(forms.ModelForm):
    """ Create a Customer form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = Customer
        fields = '__all__'

        widgets = {
                # farm_profile = models.ForeignKey(FarmProfile,
                #                                 blank=False,
                #                                 null=False,
                #                                 on_delete=models.CASCADE,
                #                                 related_name='farmprofile')
                # customer_type = models.ForeignKey(CustomerType,
                #                                   blank=False,
                #                                   null=False,
                #                                   on_delete=models.CASCADE,
                #                                   related_name='customertype'
                #                                   )
                'customer_name': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'customer-name',
                                                           'name': 'customer_name',
                                                           'placeholder':
                                                           "Customer Name",
                                                           'value': ''}),
                'address': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'address',
                                                           'name': 'address',
                                                           'placeholder':
                                                           "Address",
                                                           'value': ''}),
                'postcode': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'postcode',
                                                           'name': 'postcode',
                                                           'placeholder':
                                                           "Postcode",
                                                           'value': ''}),
                'phone': forms.TextInput(attrs={'class': 'class-name',
                                                'id': 'phone',
                                                'name': 'phone',
                                                'placeholder':
                                                "Phone",
                                                'value': ''}),
                'date_added': forms.DateInput(attrs={'class': 'class-name',
                                                     'id': 'date-added',
                                                     'name': 'date_added',
                                                     'placeholder':
                                                     "Date Customer was Added",
                                                     'value': ''}),
                # status = models.ForeignKey(attrs={'class': 'class-name',
                                                    # 'id': 'customer-status',
                                                    # 'name': 'customer_status',
                                                    # 'placeholder':
                                                    # "Customer Status"}),
                'order_qty': forms.TextInput(attrs={'class': 'class-name',
                                                    'id': 'order-qty',
                                                    'name': 'order_qty',
                                                    'placeholder':
                                                    "Normal Order Qty",
                                                    'value': ''}),
                'route_day': forms.DateInput(attrs={'class': 'class-name',
                                                    'id': 'route-day',
                                                    'name': 'route_day',
                                                    'placeholder':
                                                    "Route Day",
                                                    'value': ''}),
                'route_position': forms.TextInput(attrs={'class': 'class-name',
                                                         'id': 'route-position',
                                                         'name': 'route_position',
                                                         'placeholder':
                                                         "Route Position",
                                                         'value': ''}),
                'single_egg_price': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'single-egg-price',
                                                           'name': 'single_egg_price',
                                                           'placeholder':
                                                           "Single Egg Price",
                                                           'value': ''}),
                'six_egg_price': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'six-egg-price',
                                                           'name': 'six_egg_price',
                                                           'placeholder':
                                                           "Half Dozen Eggs Price",
                                                           'value': ''}),
                'ten_egg_price': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'ten-egg-price',
                                                           'name': 'ten_egg_price',
                                                           'placeholder':
                                                           "Ten Eggs Price",
                                                           'value': ''}),
                'twelve_egg_price': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'twelve-egg-price',
                                                           'name': 'twelve_egg_price',
                                                           'placeholder':
                                                           "Dozen Eggs Price",
                                                           'value': ''}),
                'tray_price': forms.TextInput(attrs={'class': 'class-name',
                                                           'id': 'tray-price',
                                                           'name': 'tray_price',
                                                           'placeholder':
                                                           "Tray Price",
                                                           'value': ''}),
                'notes': forms.Textarea(attrs={'class': '',
                                               'id': 'notes-customer',
                                               'name': 'notes_customer',
                                               'placeholder':
                                               "Notes",
                                               'value': ''}),
                'images': forms.ClearableFileInput(attrs={'class': 'upload',
                                                          'id': 'images-customer',
                                                          'name': 'images_customer'})
        }