from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.contrib.auth.models import User
from django.db.models import Avg
import requests
from django import forms
import json
from decimal import Decimal
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = CalculatorForm(request.POST)
            if form.is_valid():

                year = form.cleaned_data.get('Year')
                size = form.cleaned_data.get('Size')
                description = form.cleaned_data.get('Description')
                make = form.cleaned_data.get('Make')
                model = form.cleaned_data.get('Model')
                
                make = make.lower()

                url = "https://ussouthcentral.services.azureml.net/workspaces/fc99097f01f349e2b6c076486b11bd6a/services/06579f005e044a81bd6f06e43252afd0/execute"

                querystring = {"api-version":"2.0","details":"true"}

                payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"Price\",\r\n        \"Year\",\r\n        \"Size\",\r\n        \"Description\",\r\n        \"make\",\r\n        \"model\",\r\n        \"NumUniqueNgrams\",\r\n        \"NGramsString\",\r\n        \"Preprocessed Description.[yoshi]\",\r\n        \"Preprocessed Description.[fall]\",\r\n        \"Preprocessed Description.[kx450f]\",\r\n        \"Preprocessed Description.[crf_run]\",\r\n        \"Preprocessed Description.[run_excellent]\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"0\",\r\n          \"" + year + "\",\r\n          \"" + size + "\",\r\n          \"" + description + "\",\r\n          \"" + make + "\",\r\n          \"" + model + "\",\r\n          \"2\",\r\n          \"value\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  },\r\n  \"GlobalParameters\": {}\r\n}"
                headers = {
                    'Authorization': "Bearer Hz+fKMYqeOM2FUrTIF0l9Zk5DiA13saWg3HO8XdXJ/3W6FQsfyALqINsRU8loMLwBS8s00IWzLZgLvArZwKcGg==",
                    'Content-Type': "application/json",
                    'cache-control': "no-cache",
                    'Postman-Token': "1ba04d53-9e44-4f5e-b0c4-454e483cc98b"
                    }

                response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

                start = str(response.text).find('Values":[["')
                s = str(response.text)[start:]            
                end = str(response.text).find(']]')
                values = str(response.text)[start + 11 : end - 1]
                values = values.replace("\"", "")
                valueList = values.split(',')

                value = valueList[-1]
                value = round(Decimal(value), 2)

            else:
                value = ""

        else:
            form = CalculatorForm()
            value = ""

        context = {
            'form': form, 
            'value': value,
        }

        return request.dmp.render('calculator.html', context)

    else:
        return HttpResponseRedirect('/homepage/login/')



class CalculatorForm(forms.Form):
    Year = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'year'}), max_length=100)
    Size = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'size'}), max_length=100)
    Description = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'description'}), max_length=100)
    Make = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'make'}), max_length=100)
    Model = forms.CharField(label='',  widget=forms.TextInput(attrs={'placeholder': 'model'}), max_length=100)

    
    def clean(self):

        if len(self.cleaned_data.get('Year')) < 4: 
          raise forms.ValidationError("Please enter a 4 digit year")

        return self.cleaned_data