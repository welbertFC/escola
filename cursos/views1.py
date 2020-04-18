from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    Api de curso da escola
    """

    def get(self, request):
        #print(request.user)
        cursos = Curso.objects.all()  # all estou bucando todos os objetos
        serializer = CursoSerializer(cursos, many=True)  # many siginifica que estou passando varios objetos
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"id": serializer.data['id'], "curso:": serializer.data['titulo'], "mensagem HTTP ": status.HTTP_200_OK}, status=status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):
    """
    API de Avaliação da escola
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
