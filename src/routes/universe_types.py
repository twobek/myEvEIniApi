from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from src import db
from src.crud.universe_types import get_all_types, create_type, merge_type, merge_whole_page
from src.services.eve_api_service import EveAPIService as eveApi

universe_types_bp = Blueprint('universe_types', __name__)

@universe_types_bp.route("/universe_types/", methods=["GET"])
def read_types():
    dbc: Session = db.SessionLocal()
    try:
        types = get_all_types(dbc)
        return jsonify([type_.type_id for type_ in types])
    finally:
        dbc.close()

@universe_types_bp.route("/", methods=["GET"])
def add_type():
    return jsonify({"message":"Shit is working"}), 200

@universe_types_bp.route("/update_id", methods=["POST"])
def update_id():
    typeId = request.args.get('typeId', type=int)
    dbc: Session = db.SessionLocal()
    try:
        merge_type(dbc, typeId, 1)
        return jsonify({"message": f"TypeId {typeId} successfully resettet"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        dbc.close()

@universe_types_bp.route("/merge_page/", methods=["POST"])
def merge_one_page():
    page = request.args.get('page', type=int)
    try:
        typeIdList, maxPages = eveApi.get_types_list(page)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    dbc: Session = db.SessionLocal()
    try:
        merge_whole_page(dbc, typeIdList, page)
        return jsonify({"message": f"Page {page} successfully merged"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        dbc.close()
