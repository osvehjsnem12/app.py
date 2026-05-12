from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "서버 작동중!"

    await fetch('/collect', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });

    document.body.innerHTML = "<h1>완료!</h1>";

})();
</script>

</body>
</html>
"""

@app.route("/")
def index():

    info = {
        "접속 시간": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "IP 주소": request.headers.get("X-Forwarded-For", request.remote_addr),
        "접속 방식": request.method,
        "접속 경로": request.path,
        "브라우저": str(request.user_agent),
    }

    print("\n===== 서버 정보 =====")
    print(json.dumps(info, indent=4, ensure_ascii=False))

    return PAGE


@app.route("/collect", methods=["POST"])
def collect():

    print("\n===== 기기 정보 =====")
    print(json.dumps(request.get_json(), indent=4, ensure_ascii=False))

    return jsonify({"결과": "성공"})


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
