
### 터미널 열기
- 'Ctrl + `'

# GIT 이란...
> 분산 버전 관리 시스템
> - 코드의 버전(히스토리)를 관리
> - 개발되어 온 과정 파악
> - 이전 버전과의 변경 사항 비교
> 코드의 '변경이력'을 기록하고 '협업'을 원활하게 하는 도구

# GIT의 세가지 영억
> Working Directory
- 실제 작업 영억
> Staging Area
- 중간 준비 영역
> Repositiry
- 버전 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨

# GIT 초기화
```bash
$ git init
```
# 숨긴 폴더 모두 보기
```bash
$ ls -a
```

> 버전 남긴다 = commit 찍다(snapshot)

### 상태 확인 명령어
```bash
$ git status
```

### Staging area에 추가
```bash
$ git add {path}<folder_name>/{file_name}
```
### Repository에 저장하기
```bash
$ git commit -m "commit message"
```

### 사용자 등록(git 기초설정)
```bash
$ git config --global user.email ""
$ git config --global user.name ""
$ git config --global --list
```

### commit 기록 확인하기
```bash
$ git log
```