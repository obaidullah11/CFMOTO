from django import forms
from django.utils.safestring import mark_safe

class CustomManyToManyWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []

        # Custom rendering logic for the widget
        rendered_data = []
        for choice in self.choices:
            rendered_data.append(
                f'<label><input type="checkbox" name="{name}" value="{choice[0]}"{" checked" if choice[0] in value else ""}> {choice[1]}</label>'
            )

        return mark_safe('\n'.join(rendered_data))

    def value_from_datadict(self, data, files, name):
        selected_values = data.getlist(name)
        return [v for v in selected_values if v]

    def value_omitted_from_data(self, data, files, name):
        return False
