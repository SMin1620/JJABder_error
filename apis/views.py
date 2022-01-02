from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email, ValidationError
from django.db import IntegrityError

from django.contrib.auth.models import User
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


# register
class UserCreateView(BaseView):
    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해 주세요.', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해 주세요.', status=400)
        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            return self.response(message='이메일을 입력해 주세요.', status=400)

        # 예외 처리
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디 입니다.', status=400)

        return self.response({'user.id': user.id})


# Login
class UserLoginView(BaseView):
    def post(self, request):
        username = request.POST.get('username', '').strip()
        if not username:
            return self.response(message='아이디를 입력해 주세요.', status=400)
        password = request.POST.get('password', '').strip()
        if not password:
            return self.response(message='비밀번호를 입력해 주세요.', status=400)

        # authenticate 함수는 username, password이 일치하지 않을경우, None을 반환.
        user = authenticate(request, username=username, password=password)
        if user is None:
            return self.response(message='아이디 또는 비밀번호가 일치하지 않습니다.', status=400)

        login(request, user)

        return self.response()


# logout
class UserLogoutView(BaseView):
    def get(self, request):
        logout(request)
        return self.response()


# Cart Add
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
