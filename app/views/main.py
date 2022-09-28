import os
from typing import Tuple

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from app.classes import Query
from app.config import DATA_DIR
from app.generators import generator_commands
from app.models.request_params import RequestParams

app = Blueprint('main', __name__)


@app.route("/perform_query/", methods=['POST'])
def perform_query() -> Response | Tuple[str, int]:
    # Проверка правильности запроса
    try:
        req_value = RequestParams().load(request.values)
    except ValidationError as e:
        return e.messages, 400

    path = os.path.join(DATA_DIR, req_value['file_name'])  # получаем путь к файлу
    query = Query(path)  # создаем экземпляр запроса по пути к файлу

    # Проверяем существует ли файл
    try:
        params = generator_commands(req_value)
        result = query.get_query(params)
    except FileNotFoundError:
        return 'FileNotFound', 400

    return jsonify(result)
