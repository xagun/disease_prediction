# predictor/views.py

from django.shortcuts import render
from .forms import PredictionForm
from .load_model import model


def index(request):
    return render(request, 'predictor/index.html')

def thyroid_prediction(request):
    return render(request, 'predictor/thyroid.html')

def diabetes_prediction(request):
    result = None  # Initialize result as None
    form_data = {}  # Initialize form_data as an empty dictionary

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract the data from the form
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            hypertension = form.cleaned_data['hypertension']
            heart_disease = form.cleaned_data['heart_disease']
            smoking_history = form.cleaned_data['smoking_history']
            bmi = form.cleaned_data['bmi']
            HbA1c_level = form.cleaned_data['HbA1c_level']
            blood_glucose_level = form.cleaned_data['blood_glucose_level']

            # Encode categorical variables as needed
            gender_encoded = 1 if gender == 'Male' else 0  # Example encoding
            smoking_encoded = {'Never': 0, 'Former': 1, 'Current': 2}[smoking_history]
            hypertension_encoded = 1 if hypertension == 'Yes' else 0  # Example encoding
            heart_disease_encoded = 1 if heart_disease == 'Yes' else 0  # Example encoding

            # Create input array for the model
            input_data = [[gender_encoded, age, hypertension_encoded, heart_disease_encoded, smoking_encoded, bmi, HbA1c_level, blood_glucose_level]]
            
            # Get the prediction from the model
            prediction = model.predict(input_data)
            
            # Collect all form data to pass back to the template
            form_data = {
                'gender': gender,
                'age': age,
                'hypertension': hypertension,
                'heart_disease': heart_disease,
                'smoking_history': smoking_history,
                'bmi': bmi,
                'HbA1c_level': HbA1c_level,
                'blood_glucose_level': blood_glucose_level
            }
            if prediction[0] == 1:
                result = "The person is at risk of the disease."
            else:
                result = "The person is not at risk of the disease."

            return render(request, 'predictor/result.html', {
        'form': form,
        'result': result,
        'form_data': form_data
    })
    else:
        form = PredictionForm()

    return render(request, 'predictor/diabetes.html', {'form': form})
