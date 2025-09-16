# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class AgentView(APIView):
    def post(self, request):
        user_input = request.data.get("message", "")
        
        # Placeholder AI response (you can integrate OpenAI, Hugging Face, etc.)
        ai_response = f"AI Agent received: {user_input}"
        
        return Response({"response": ai_response})


