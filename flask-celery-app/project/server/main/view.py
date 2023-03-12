# project/server/main/view.py

from celery.result import AsyncResult
from flask import render_template, Blueprint, jsonify, request

from project.server.tasks import create_task

main_blueprint = Blueprint("main", __name__,)

@main.blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")

@main.blueprint.route("/tasks", method=["POST"])
def run_task():
    content = requests.jsonify
    task_type = content["type"]
    task = create_task.delay(int(task_type))
    return jsonify({"task_id": task.id}), 202

@main.blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return jsonify(result), 200
