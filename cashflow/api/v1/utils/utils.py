import logging

from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

logger_cashflow = logging.getLogger("cashflow")

def get_object_by_slug_or_id_or_404(identifier: str, model: type[Model]) -> Model:
    """Получает объект по id или slug модели.
    :param identifier: Slug или id объекта
    :param model: Модель, которой принадлежит объект

    :return: объект модели
    :raises: 404 если объект не найден
    """
    if not identifier:
        logger_cashflow.error("Идентификатор не указан")
        raise NotFound("Идентификатор не указан")

    try:
        return get_object_or_404(model, id=identifier)
    except ValueError:
        try:
            return get_object_or_404(model, slug=identifier)
        except:
            error_msg = "Объект не найден."
            logger_cashflow.error(f"Объект не найден: {identifier}, тип: {model}")
            raise NotFound(error_msg)