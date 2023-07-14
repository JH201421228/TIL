# CLI
- Command Line Interface

- 새 폴더 만들기
```bash
$ mkdir new_folder
```

- 작업 위치를 new_folder로 이동
```bash
$ cd new_folder
```

- 현재 작업 위치를 열기
```bash
# . -> 현재 위치 (상대 경로)
$ start . 
# 현재 위치를 VSCode로 열기
$ code .
```

- 현재 작업 위치의 파일 목록
```bash
$ ls
```

- 파일의 이름을 바꾸거나 위치를 옮기거나
```bash
$ mv {이동할 대상} {이동될 위치}
$ mv {이름 바꿀 대상} {바꿀 이름}
```

### 상대 경로 절대 경로
1. 절대 경로
/c/Users/SSAFY/Desktop/new_folder

2. 상대 경로
- 나를 기준으로 경로를 지정

- 삭제
```bash
$ rm {파일 명}
$ rm -r {폴더}
```