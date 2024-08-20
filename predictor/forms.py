# predictor/forms.py

from django import forms

class PredictionForm(forms.Form):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    SMOKING_CHOICES = [('Never', 'Never'), ('Former', 'Former'), ('Current', 'Current')]
    YES_NO_CHOICE = [('1', 'Yes'),('0', 'No')]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', widget=forms.Select(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}))
    hypertension = forms.ChoiceField(choices=YES_NO_CHOICE, label='Hypertension', widget=forms.Select(attrs={'class': 'form-control'}))
    heart_disease = forms.ChoiceField(choices=YES_NO_CHOICE, label='Heart Disease', widget=forms.Select(attrs={'class': 'form-control'}))

    smoking_history = forms.ChoiceField(choices=SMOKING_CHOICES, label='Smoking History', widget=forms.Select(attrs={'class': 'form-control'}))
    bmi = forms.FloatField(label='BMI', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter BMI'}))
    HbA1c_level = forms.FloatField(label='Hemoglobin A1C (HbA1c) Level', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hemoglobin A1C (HbA1c) Level'}))
    blood_glucose_level = forms.FloatField(label='Blood Glucose Level', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blood Glucose Level'}))


class ThyroidPredictionForm(forms.Form):
    YES_NO_CHOICE = [(0, 'No'), (1, 'Yes')]
    SEX_CHOICES = [(0, 'Male'), (1, 'Female')]

    age = forms.IntegerField(
        label='Age',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'})
    )
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        label='Sex',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    on_thyroxine = forms.ChoiceField(
        choices=YES_NO_CHOICE,
        label='On Thyroxine',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    pregnant = forms.ChoiceField(
        choices=YES_NO_CHOICE,
        label='Pregnant',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    thyroid_surgery = forms.ChoiceField(
        choices=YES_NO_CHOICE,
        label='Thyroid Surgery',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    TSH_measured = forms.ChoiceField(
        choices=YES_NO_CHOICE,
        label='TSH Measured',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    TT4_measured = forms.ChoiceField(
        choices=YES_NO_CHOICE,
        label='TT4 Measured',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    TBG_measured = forms.ChoiceField(
        choices=YES_NO_CHOICE,
        label='TBG Measured',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
