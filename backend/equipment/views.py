import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dataset
from .serializers import DatasetSerializer
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES['file']
    df = pd.read_csv(file)

    total = len(df)
    avg_flow = df['Flowrate'].mean()
    avg_pressure = df['Pressure'].mean()
    avg_temp = df['Temperature'].mean()

    # Delete older datasets (keep last 5)
    if Dataset.objects.count() >= 5:
        Dataset.objects.first().delete()

    dataset = Dataset.objects.create(
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

@api_view(['GET'])
def history(request):
    datasets = Dataset.objects.all().order_by('-uploaded_at')
    serializer = DatasetSerializer(datasets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def generate_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, "Chemical Equipment Report")
    p.drawString(100, 730, "Generated Summary")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='report.pdf')