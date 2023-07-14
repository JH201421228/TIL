
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
### 최근 commit 이름 변경
```bash
$ git commit --amend
#vim에서 커밋 내용 수정하기
```

> 메모장 상태에서 insert 누르고 이름 변경 esc로 탈출 ':wq'로 완전 탈출 (write, quit)

### 원격 저장소
> remote Repository
    - github
    - gitlab

### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# vim git 설정 파일열기
$ vim ~/.gitconfig
# insert 키
# 모든 내용 삭제
# esc
# :wq
```

### vscode로 열기
```bash
$ code ~/.gitconfig
```

### 주의
```bash
$ git init
# 사용시 현재 관리할 폴더에서 사용
```

### 현재 폴더
```bash
$ git add .
# '.'은 현재 폴더
```

### 제거하기
```bash
$ git rm --cached <files>
```

### 한줄로 만들기
```bash
$ git log --oneline
```

### 깃헙 업로드 하기
```bash
# 파일 수정상태 확인
$ git add .
$ git commit -m "내용"
$ git push origin master
```

### 원격 저장소 git에 등록
```bash
$ git remote a
```

### 원격 저장소에 있는 내용 복제
- 최초로 다운 받을때
```bash
$ git clone repository_url
```

### 20230713 수정

### 20230714 수업 내용

- 0. init
- add, commit push
- pull clone