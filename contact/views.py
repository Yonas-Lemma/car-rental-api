# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.core.mail import send_mail
# from .models import Contact
# from .serializers import ContactSerializer

# class ContactView(APIView):
#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # Send email
#             send_mail(
#                 subject=f"New contact form submission from {serializer.validated_data['name']}",
#                 message=serializer.validated_data['message'],
#                 from_email=serializer.validated_data['email'],
#                 recipient_list=['yonbetizazu@gmail.com'],  # Replace with admin email
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from .serializers import ContactSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from the serializer
            name = serializer.validated_data['name']
            user_email = serializer.validated_data['email']  # This is the user's email
            message = serializer.validated_data['message']

            # Send email
            try:
                send_mail(
                    subject=f"New contact form submission from {user_email}",
                    message=message,
                    from_email=user_email,  # This should be the user's email
                    recipient_list=['yonbetizazu@gmail.com'],  # Replace with your email
                )
                return Response({"message": "Email sent successfully!"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)