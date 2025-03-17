# Django
## 0. 

- `.gitignore` (gitignore.io에서 python, window, mac, django 추가)
- 가상환경 설정 `python -m venv venv`
- 가상환경 활성화 `source venv/Scripts/activate`
- `README.md`

## 1. Django  프로젝트
- **프로젝트**는 Django 웹 애플리케이션의 전체 구조를 관리하고, 앱을 포함하는 상위 레벨입니다.
- **앱**은 웹 애플리케이션 내에서 특정 기능을 담당하는 모듈로, 프로젝트 내 여러 개가 있을 수 있습니다.
1. django 설치
```shell
pip install django
```

2. 프로젝트 생성
```shell
django-admin startproject <pjt-name> <path>
```
수업시간엔 아래처럼 씀
```
django-admin startproject first_pjt .
```

3. 서버실행 (ctrl + c: 종료)
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app-name>
```
수업시간에는 django-admin startapp first_app

5. 앱 등록(`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```
    first_pjt : 프로젝트 폴더 (앱을 통합관리)
        - settings.py에서 여러가지 설정들을 할 수 있다
        - 앱등록은 settings.py에서 'ISTALLED_APPS' 리스트에 내가 생성한 앱을 등록한다

<MTV 패턴에 대한 이해>
- view: 사용자의 요청에 따라 적절한 데이터를 반환하고, 템플릿을 렌더링하여 응답을 생성하는 역할
- template: HTML, CSS, Javascript를 활용하여 화면 구성
- modle: 데이터베이스를 관리(데이터를 저장, 수정, 삭제, 조회)

1️⃣ 클라이언트가 요청을 보냄 → http://127.0.0.1:8000/some-page/
2️⃣ urls.py에서 요청을 처리할 view를 찾음 
3️⃣ views.py에서 요청을 받고 필요한 데이터를 models.py에 요청
4️⃣ models.py가 데이터베이스에서 데이터를 가져옴
5️⃣ views.py가 가져온 데이터를 template(HTML 파일)에 전달
6️⃣ 완성된 HTML을 클라이언트에게 반환하여 브라우저에 출력


1. 특정 URL 요청을 처리하기 위한 경로를 설정
- urls.py에서 `urlpateerns`라는 리스트에
- **path('index/', views.lunch)** 생성
- **동적경로 설정** : **'profile/<_username>'**
- 동적경로: URL에서 특정 값을 변수처럼 받아서 view 함수로 전달하는 역할을 합니다.
- path() 함수를 사용하여 URL과 views.py의 함수(views.lunch)를 연결

2.  views.py에서 <lunch> 함수 선언
def lunch(request):
    menu = ['짜장면', '불닭볶음면', '마라탕']
    pick = random.choice(menu)
    context = {
        'pick' : pick #'딕셔너리이름' : 변수
    }
    return render(request, 'lunch.html', context)
- first_app에서 views.py에 lunch라는 함수를 만들고, HTML을 렌더링(데이터를 HTML로 변환하여 보여주는 과정)하도록 설정
- **context**: view에서 템플릿으로 데이터를 전달하는 딕셔너리

# first_app에서 templates라는 새로운 폴더 생성(템플릿을 모아놓는 공간)

4. templates안에 <index>.html이라는 파일 생성
    - templates는 HTML을 이용하여 화면을 구성해주는것
    - index.html에서 !+tab으로 구조 생성
    - body에 h1으로 hello! 생성



특정 url에 해당하는 경로 설정 path(url, views.함수)
> views.py에서 html과 결합된 데이터를 가져오는 함수 생성
def 함수이름(request):
context = {'':}
return render(request, 함수이름.html, context)
> templates 파일에 함수이름.html 이라는 템플릿 생성