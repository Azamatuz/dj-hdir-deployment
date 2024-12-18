import base64
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from google.cloud import vision

def process_image(request):
    image_data = request.POST.get('image')
    if image_data:
        # Decode the base64 image
        image_data = base64.b64decode(image_data.split(',')[1])

        # Initialize the Google Vision client
        client = vision.ImageAnnotatorClient()

        # Create an image object
        image = vision.Image(content=image_data)

        # Perform text detection on the image
        text_response = client.text_detection(image=image)
        texts = text_response.text_annotations

        # Perform object localization on the image
        object_response = client.object_localization(image=image)
        objects = object_response.localized_object_annotations

        # Extract product codes and their coordinates
        product_codes = []
        for text in texts:
            if text.description.isdigit():
                product_codes.append({
                    'code': text.description,
                    'bounding_poly': [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
                })

        # Extract box coordinates
        boxes = []
        for obj in objects:
            if obj.name == 'Box':
                boxes.append({
                    'name': obj.name,
                    'bounding_poly': [(vertex.x, vertex.y) for vertex in obj.bounding_poly.normalized_vertices]
                })

        return JsonResponse({'product_codes': product_codes, 'boxes': boxes})
    return JsonResponse({'error': 'No image data provided'}, status=400)

@login_required
def ScanView(request):
    if request.method == 'POST':
        return process_image(request)
    return render(request, 'vision/scan.html')

@login_required
def ScanViewTest(request):
    if request.method == 'POST':
        return process_image(request)
    return render(request, 'vision/scan-flow.html')