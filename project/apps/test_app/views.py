from django.http import JsonResponse

from project.abstract.views import BaseReadView


class TestView(BaseReadView):

    async def get(self, request, *args, **kwargs):
        return JsonResponse(data={"hello": "world"}, status=200)
