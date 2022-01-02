from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from shop.models import Cart


# Create your views here.
# CBV 기반의 base api
@method_decorator(csrf_exempt, name='dispatch')
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message
        }
        return JsonResponse(result, status=status)


class CartCreateView(BaseView):
    def post(self, request):
        # 유저의 pk 및 상품의 pk가 올바른지 확인
        try:
            product_id = request.POST.get('pk', '')
        except ValueError:
            return self.response(message='잘못된 요청입니다.', status=400)

        # 장바구니에 추가
        if product_id in Cart.objects.all():
            return self.response(message='이미 장바구니에 있습니다.', status=400)
        else:
            Cart.objects.create(
                product_id=product_id,
                quantity=1
            )

        return self.response({})







