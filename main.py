import os
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "tempkey")  # 환경변수 또는 기본값

# ✅ 관리자 로그인 페이지
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == os.environ.get("ADMIN_PASS"):
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            return "❌ 비밀번호가 틀렸습니다.", 403
    return render_template("admin_login.html")

# ✅ 관리자 대시보드
@app.route("/admin")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/admin-login")
    return render_template("admin.html")

# ✅ 로그아웃
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

# ✅ 앱 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
