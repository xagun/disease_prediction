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
