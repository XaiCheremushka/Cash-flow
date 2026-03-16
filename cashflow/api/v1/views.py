import logging

from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.views import APIView

from api.v1.utils import utils
from finance.models import Category, Subcategory, Type

logger_cashflow = logging.getLogger("cashflow")


@extend_schema(
    tags=["ДДС"],
    summary='Получение подкатегорий по категории',
    description="Получение всех подкатегорий по указанной категории.",
    parameters=[
        OpenApiParameter(
            name="identifier",
            location=OpenApiParameter.PATH,
            description="ID или slug категории",
            required=True,
            type=str
        )
    ],
    responses={
        200: OpenApiExample('OK'),
        404: OpenApiExample('Пример ответа, если категория не найдена')
    },
    examples=[
        OpenApiExample(
            'OK',
            summary='Пример успешного ответа',
            value={
                "status": 'Success',
                "subcategories": [
                    {'id': 1, 'name': "VPS", 'slug': "vps"},
                    {'id': 2, 'name': "Proxy", 'slug': "proxy"},
                ]
            },
            response_only=True
        ),
        OpenApiExample(
            'Пример ответа, если категория не найдена',
            value={"detail": "Категория не найдена."},
            status_codes=['404'],
            response_only=True,
        )
    ]
)
class SubcategoriesByCategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """Обработка запроса к серверу для получения подкатегорий указанной категории в админ-панели"""
        identifier = kwargs.get('identifier')
        logger_cashflow.debug(f"Получение подкатегорий категории с id(slug)={identifier}")

        category_obj = utils.get_object_by_slug_or_id_or_404(identifier, Category)

        logger_cashflow.debug(f"Получение категорий по категории={category_obj.name}")

        subcategories = (
            Subcategory.objects
            .filter(category=category_obj)
            .order_by('id')
            .values('id', 'name', 'slug')
        )

        logger_cashflow.debug(f'Количество найденных подкатегорий: {subcategories.count()}')

        return JsonResponse({
            'status': "Success",
            'subcategories': list(subcategories)
        })


@extend_schema(
    tags=["ДДС"],
    summary='Получение категорий по типу ДДС',
    description="Получение всех категорий по указанному типу.",
    parameters=[
        OpenApiParameter(
            name="identifier",
            location=OpenApiParameter.PATH,
            description="ID или slug типа",
            required=True,
            type=str
        )
    ],
    responses={
        200: OpenApiExample('OK'),
        404: OpenApiExample('Пример ответа, если тип не найден')
    },
    examples=[
        OpenApiExample(
            'OK',
            summary='Пример успешного ответа',
            value={
                "status": 'Success',
                "subcategories": [
                    {'id': 1, 'name': "Инфраструктура", 'slug': "infrastruktura"},
                    {'id': 2, 'name': "Маркетинг", 'slug': "marketing"},
                ]
            },
            response_only=True
        ),
        OpenApiExample(
            'Пример ответа, если тип не найден',
            value={"detail": "Тип не найден."},
            status_codes=['404'],
            response_only=True,
        )
    ]
)
class CategoriesByTypesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """Обработка запроса к серверу для получения категорий указанного типа в админ-панели"""
        identifier = kwargs.get('identifier')
        logger_cashflow.debug(f"Получение категорий по типу с id(slug)={identifier}")

        type_obj = utils.get_object_by_slug_or_id_or_404(identifier, Type)

        logger_cashflow.debug(f"Получение категорий по типу={type_obj.name}")

        categories = (
            Category.objects
            .filter(type=type_obj)
            .order_by('id')
            .values('id', 'name', 'slug')
        )

        logger_cashflow.debug(f'Количество найденных категорий: {categories.count()}')

        return JsonResponse({
            'status': "Success",
            'categories': list(categories)
        })

