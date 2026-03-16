import logging

from django import forms

from finance.models import CashFlow

logger_cashflow = logging.getLogger("cashflow")

class CashFlowAdminForm(forms.ModelForm):

    class Meta:
        model = CashFlow
        fields = ['date_created', 'status', 'type', 'category', 'subcategory', 'amount', 'currency', 'comment']


    def clean(self):
        cleaned_data = super().clean()

        type = cleaned_data['type']
        category = cleaned_data['category']
        subcategory = cleaned_data['subcategory']

        logger_cashflow.debug("CashFlowAdminForm clean")

        if type and category and subcategory:
            if category.type != type:
                logger_cashflow.error("Тип категории не совпадает с типом Движения денежных средств.")
                self.add_error(
                    'category',
                    "Тип категории не совпадает с типом Движения денежных средств."
                )
            if subcategory.category != category:
                logger_cashflow.error("Подкатегория не принадлежит выбранной категории.")
                self.add_error(
                    'subcategory',
                    "Подкатегория не принадлежит выбранной категории."
                )

        return cleaned_data


