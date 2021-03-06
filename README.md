<h1>CLASSTIME</h1>

<div align="center"><img src="https://capsule-render.vercel.app/api?type=soft&color=auto&height=150&section=header&text=ClassTime&fontSize=70&animation=twinkling" alt="head"/></div>

<hr/>

<div>
    <h3>[프로젝트 기술]</h3>
    <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/>
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/>
    <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
    <img src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=MicrosoftAzure&logoColor=white"/>
</div>

<hr/>

<div>
<h3>[참고 사이트 및 문헌]</h3>

- Flask
    - 점프 투 플라스크: https://wikidocs.net/book/4542
    - vscode flask 개발환경 구축 : https://krksap.tistory.com/1766
</div>

<hr/>

<div>
<h3>[공지사항]</h3>

- 파일 관련
    - .vscode는 vscode에서 flask 실행환경을 설정하기 위한 json 파일이 들어있는 디렉터리입니다.
    - migrations는 flask와 db간의 연동을 관리하기위한 db revision 파일입니다.
    - 파일명들은 flask 구동과 연동되는 이름들 입니다. 바꾸지 말아주세요.
- DB 관련
    - db 설정은 임시로 schema: classtime, user: classtimepm, pw: ct1234로 설정하였습니다. 추후에 상의를 통해 db환경을 다시 설정하도록 하겠습니다.

- 환경설정 관련
    - flask 설치
        - 해당 파일로 가서 pip install flask
    - Flask-Migrate 설치
        - 해당 파일로 가서 pip install flask-Migrate
        - AttributeError: can't set attribute 발생 시 pip install SQLAlchemy==1.3.23
    - Flask-WTF 설치
        - 해당 파일로 가서 pip install Flask-WTF
- 주의사항
    - vscode에서 작업 시 최상위directory(classtime)가 아닌 각각의 하위 파일(home, list, ..등)을 오픈하여 작업해야합니다.
    - flask 설치 및 환경설정이 안되어 있는 경우 환경설정 관련 항목을 참고하여 설정해주세요.
    - app을 찾지 못하는 경우 발생 시, ctrl+shift+p를 눌러 위 커맨트 창에서 Select Interpreter를 통해 interpreter를 수정해주세요.
    - export FLASK_APP=build/app.py 를 입력하여 app.py 위치 수정 필요
- flask 환경설정 관련해서 어려움이 있으시면 연락주세요
</div>
