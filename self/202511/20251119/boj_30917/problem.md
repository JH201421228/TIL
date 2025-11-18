 30917번
제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
질문 게시판
A+B - 10 (제1편) 인터랙티브
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	2035	1208	1023	61.257%
문제
1 이상 9 이하의 정수 A, B에 대해 A+B의 값을 출력해야 한다. 단, 이 문제는 인터랙티브 (상호작용) 문제이다. 이 문제에서는 A와 B의 값이 바로 주어지지 않고, 채점기와의 상호작용을 통해 그 값을 알아내야 한다.

출력
여러분은 채점기에게 최대 18번 질문할 수 있다. 질문의 형태는 다음 중 하나이다.

? A x - A의 값이 x인지 물어본다.
? B x - B의 값이 x인지 물어본다.
예를 들어 A의 값이 4인지 물어보려면 ? A 4를 출력하면 된다. 이때 x는 1 이상 9 이하의 정수여야 한다.

질문을 출력한 뒤 실제로 질문을 채점기에게 보내려면 표준 출력을 flush해야 한다. 자세한 내용은 아래의 노트 란을 참조하자.

질문을 보낸 뒤에는 채점기로부터 정수 하나를 입력받는다. 그 수는 질문의 답이 "예"인 경우 1, "아니요"인 경우 0이다.

A와 B의 값을 알아냈으면 A+B를 계산하여 다음과 같은 형태로 출력한다.

! x - A+B의 값은 x이다.
예를 들어 A+B가 10인 경우 ! 10을 출력하면 된다. 이는 질문 횟수에 포함되지 않는다.

아래의 "노트" 란에 여러 언어에 대한 예시 코드가 작성되어 있다. 단, 완성되지 않은 코드이므로 빈 공간은 직접 채워 넣어야 한다.

예제 입력 1 
​
0

0

1

0

1
예제 출력 1 
? A 1

? A 2

? A 3

? B 1

? B 2

! 5
상호작용 문제의 입출력 예제는 일반적인 문제와 달리 둘을 동시에 읽어야 한다. 위의 예제는 다음과 같이 해석된다.

? A 1을 출력한다.
0을 입력받는다.
? A 2를 출력한다.
0을 입력받는다.
? A 3을 출력한다.
1을 입력받는다.
? B 1을 출력한다.
0을 입력받는다.
? B 2를 출력한다.
1을 입력받는다.
! 5를 출력한다.
꼭 ? A 1을 첫 번째로 출력할 필요는 없고, ? B 4같은 다른 질문도 가능하다. 마찬가지로 첫 입력이 꼭 0이라는 보장은 없다. 또한 빈 줄은 편의를 위해 끼워넣은 것일 뿐, 실제로 빈 줄을 출력하거나 입력받으면 안 된다.

노트
상호작용 문제는 채점 방식이 복잡하기 때문에, 문제에 주어진 규약을 지키지 않았을 때 "틀렸습니다"가 아닌 다른 결과가 나올 수도 있음에 유의하자.

예시 코드

C

#include <stdio.h>
int main() {
    int resp;
    for(int a=1; a<=9; a++){
        // A가 a인지 물어보고 flush를 한다.
        printf("? A %d\n", a); 
        fflush(stdout);

        // 채점기의 답변을 입력받는다.
        scanf("%d", &resp);

        if(resp == 1){
            // 답변이 "예"이므로 A의 값은 a이다.
            // B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
            int b = 0;
            printf("! %d", a + b);
            break;
        }
    }
}
C++

#include <iostream>
int main() {
    int resp;
    for(int a=1; a<=9; a++){
        // A가 a인지 물어보고 flush를 한다.
        // endl은 자동으로 flush도 해준다.
        std::cout << "? A " << a << std::endl;

        // 채점기의 답변을 입력받는다.
        std::cin >> resp;

        if(resp == 1){
            // 답변이 "예"이므로 A의 값은 a이다.
            // B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
            int b = 0;
            std::cout << "! " << a + b;
            break;
        }
    }
}
Python

for a in range(1, 10):
    # A가 a인지 물어보고 flush를 한다.
    # print에 flush 파라미터를 넣으면 된다.
    print("? A", a, flush=True)

    # 채점기의 답변을 입력받는다.
    resp = int(input())

    if resp == 1:
        # 답변이 "예"이므로 A의 값은 a이다.
        # B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
        b = 0
        print("!", a + b)
        break
Rust

fn read_i32() -> i32 {
    let mut resp_s = String::new();
    std::io::stdin().read_line(&mut resp_s).unwrap();
    resp_s.trim().parse().unwrap()
}

fn main() {
    for a in 1..=9 {
        // A가 a인지 물어보고 flush를 한다.
        // println!은 자동으로 flush도 해준다.
        println!("? A {a}");

        // 채점기의 답변을 입력받는다.
        let resp = read_i32();

        if resp == 1 {
            // 답변이 "예"이므로 A의 값은 a이다.
            // B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
            let b = 0;
            println!("! {}", a + b);
            break;
        }
    }
}
Java

import java.io.*;
import java.util.*;
 
public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        for(int a=1; a<=9; a++){
            // A가 a인지 물어보고 flush를 한다.
            // System.out.println은 자동으로 flush도 해준다.
            System.out.println("? A " + a);

            // 채점기의 답변을 입력받는다.
            int resp = sc.nextInt();

            if(resp == 1){
                // 답변이 "예"이므로 A의 값은 a이다.
                // B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
                int b = 0;
                System.out.println("! " + (a + b));
                break;
            }
        }
    }
}
표준 출력을 flush해야 하는 이유

콘솔 혹은 파일 입출력은 사칙연산이나 값을 대입하는 등의 기본적인 연산에 비해 상대적으로 느린 작업이다. 따라서 많은 프로그래밍 언어의 기본 출력 기능은 출력을 요청받은 값들을 한 공간에 쌓아두고, 적당한 때에 한꺼번에 출력되도록 한다. 이 공간을 버퍼(buffer)라고 부른다.

그러나 이 문제에서는 채점기가 프로그램의 출력을 실시간으로 확인해야 답변을 줄 수 있다. 따라서 버퍼를 직접 비우는 작업이 필요하고, 이 작업을 flush라고 한다.

예고편

제2편에서는 "적응하는 채점기"와 "적응하지 않는 채점기"의 차이를 다룬다. 제1편에 비해 어렵다는 점을 유의하자.

이 문제의 채점기는 적응하지 않는다.

출처
Contest > BOJ User Contest > BOJ Bundle > BOJ Bundle in Math. Vol 1 H번

문제를 만든 사람: jh05013
문제를 검수한 사람: ibm2006, kaorin, kiwiyou, sorohue, utilforever, wider93
알고리즘 분류

수학
구현
브루트포스 알고리즘 📌
사칙연산 📌
채점 및 기타 정보
예제는 채점하지 않는다.
메모