# Step By Step 기록

# 개발환경 세팅

## 가상환경 및 인터프리터
- 가상환경명: `flaskenv`
- 인터프리터경로: `~/Desktop/myproj/flask/flaskenv/bin/python`

## pip install
아래 요구사항에 맞게 패키지를 다운받는다.
- Flask==1.1.2
- Werkzeug==1.0.1
- click==7.1.2
- itsdangerous==1.1.0
- Jinja2==2.11.3
- MarkupSafe==1.1.1

```
pip install Flask==1.1.2 Werkzeug==1.0.1 click==7.1.2 itsdangerous==1.1.0 Jinja2==2.11.3 MarkupSafe==1.1.1
flaskenv HYEONHUI 🎉   ~/Desktop/myproj/flask/gogglekaap   newbie  pip install Flask==1.1.2 Werkzeug==1.0.1 click==7.1.2 itsdangerous==1.1.0 Jinja2==2.11.3 MarkupSafe==1.1.1
Requirement already satisfied: Flask==1.1.2 in /Users/I751244/Desktop/myproj/flask/flaskenv/lib/python3.8/site-packages (1.1.2)
Requirement already satisfied: Werkzeug==1.0.1 in /Users/I751244/Desktop/myproj/flask/flaskenv/lib/python3.8/site-packages (1.0.1)
Requirement already satisfied: click==7.1.2 in /Users/I751244/Desktop/myproj/flask/flaskenv/lib/python3.8/site-packages (7.1.2)
Requirement already satisfied: itsdangerous==1.1.0 in /Users/I751244/Desktop/myproj/flask/flaskenv/lib/python3.8/site-packages (1.1.0)
Requirement already satisfied: Jinja2==2.11.3 in /Users/I751244/Desktop/myproj/flask/flaskenv/lib/python3.8/site-packages (2.11.3)
Requirement already satisfied: MarkupSafe==1.1.1 in /Users/I751244/Desktop/myproj/flask/flaskenv/lib/python3.8/site-packages (1.1.1)
```

이후 터미널에서 `pip3 freeze > requirements.txt` 라고 하면 파일 생김

## 플라스크 환경변수 설정

- 디버그모드 설정: `export FLASK_ENV=development`
- 메인앱 설정: `export FLASK_APP=gogglekaap` (gogglekaap 모듈화 필요)

### gogglekaap 모듈화
- gogglekaap이라는 별도 directory를 만든 후 module로 만들어주기
- 이때 순환 참조 장애 방지를 위해 팩토리패턴을 사용하여 create_app으로 감싸준다.


### [CSRF 공격 조치](https://github.com/hidekuma/gogglekaap/wiki/D.1.-CSRF-%EB%B0%A9%EC%96%B4:-Flask-WTF%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-CSRF-%EA%B3%B5%EA%B2%A9-%EC%A1%B0%EC%B9%98):
CSRF (Cross Site Request Forgery)의 약자로, 사이트간 요청 위조를 뜻한다. 희생자의 의지와 무관하게 공격자가 의도한 작업이 진행 되게끔 유도하는 해킹방법. (예: 클릭하면 100만원이란 버튼이었는데...)

그래서 해당 공격에 대한 조치로, `쓰기/변경이 s가능한 엔드포인트 및 메서드들`에 특정 토큰을 포함해서 요청하도록 해야한다.
- `app.config['SECRET_KEY'] = 'qwerty'` 로 csrf token이 만들어지도록 하자
