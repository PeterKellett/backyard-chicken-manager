from django import forms
from .models import EggRoadsideSales, EggCollectionSales, EggDeliverySalesDashboard, EggDeliverySales, EggMarketSales


# Create an Egg Roadside Sales form
class EggRoadsideSalesForm(forms.ModelForm):
    """ Create a Roadside Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggRoadsideSales
        fields = '__all__'


# Create an Egg Collection Sales form
class EggCollectionSalesForm(forms.ModelForm):
    """ Create an Egg Collection Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggCollectionSales
        fields = '__all__'


# Create an Egg Delivery Sales form
class EggDeliverySalesForm(forms.ModelForm):
    """ Create an Egg Delivery Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggDeliverySales
        fields = '__all__'


# Create an Egg Delivery Sales Dashboard form
class EggDeliverySalesDashboardForm(forms.ModelForm):
    """ Create an Egg Delivery Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggDeliverySalesDashboard
        fields = '__all__'


# Create an Egg Market Sales form
class EggMarketSalesForm(forms.ModelForm):
    """ Create an Egg Market Sales form """
    class Meta:
        """ Meta Class Docstring here as required """
        model = EggMarketSales
        fields = '__all__'
