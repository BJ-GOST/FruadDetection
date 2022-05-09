from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import fraud_serializer
from .models import fraud
import joblib

# Create your views here.



@api_view(['GET'])
def api_overview(request):
	api_urls = {

	}
	return Response(api_urls)



@api_view(['GET'])
def fraud_detector(request):
	queryset= fraud.objects.all()
	serializer = fraud_serializer(fraud, many=True)
	return Response(serializer.data)



@api_view(['POST'])
def check_fraud(request):
	serializer=fraud_serializer(data=request.data)
	if serializer.is_valid():
		v1 = request.data.get('v1', None)
		v2 = request.data.get('v2', None)
		v3 = request.data.get('v3', None)
		v4 = request.data.get('v4', None)
		v5 = request.data.get('v5', None)
		v6 = request.data.get('v6', None)
		v7 = request.data.get('v7', None)
		v8 = request.data.get('v8', None)
		v9 = request.data.get('v9', None)
		v10 = request.data.get('v10', None)
		v11= request.data.get('v11', None)
		v12= request.data.get('v12', None)
		v13= request.data.get('v13', None)
		v14= request.data.get('v14', None)
		v15= request.data.get('v15', None)
		v16= request.data.get('v16', None)
		v17= request.data.get('v17', None)
		v18= request.data.get('v18', None)
		v19= request.data.get('v19', None)
		v20= request.data.get('v20', None)
		v21= request.data.get('v21', None)
		v22= request.data.get('v22', None)
		v23= request.data.get('v23', None)
		v24= request.data.get('v24', None)
		v25= request.data.get('v25', None)
		v26= request.data.get('v26', None)
		v27= request.data.get('v27', None)
		v28= request.data.get('v28', None)
		v29= request.data.get('v29', None)
		v30= request.data.get('v30', None)
		prediction_fields = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, 
		v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
		v21, v22, v23, v24, v25, v26, v28, v29, v30]
		model = joblib.load('FraudPrediction.joblib')
		prediction = model.predict([prediction_fields])

		serializer.save()
	else:
		serializer = fraud_serializer()
	return Response(serializer.data)