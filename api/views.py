from django.http import HttpRequest,JsonResponse,FileResponse
from django.views import View
from .models import Document
import json



class DocumentView(View):
    def get(self, request:HttpRequest,n:str):
        #Get the model instance that corresponds to the requested file
        # my_model = get_object_or_404(MyModel, pk=pk)
        # Open the file using Python's built-in `open()` function
        try:
            document=Document.objects.get(name=n)
            file = open(document.file.path, 'rb')
            # Return the file as a `FileResponse`
            response = FileResponse(file)
            return response
        except:
            return JsonResponse({"result":'File not found'})
    def post(self,request,name:str):
        # Get the uploaded file from the request object
        try:
            ob=Document.objects.get(name=name)
            return JsonResponse({"result":"the key is invalid"})
        except:
            uploaded_file = request.FILES['file']
            my_file = Document(name=name, file=uploaded_file)
            # Save the model instance
            my_file.save()
            return JsonResponse({'success': True})