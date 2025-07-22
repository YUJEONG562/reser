from flask import Blueprint

# Blueprint 객체 생성
main_bp = Blueprint('main', __name__)

# 이 blueprint에 라우트 등록
@main_bp.route("/")
def home():
    return "예약 시스템 메인 페이지"
