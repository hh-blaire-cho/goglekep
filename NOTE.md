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
- 메인앱 설정: `export FLASK_APP=goglekep` (goglekep 모듈화 필요)

### goglekep 모듈화
- gogglekaap이라는 별도 directory를 만든 후 module로 만들어주기
- 이때 순환 참조 장애 방지를 위해 팩토리패턴을 사용하여 create_app으로 감싸준다.