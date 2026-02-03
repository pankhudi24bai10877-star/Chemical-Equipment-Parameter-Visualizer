from django.shortcuts import render
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dataset

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES['file']
    df = pd.read_csv(file)

    total = len(df)
    avg_flow = df['Flowrate'].mean()
    avg_pressure = df['Pressure'].mean()
    avg_temp = df['Temperature'].mean()

    if Dataset.objects.count() >= 5:
        Dataset.objects.first().delete()

    Dataset.objects.create(
        name=file.name,
        total_equipment=total,
        avg_flowrate=avg_flow,
        avg_pressure=avg_pressure,
        avg_temperature=avg_temp
    )

    type_distribution = df['Type'].value_counts().to_dict()

    return Response({
        "total": total,
        "avg_flowrate": avg_flow,
        "avg_pressure": avg_pressure,
        "avg_temperature": avg_temp,
        "type_distribution": type_distribution
    })
