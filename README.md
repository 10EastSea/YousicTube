# YousicTube

[![button](https://img.shields.io/badge/link-YousicTube-brightgreen)](https://github.com/10EastSea/YousicTube)

이 프로젝트 파일은 YousicTube 사이트의 실행파일입니다.

YousicTube는 악보제작을 자동으로 해주는 웹 애플리케이션입니다. 제공해주는 서비스는 다음과 같습니다.

1. 유튜브 음악 영상 커뮤니티 사이트
2. 분석된 코드를 통해 원하는 곡 악보 제작
3. 음악 플랫폼 데이터를 분석해 동일한 코드 진행의 음악들을 추천

## 목차
- [설치](#설치)
- [사용법](#사용법)
- [크레딧](#크레딧)

## 설치

이 프로젝트는 python을 사용하기 때문에 python 3.6.9 이상의 버전이 설치된 컴퓨터와 pip가 필요합니다.

python 및 라이브러리 버전과 관련하여 생길 오류를 방지하기 위해, python 가상환경을 구축하여 실행했으며 다음의 오픈소스 라이브러리를 사용하였습니다.

* [Django](https://www.djangoproject.com/) (3.0.8)
* [youtube-dl](https://youtube-dl.org/) (2020.7.28)
* [ffmpeg](https://ffmpeg.org/) (1.4)
* [librosa](https://librosa.org/) (0.8.0)
* [vamp](https://code.soundsoftware.ac.uk/projects/vamp-plugin-pack) (1.1.0)
* [pillow](https://github.com/python-pillow/Pillow) (7.2.0)
* [tensorflow-cpu](https://www.tensorflow.org/?hl=ko) (2.3.0)

우선 프로젝트를 다운받고 다음 명령어를 입력해 필요한 라이브러리를 다운받습니다.

```sh
$ pip install Django
$ pip install youtube-dl
$ pip install ffmpeg
$ pip install librosa
$ pip install vamp
$ pip install pillow
$ pip install tensorflow-cpu
```
> 1. pip install ffmpeg를 한 후 실행했을 시 파일의 포맷을 찾을 수 없다는 에러가 나오면, 각 컴퓨터 운영체제에 맞는 ffmpeg를 따로 설치진행해 주어야 함 ([홈페이지](https://ffmpeg.org/download.html)에서 다운로드)
> 2. pip install vamp를 한 후에 반드시 [vamp 플러그인 홈페이지](https://code.soundsoftware.ac.uk/projects/vamp-plugin-pack)에서 Chordino and NNLS chroma 플러그인, beatRoot 플러그인을 설치해주어야 함

## 사용법

다음 프로젝트를 실행하기 위해선 로컬 서버에서 운영하는 방법이 존재합니다.
로컬 서버에서 이 프로젝트를 운영하는 방법은 프로젝트 최상위 폴더내에 존재하는 manage.py를 실행함으로써 운영할 수 있습니다. 다음의 명령어를 입력하면 로컬서버에서 실행할 수 있습니다.

```sh
$ python manage.py runserver --settings=config.settings.local
```

만약 프로젝트를 처음 실행하는 것이라면 데이터베이스를 만들어주어야 하기 때문에 다음과 같은 명령어를 우선 입력해주어야 합니다.

```sh
$ python manage.py makemigrations --settings=config.settings.local
$ python manage.py migrate --settings=config.settings.local
```

## 크레딧

* 웹 사이트 및 서버 개발자: [EastSea](https://github.com/10EastSea)
* 악보 추출 및 음악 추천기능 개발자: [Jiker Bug](https://github.com/jikerbug)
