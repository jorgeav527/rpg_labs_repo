from django import forms
from django.forms import inlineformset_factory

from dynamic_forms import DynamicField, DynamicFormMixin

from orders.models import Order, OrderItems
from tests_labs.models import CharacteristicTestLab, TestLab


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('discount',)
        labels = {
            'discount': 'Descuento',
        }


class OrderItemsForm(forms.ModelForm):
    required_css_class = 'required'

    id = forms.IntegerField()

    class Meta:
        model = OrderItems
        fields = ('order', 'id', 'characteristictestlab', 'test_lab',
                  'quantity', 'price', 'sampling_by')
        labels = {
            'characteristictestlab': 'Labfgf.',
            'test_lab': 'Ensayo',
            'quantity': 'Cantidad',
            'price': 'Precio',
            'sampling_by': 'Muestreo por RPG'
        }

    def __init__(self, *args, **kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['id'].label = ''
        self.fields['id'].widget = forms.HiddenInput()

        self.fields['order'].label = ''
        self.fields['order'].widget = forms.HiddenInput()

        # if not self.fields['id']:
        #     self.fields['test_lab'].queryset = TestLab.objects.none()

        self.fields['price'].widget.attrs['step'] = 0.01


OrderItemsFormset = inlineformset_factory(
    Order, OrderItems, form=OrderItemsForm, extra=0, can_delete=False, min_num=1, validate_min=True)
