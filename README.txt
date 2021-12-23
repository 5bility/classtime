[load_balancing.py]

시나리오 1 수행을 위한 로드 밸런서 모듈입니다.

<docker-py 라이브러리 설치>
pip install docker==2.0.0

<실행>
python3 load_balancing.py



[health_check.c] or [health_check(python ver).py]

시나리오 2 수행을 위한 헬스체크 모듈입니다.
health_check.c 파일의 실행에 앞서 사용자 정의 네트워크 생성 후 해당 네트워크를 기반으로 컨테이너 생성합니다.

<사용자 정의 네트워크 생성 명령어>
sudo docker network create --driver bridge --label project=dockerinkpu --label purpose=education --attachable --scope local --subnet 10.0.42.0/28 --ip-range 10.0.42.0/28 5biity
