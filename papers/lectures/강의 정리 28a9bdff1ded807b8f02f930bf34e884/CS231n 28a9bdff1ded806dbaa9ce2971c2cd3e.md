# CS231n

소유자: 주헌 박

# **CS231n (2021) 강의별 요약**

## **Lecture 1: Course Introduction**

**강의 제목:** *Course Introduction. Computer vision overview, Historical context, Course logistics*

**핵심 개념:** 이 강의에서는 컴퓨터 비전의 전체 그림과 역사적 맥락을 소개한다. 컴퓨터 비전은 이미지로부터 의미 있는 정보를 추출하는 분야로, **이미지 분류(image classification)**, **객체 검출(object detection)**, **세그멘테이션(segmentation)** 등의 핵심 과제를 포함한다. 강의는 초창기 비전 연구부터 딥러닝 등장 이전의 기법들까지 역사적 배경을 다루며, 딥러닝의 출현으로 컴퓨터 비전이 급격히 발전한 과정을 설명한다. 또한 2021년 최신 컴퓨터 비전 동향과 **컨볼루션 신경망(CNN)** 등의 중요 개념을 소개하고, 수업 진행 방식과 과제 등에 대한 **수업 운영(코스 로지스틱)** 사항을 안내한다.

**주요 내용 요약:**

- **컴퓨터 비전의 도전 과제:** **시점 변화(viewpoint)**, **크기 변화(scale)**, **변형(deformation)**, **가림(occlusion)**, **조명 변화(illumination)**, **배경 잡음(background clutter)**, **클래스 내 다양성(intra-class variation)** 등으로 인해 동일 객체라도 다양한 모습으로 나타나 컴퓨터가 인식하기 어렵다cs231n.github.iocs231n.github.io. 이러한 다양성 속에서 **클래스 간 차이(inter-class variation)**는 구분되어야 하므로, 강인하면서도 예민한 모델이 필요하다[studocu.com](https://www.studocu.com/en-us/document/stanford-university/convolutional-neural-networks-for-visual-recognition/1-cs231n-convolutional-neural-networks-for-visual-recognition/93095363#:~:text=The%203%20represents%20the%20three,Many%20objects%20of%20interest)[studocu.com](https://www.studocu.com/en-us/document/stanford-university/convolutional-neural-networks-for-visual-recognition/1-cs231n-convolutional-neural-networks-for-visual-recognition/93095363#:~:text=illumination%20are%20drastic%20on%20the,class%20variations).
- **데이터 기반 접근법:** 전통적 프로그래밍으로 “고양이”를 식별하는 규칙을 일일이 정의하기 어렵다. 대신 **데이터 주도 접근(data-driven approach)**으로 많은 레이블된 이미지를 모아 학습 알고리즘이 **각 클래스의 시각적 특징을 학습**하도록 한다cs231n.github.io. 이 과정은 아이에게 시각 개념을 가르치는 방법과 유사하며, 대규모 **훈련 데이터셋(training dataset)** 구축이 필수적이다.
- **이미지 표현과 파이프라인:** 컴퓨터는 이미지를 **픽셀 숫자 행렬**로 표현한다. 예를 들어 RGB 컬러 이미지는 폭 * 높이 * 3채널의 3차원 배열로 나타나며, 픽셀 하나당 0~255값을 갖는다cs231n.github.io. 분류 파이프라인은 (1) **입력**: N장의 이미지와 각 이미지의 레이블로 구성된 훈련 집합, (2) **학습**: 모델 파라미터를 조정해 각 클래스의 특징을 학습, (3) **평가**: 학습된 모델로 보지 못한 새 이미지의 레이블을 예측하고 실제 정답(ground truth)과 비교하는 단계를 거친다cs231n.github.iocs231n.github.io.
- **코스 로지스틱:** 수업은 이론 강의와 실습, 과제로 구성된다. 파이썬/NumPy 튜토리얼과 딥러닝 프레임워크 사용법 (예: PyTorch) 안내가 제공되며, 3개의 프로그래밍 과제를 통해 k-최근접 이웃, SVM, CNN 구현과 실험을 하게 된다. 또한 프로젝트를 수행하여 최종적으로 실제 딥러닝 연구 또는 응용을 경험하도록 설계되어 있다.

**응용 및 참고:** 컴퓨터 비전 기술은 사진 속 인물 식별, 의료 영상 진단, 자율주행 차량의 객체 인식, 공장 자동화 검사 등 다양한 분야에 적용된다. 예를 들어, **이미지 분류** 기술은 방대한 사진 데이터베이스에서 특정 객체를 검색하거나 사진의 내용을 자동 태깅하는 데 활용된다. 강의는 이러한 실세계 응용을 소개함으로써 동기 부여를 제공하며, 추가로 딥러닝 기반 비전의 사회적 영향과 윤리적 고려사항도 개괄한다. (※ *이 강의부터 실제 모델과 알고리즘 구현을 다루므로, 수학적 이해와 프로그래밍 실습을 병행할 것을 권장한다.*)

## **Lecture 2: Image Classification**

**강의 제목:** *Image Classification. The data-driven approach, K-nearest neighbor, Linear classification I*

**핵심 개념:** 이미지 분류 문제를 다루며, 가장 먼저 **최근접 이웃 분류기(k-Nearest Neighbor, kNN)**를 소개한다[studocu.com](https://www.studocu.com/en-us/document/stanford-university/convolutional-neural-networks-for-visual-recognition/1-cs231n-convolutional-neural-networks-for-visual-recognition/93095363#:~:text=As%20our%20%C2%A6rst%20approach%2C%20we,the%20image%20below%20you%20can). 이는 **비매개변수(non-parametric)** 접근으로 새로운 이미지의 클래스를 결정하기 위해 **훈련 세트의 이미지와 일일이 비교**하는 방법이다. 이후 더 나은 대안으로 **선형 분류기(linear classifier)**를 도입한다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=Overview,parameters%20of%20the%20score%20function). 선형 분류기는 입력 이미지의 픽셀을 일렬로 펼친 벡터 x*x*에 가중치 행렬 W*W*와 편향 b*b*를 곱하여 **클래스 점수**를 계산하며, 수식으로 f(x;W,b)=Wx+b*f*(*x*;*W*,*b*)=*Wx*+*b*로 표현된다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=Linear%20classifier,possible%20function%2C%20a%20linear%20mapping). 이 강의에서는 이러한 **점수 함수(score function)**와 **손실 함수(loss function)**의 개념을 정의하고, 이를 기반으로 분류기를 학습시키는 **데이터 주도 학습**의 기초를 다룬다.

**주요 수식 및 알고리즘:**

- **최근접 이웃 (kNN):** 새로운 데이터에 가장 **유사한** k*k*개의 훈련 이미지 레이블을 참조하여 다수결 등으로 클래스를 예측한다. 두 이미지 간 유사도의 한 기준으로 **L1 거리**(절댓값 차이 합) 또는 **L2 거리**(유클리드 거리)가 사용된다 (예: L2(xi,xj)=∑p(xi[p]−xj[p])2*L*2(*xi*,*xj*)=∑*p*(*xi*[*p*]−*xj*[*p*])2). kNN의 단점은 모든 훈련 데이터를 저장해야 하고 예측 시 모든 데이터와 비교하므로 **메모리 비효율** 및 **예측 시간 지연**이 발생한다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=kNN%20has%20a%20number%20of,disadvantages). 실제 CIFAR-10 데이터셋 (10종 객체, 60,000장 이미지)에 kNN을 적용하면 약 30~40% 정확도 수준에 그쳐 딥러닝에 비해 성능이 낮다[studocu.com](https://www.studocu.com/en-us/document/stanford-university/convolutional-neural-networks-for-visual-recognition/1-cs231n-convolutional-neural-networks-for-visual-recognition/93095363#:~:text=label%20the%20remaining%2010%2C000,the%20right%20you%20can%20see)[studocu.com](https://www.studocu.com/en-us/document/stanford-university/convolutional-neural-networks-for-visual-recognition/1-cs231n-convolutional-neural-networks-for-visual-recognition/93095363#:~:text=be%20mislabeled%20as%20a%20car,if%20the%20images%20are%20very).
- **선형 분류기:** 모든 데이터를 저장하는 대신 **매개변수 W,b*W*,*b*만 학습**하는 **모델 기반(parametric)** 접근이다. 각 클래스별로 가중치 행 벡터가 존재하며, 이미지의 픽셀 벡터 x*x*와 내적(dot product)을 통해 해당 클래스의 점수를 산출한다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=Linear%20classifier,possible%20function%2C%20a%20linear%20mapping). 이렇게 얻은 **점수 벡터** s=Wx+b*s*=*Wx*+*b*에서 가장 높은 점수를 가진 클래스가 예측 결과가 된다. 선형 분류의 장점은 학습 후에는 W,b*W*,*b*만 유지하면 되므로 **공간 효율성**이 높고, 예측도 단순 행렬곱으로 **속도가 빠르다**[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=,the%20scores%20of%20incorrect%20classes)[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=image%20can%20be%20simply%20forwarded,image%20to%20all%20training%20images).
- **손실 함수:** 모델이 훈련 데이터를 얼마나 잘 분류하는지 측정하는 함수다. 강의에서는 두 가지 대표 손실을 다룬다. (1) **서포트 벡터 머신(SVM)**의 **멀티클래스 힌지 손실**: 정답 클래스 점수가 다른 클래스 점수보다 ΔΔ만큼 크도록 유도하며, 이를 위반할 경우 선형적으로 패널티를 부과한다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=Let%E2%80%99s%20now%20get%20more%20precise,is%20then%20formalized%20as%20follows). 하나의 데이터 i*i*에 대한 SVM 손실 식은 Li=∑j≠yimax⁡(0,sj−syi+Δ)*Li*=∑*j*=*yi*max(0,*sj*−*syi*+Δ)로 정의된다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=scores%29,is%20then%20formalized%20as%20follows)[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=%5C%5BL_i%20%3D%20%5Cmax%280%2C%20,13%20%2B%2010). 직관적으로, 정답 점수 syi*syi*가 다른 어떤 클래스 점수 sj*sj*보다 ΔΔ 이상 작으면 그만큼 손실이 발생한다. (2) **소프트맥스(Softmax)** **교차 엔트로피 손실**: 점수를 정규화하여 각 클래스에 대한 **확률 분포**로 해석하고, 정답 클래스 확률을 높이는 방향으로 학습한다. 하나의 데이터에 대한 손실은 Li=−log⁡esyi∑jesj*Li*=−log∑*jesjesyi*로 표현되며[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=the%20hinge%20loss%20with%20a,loss%20that%20has%20the%20form), 이는 **정답 클래스의 예측 확률의 음의 로그**값이다. 소프트맥스는 SVM과 달리 모든 클래스 점수 차이에 민감하게 반응하며, 정답 클래스의 확률이 1에 가까워질수록 손실이 0에 수렴한다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=%5C%5BL_i%20%3D%20,f_%7By_i%7D%20%2B%20%5Clog%5Csum_j%20e%5E%7Bf_j)[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=The%20Softmax%20classifier%20is%20hence,In%20other). 두 손실 모두 **정규화 항(reguralization)** R(W)*R*(*W*)를 추가해 가중치 크기를 억제함으로써 오버피팅을 방지할 수 있으며, 최종 최적화 목적은 1N∑iLi+λR(W)*N*1∑*iLi*+*λR*(*W*)의 최소화이다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=In%20other%20words%2C%20we%20wish,quadratic%20penalty%20over%20all%20parameters)[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=Notice%20that%20the%20regularization%20function,full%20Multiclass%20SVM%20loss%20becomes).

**응용 사례:** 이 강의의 개념들은 간단한 분류기 구현에 바로 적용된다. 예컨대 **CIFAR-10** 데이터셋을 대상으로 kNN과 선형 SVM/Softmax 분류기를 직접 코딩하고 성능을 비교해보는 실습을 진행한다. 이를 통해 **하이퍼파라미터 튜닝**(예: k값, ΔΔ, 정규화 세기 등)의 영향도 경험하게 된다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=match%20at%20L345%20full%20Multiclass,full%20Multiclass%20SVM%20loss%20becomes). 또한 kNN 대비 선형 분류기가 대규모 데이터에서 어떻게 효율적이고 성능 향상을 가져오는지 체감할 수 있다. 정리하면, 이미지 분류의 기본 해결책으로서 *“특징 표현 + 학습 가능한 매개변수 + 손실함수 최적화”*의 틀을 제시하고, 이는 이후 다루게 될 복잡한 신경망의 기반이 된다.

## **Lecture 3: Loss Functions and Optimization**

**강의 제목:** *Loss Functions and Optimization. Linear classification II, Higher-level representations, Image features, Optimization, Stochastic gradient descent*

**핵심 개념:** 본 강의에서는 이전 강의의 선형 분류기를 심화하여, **손실 함수 최적화**를 통한 모델 학습 원리를 다룬다. 먼저 이미지의 **고차원 표현(higher-level representation)**에 대해 언급하며, 픽셀 자체보다는 특징 추출(feature extraction)을 통해 분류 성능을 높일 수 있음을 설명한다. 그러나 End-to-End 딥러닝에서는 **학습이 특징 추출까지 포함**되므로, 여기서는 주로 **매개변수 학습** 메커니즘에 집중한다. 핵심은 **최적화(optimization)**로, 손실 함수를 최소화하는 W,b*W*,*b* 파라미터를 찾는 과정이다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=We%20saw%20that%20a%20setting,that%20minimize%20the%20loss%20function). 이를 위해 **경사 하강법(gradient descent)**과 그 변형들을 소개하고, 특히 **확률적 경사 하강법(SGD)**이 대규모 데이터 학습에 효율적임을 강조한다.

**주요 개념 및 수식:**

- **손실 함수 복습:** SVM과 Softmax 손실의 형태와 차이를 비교한다. SVM은 **마진 기반(max-margin)** 접근으로 어느 정도 여유(ΔΔ)를 두고 정답 점수가 높길 바라며, Softmax는 **확률적 접근**으로 정답 확률 자체를 최대화한다[cs231n.github.io](https://cs231n.github.io/linear-classify/#:~:text=classifier%20uses%20the%20cross,doesn%E2%80%99t%20make%20sense%20to%20talk). 두 손실 모두 최소화해야 할 **스칼라 비용**을 산출하므로, 이제 이 비용에 대해 최적화 기법을 적용할 수 있다.
- **최적화 문제:** 선형 분류기의 전체 손실 L(W)*L*(*W*)는 가중치 W*W*에 대한 **비凸(convex)** 함수 (정규화 없이는 부분적으로 볼록)이다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=We%20can%20explain%20the%20piecewise,a%20single%20example%20we%20have). 작은 예에서는 손실을 그래프로 시각화해 보면 다차원 곡면(bowl)을 이루고, 최솟값에서 0에 가까운 손실을 갖는다. 최적화를 통해 이 **“곡면의 최저점”**을 찾는 것이 학습이다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=Visualizing%20the%20loss%20function)[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=evaluating%20the%20loss%20,be%20visualized%20with%20a%20color).
- **경사(Gradient):** 함수의 기울기 벡터 ∇WL∇*WL*는 파라미터를 얼마나 조정해야 손실이 가장 크게 줄어드는지 방향을 알려준다. 이론적으로 **기울기가 0**인 지점이 극솟값이므로, 경사 하강법은 ∇WL∇*WL*을 0으로 만드는 W*W*를 찾아가는 과정으로 볼 수 있다[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=Problem%20statement,)[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=If%20you%20are%20coming%20to,help%20you%20throughout%20the%20class). 미분 계산에는 **연쇄 법칙(chain rule)**을 활용하며, 복잡한 네트워크에서도 **역전파(backpropagation)** 알고리즘으로 기울기를 효율적으로 구할 수 있음을 예고한다 (다음 Lecture 4에서 상세히 다룸).
- **수치적 vs 해석적 기울기:** 기울기는 **유한 차분(finite difference)**으로 근사 계산할 수도 있고, **미분 공식을 통한 해석적 계산**도 가능하다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=,of%20computing%20it%20numerically%20using)[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=,a%20parameter%20update%20in%20loop). 수치적 방법은 구현은 쉬우나 오차가 있고 느리다. 해석적 방법(역전파)은 정확하고 빠르지만 구현 시 실수가 있을 수 있다. 따라서 **Gradient Checking**으로 둘을 교차 검증하는 것이 실무에서 중요하다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=,a%20gradient%20check%2C%20in%20which).
- **경사 하강법 (GD):** 가장 기본적인 최적화 알고리즘으로, 반복(iteration)마다 W:=W−η∇WL*W*:=*W*−*η*∇*WL*로 갱신한다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=)[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=while%20True%3A%20weights_grad%20%3D%20evaluate_gradient,perform%20parameter%20update). 여기서 스텝 크기 η*η*는 **학습률(learning rate)**로, 너무 작으면 수렴이 느리고 너무 크면 발산하거나 최솟값 주변에서 진동한다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=optimization%20landscape%20in%20which%20we,of%20computing%20it%20numerically%20using). GD의 계산은 **전체 데이터셋의 손실을 매번 정확히 계산**해야 하므로 매우 느릴 수 있다.
- **확률적 경사 하강법 (SGD):** 대용량 데이터에 GD를 직접 적용하면 비효율적이므로, **미니배치(mini-batch)** 단위로 손실과 경사를 추정하여 업데이트하는 SGD를 사용한다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=Mini,to%20perform%20a%20parameter%20update)[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=while%20True%3A%20data_batch%20%3D%20sample_training_data,perform%20parameter%20update). 예컨대 100만 샘플 중 256개씩 배치로 가져와 경사를 계산하고 가중치를 갱신하는 방식이다. 이렇게 하면 각 업데이트가 **약간의 노이즈**가 섞인 경사로 이루어지지만, **계산 비용을 크게 줄여** 더 자주 업데이트할 수 있어 결과적으로 빠르게 수렴한다[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=small%20subset%20of%201000,perform%20more%20frequent%20parameter%20updates)[cs231n.github.io](https://cs231n.github.io/optimization-1/#:~:text=to%20using%20a%20single%20example,sized%20in%20powers%20of%202). 실제로도 “SGD”라고 부를 때 대부분 미니배치 SGD를 의미한다.
- **랜덤 초기화 및 필요성:** 최적화 전에 가중치 W*W*는 보통 작은 난수로 초기화한다. 만약 0으로 초기화하면 모든 출력이 대칭적으로 같아지고 경사도 동일해져, 여러 뉴런이 같은 값만 학습하는 **대칭 깨짐 문제**가 발생한다[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Pitfall%3A%20all%20zero%20initialization,In%20other%20words)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Small%20random%20numbers,initialized%20as%20a%20random%20vector). 난수 초기화(예: 0.01×N(0,1)0.01×N(0,1)로 샘플링)는 이러한 대칭을 깨고 각 뉴런이 다른 경로로 학습되도록 해준다[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Small%20random%20numbers,initialized%20as%20a%20random%20vector)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=unique%20in%20the%20beginning%2C%20so,the%20final%20performance%20in%20practice).

**학습 팁 및 최적화 트릭:** 본 강의에서는 최적화 시 고려해야 할 실용적인 이슈도 논한다. 예를 들어, **학습률 설정**은 경험적으로 중요한데, 보통 1e-3 정도에서 시작해 관찰하며 조정한다. 또한 학습률을 학습 중 점차 줄여주는 **러닝레이트 스케줄링**이나, 경사 업데이트에 **모멘텀(momentum)**을 추가하여 진동을 줄이고 가속하는 방법도 소개될 수 있다 (Momentum SGD: v:=αv+η∇WL;W:=W−v*v*:=*αv*+*η*∇*WL*;*W*:=*W*−*v* 형태). 이러한 고급 최적화 기법들은 Lecture 7~8에서 더 자세히 다룰 예정이다. 이번 강의를 통해 학생들은 손실 함수를 최소화하는 것이 곧 **모델의 예측 성능을 높이는 방향**임을 이해하고, 경사 기반 학습의 원리를 습득하게 된다.

## **Lecture 4: Neural Networks and Backpropagation**

**강의 제목:** *Neural Networks and Backpropagation. Backpropagation, Multi-layer Perceptrons, The neural viewpoint*

**핵심 개념:** 이번 강의에서는 선형 분류기를 다층으로 확장한 **인공 신경망(Artificial Neural Network)**의 구조와 학습 원리를 다룬다. **다층 퍼셉트론(Multi-Layer Perceptron, MLP)**은 입력층과 출력층 사이에 하나 이상의 **은닉층(hidden layer)**을 추가한 모델로, 각 층이 이전 층의 선형 조합을 비선형 함수에 통과시켜 표현력을 향상시킨다. 주된 내용은 신경망의 **순전파(forward pass)**와 **역전파(backpropagation)** 알고리즘이다. 역전파는 연쇄 법칙을 사용하여 출력부터 입력 방향으로 **그래디언트(gradient)**를 효율적으로 전파함으로써, 모든 가중치에 대한 손실의 기울기를 계산하는 방법이다[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=Motivation,design%20and%20debug%20neural%20networks)[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=Learning,Neural%20Network%20might%20be%20doing).

**핵심 내용 및 수식:**

- **순전파와 비선형성:** 한 개의 은닉층을 가진 신경망은 수식으로 s=W2 f(W1x+b1)+b2*s*=*W*2*f*(*W*1*x*+*b*1)+*b*2로 표현된다cs231n.github.io. 여기서 f(⋅)*f*(⋅)는 **비선형 활성화 함수(activation function)**로서, 선형 모델들을 직렬로 쌓았을 때 발생하는 **표현력 한계**를 극복해준다cs231n.github.io. 대표적인 활성화 함수로는 **시그모이드(sigmoid)** σ(x)=11+e−x*σ*(*x*)=1+*e*−*x*1cs231n.github.io, **하이퍼볼릭탄젠트(tanh)** tanh⁡(x)=2σ(2x)−1tanh(*x*)=2*σ*(2*x*)−1cs231n.github.io, 그리고 오늘날 가장 널리 쓰이는 **ReLU** ReLU(x)=max⁡(0,x)ReLU(*x*)=max(0,*x*)cs231n.github.io가 있다. 시그모이드와 tanh는 출력이 포화되면 그래디언트가 거의 0이 되어 **“그래디언트 소실(vanishing gradient)”** 문제가 있었고, ReLU는 이 문제를 완화하여 학습을 가속하지만 음수 입력에서 뉴런이 죽을 수 있는 단점이 있다 (dying ReLU 문제)cs231n.github.iocs231n.github.io.
- **다층 퍼셉트론의 표현력:** 은닉층의 뉴런 수와 층 깊이를 늘리면 이론적으로 어떤 복잡한 함수도 근사할 수 있는 **보편 근사 정리(universal approximation theorem)**가 성립한다. 따라서 MLP는 선형 분류기보다 훨씬 복잡한 결정 경계(decision boundary)를 학습할 수 있다. 예를 들어, 은닉층 뉴런이 100개인 3층 신경망은 x*x* (3072차원 CIFAR-10 이미지)의 선형 변환 -> ReLU -> 선형 변환 -> ReLU -> 선형 변환을 거쳐 10차원 점수를 출력하며, 각 층이 데이터의 점진적인 **추상화된 특징**을 학습한다cs231n.github.iocs231n.github.io.
- **역전파 알고리즘:** 출력 손실 L*L*을 각 파라미터에 대해 미분하려면 연쇄법칙을 반복 적용해야 하는데, 역전파는 이를 **계층별로 계산 그래프를 따라 자동화**한 알고리즘이다. 간단한 예로 두 층 신경망의 손실 기울기는 출력층에서 ∂L∂W2,∂L∂b2∂*W*2∂*L*,∂*b*2∂*L*를 계산한 뒤, 은닉층으로 ∂L∂h=∂L∂s∂s∂h∂*h*∂*L*=∂*s*∂*L*∂*h*∂*s*를 전파하고, 이어 ∂L∂W1,∂L∂b1∂*W*1∂*L*,∂*b*1∂*L*를 구하는 식이다. 역전파의 핵심은 **중간 미분 결과를 재사용**하여 계산량을 줄이는 데 있다. 수식적으로, 예컨대 두 변수 곱 f(x,y)=x⋅y*f*(*x*,*y*)=*x*⋅*y*의 편미분은 ∂f∂x=y,∂f∂y=x∂*x*∂*f*=*y*,∂*y*∂*f*=*x*인데[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=Lets%20start%20simple%20so%20that,partial%20derivative%20for%20either%20input), 더 복잡한 조합에서도 기본 연산(+, *, max 등)의 미분 규칙을 사용해 차근차근 쪼개어 계산한다. *실제로 역전파는 각 뉴런의 출력이 손실에 미치는 영향을 구하는 과정으로, 이를 신경망 *“오차의 역전달”*이라고도 한다.*
- **계산 그래프 관점:** 신경망 연산을 노드와 엣지로 이루어진 그래프로 볼 수 있으며, 순전파는 노드들을 따라 함수 평가를, 역전파는 동일한 그래프를 **역순으로 따라 미분**을 전파한다[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=Motivation,design%20and%20debug%20neural%20networks)[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=Motivation,in). 이 모듈화 덕분에 복잡한 네트워크도 각 구성요소(선형 곱셈, 활성화 함수 등)의 미분만 구현하면 전체 그래디언트를 자동으로 구할 수 있다. 예를 들어 ReLU 노드 r=max⁡(0,z)*r*=max(0,*z*)는 입력 z*z*가 양수면 ∂r∂z=1∂*z*∂*r*=1, 음수면 0을 갖고, 이 값을 곱하여 이전 노드로 그래디언트를 보낸다[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=that%20is%2C%20the%20derivative%20on,class%20is%20the%20max%20operation). 이러한 방식으로, 딥러닝 프레임워크들은 순전파 연산을 정의하면 자동으로 역전파를 수행해준다.
- **백프로퍼게이션 구현 예:** 강의에서는 간단한 네트워크의 역전파 계산을 수기로 해보는 연습을 할 수 있다. 예컨대 입력 x*x* 두 개와 파라미터 w1,w2,b*w*1,*w*2,*b*로 구성된 출력 o=σ(w1x1+w2x2+b)*o*=*σ*(*w*1*x*1+*w*2*x*2+*b*) (시그모이드 출력)에 대해 각 변수의 기울기를 풀어쓰는 식이다. 이때 ∂L∂w1=(σ′(u)⋅∂L∂o)⋅x1∂*w*1∂*L*=(*σ*′(*u*)⋅∂*o*∂*L*)⋅*x*1 (여기서 u=w1x1+w2x2+b*u*=*w*1*x*1+*w*2*x*2+*b*)와 같이 단계별로 미분을 전파함을 확인할 수 있다. 이런 유도 과정을 통해 학생들은 역전파의 논리를 이해하고, 나아가 딥러닝 라이브러리가 내부적으로 수행하는 작업을 깊이 있게 파악하게 된다.

**응용 사례:** 역전파 알고리즘은 딥러닝 모델 훈련의 엔진으로서, 현대 프레임워크 (PyTorch, TensorFlow 등)에서는 **자동 미분(autograd)** 형태로 구현되어 있다. 이번 강의의 이해를 바탕으로, Assignment에서 학생들은 2층 신경망을 Numpy로 직접 구현하여 forward와 backward 함수를 완성하고, MNIST 같은 데이터에 학습시켜 볼 수 있다. 또한 역전파 이해는 **네트워크 구조 설계**나 **새로운 연산 정의** 시 필수적이다. 예를 들어 **커스텀 손실 함수**나 **비표준 층**을 만들 때 수식을 유도하여 역전파를 구현할 수 있어야 한다. 강의는 Colah’s blog 등의 시각적 자료를 참고하여 역전파를 직관적으로 설명하고[cs231n.github.io](https://cs231n.github.io/optimization-2/#:~:text=,Summary), Yann LeCun의 “Efficient BackProp” 논문을 추가자료로 제시하여 최적화 관점에서의 역전파 팁도 다룬다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=,2).

## **Lecture 5: Convolutional Neural Networks**

**강의 제목:** *Convolutional Neural Networks. History, Convolution and pooling, ConvNets outside vision*

**핵심 개념:** 합성곱 신경망(CNN)은 이미지 처리에 특화된 신경망 구조로, 2D 이미지의 **공간적 구조(spatial structure)**를 활용하여 효율적으로 학습한다cs231n.github.iocs231n.github.io. CNN 등장은 딥러닝의 비전 혁명을 이끌었으며, 역사적으로 LeNet(1990s)과 AlexNet(2012)의 성공으로 주목받았다. 이 강의에서는 **합성곱 계층(convolutional layer)**과 **풀링 계층(pooling layer)**의 동작 원리를 다루고, 전통적인 완전연결 네트워크와 비교하여 **파라미터 공유(parameter sharing)**와 **국소 수용영역(receptive field)** 개념을 소개한다. 또한 CNN이 이미지 외에 음성, 자연어 등 다른 분야에도 응용됨을 간략히 언급한다.

합성곱 신경망의 계층들은 입력을 가로, 세로, 깊이의 3차원 볼륨으로 취급한다cs231n.github.io. 위 그림의 오른쪽은 합성곱 계층이 **너비(width)**와 **높이(height)** 방향으로는 국소 영역만 연결하고, **깊이(depth)** 방향으로는 전체 채널(예: RGB)을 연결하는 구조를 보여준다cs231n.github.io. 이러한 구성으로 **공간적 인접성**을 활용하여 특징을 추출하며, 파라미터(필터)가 이미지 내 여러 위치에서 반복 사용되므로 학습할 매개변수 수가 크게 줄어든다cs231n.github.iocs231n.github.io.

**주요 내용 및 수식:**

- **합성곱 연산:** 합성곱 계층은 학습된 **필터(filter)**를 이미지 전역에 **슬라이딩**하며 **점곱(dot product)**을 계산한다cs231n.github.iocs231n.github.io. 예를 들어 첫 합성곱 계층에서 5x5x3 크기의 필터 1개를 사용하면, 필터를 이미지의 각 5x5 위치에 곱씌워 합산한 한 개의 출력 값이 얻어진다. 필터를 전체 위치로 이동시키면 동일 연산이 반복되어 2D **활성맵(feature map)**이 만들어진다. 여러 개의 필터를 사용하면 깊이 방향으로 활성맵이 쌓여 출력 볼륨을 형성한다. 필터 k*k*에 대한 출력 픽셀 yi,j,k*yi*,*j*,*k*는 수식으로
    
    yi,j,k=∑c=1C∑u=1Hf∑v=1WfWc,u,v(k)⋅xc, i+u−1, j+v−1+bk*yi*,*j*,*k*=∑*c*=1*C*∑*u*=1*Hf*∑*v*=1*WfWc*,*u*,*v*(*k*)⋅*xc*,*i*+*u*−1,*j*+*v*−1+*bk*
    
    와 같이 계산된다. 여기서 W(k)*W*(*k*)는 필터의 가중치, bk*bk*는 필터의 편향, C*C*는 입력 깊이(채널 수), Hf,Wf*Hf*,*Wf*는 필터 높이와 너비이다. 이 연산이 이미지의 각 위치 (i,j)(*i*,*j*)에서 수행되어 하나의 필터에 대해 전체 활성맵이 산출된다.
    
- **패딩(padding)과 스트라이드(stride):** 출력 크기는 필터 크기와 이동 간격에 영향을 받는다. 입력 크기를 N×N*N*×*N*, 필터 크기를 F×F*F*×*F*, 스트라이드를 S*S*, 패딩을 P*P*라 할 때 출력 크기는 ⌊N−F+2PS⌋+1⌊*SN*−*F*+2*P*⌋+1이 된다. 예를 들어 N=32,F=5,S=1,P=2*N*=32,*F*=5,*S*=1,*P*=2로 하면 출력이 32×3232×32로 입력 크기를 유지한다 (**세임 패딩**). 패딩은 입력 주변을 0으로 둘러 활성맵 크기를 조정하고 가장자리 정보 손실을 줄이며, 스트라이드는 필터 적용 간격을 키워 출력 크기를 줄인다.
- **풀링(pooling):** 풀링 계층은 인접한 출력들을 다운샘플링하여 특성 맵의 공간 크기를 줄인다. 일반적으로 **최대 풀링(max pooling)**이 사용되며, 예컨대 2×22×2 영역에 스트라이드 2로 적용하면 출력 크기가 절반으로 감소한다. 풀링은 **학습 파라미터가 없고** 고정 연산으로서, 약간의 **불변성(invariance)**을 준다 (작은 위치 변화에 크게 영향을 받지 않도록)cs231n.github.io. 단, 최근에는 풀링 대신 스트라이드 합성곱으로 대체하는 경향도 있으며, **평균 풀링(average pooling)**은 주로 GoogleNet의 Inception 등에서 사용된다.
- **CNN의 장점:** 완전연결층과 달리, 합성곱층은 **국소 연결**과 **파라미터 공유**로 이미지 같은 고차원 입력에 효과적이다. 완전연결층에서 첫 층 가중치가 3072×1003072×100 (CIFAR-10 예시)였다면, 5×55×5 크기 필터 16개를 가진 합성곱층의 파라미터는 5⋅5⋅3⋅16≈12005⋅5⋅3⋅16≈1200개로 크게 줄어든다cs231n.github.iocs231n.github.io. 또한 **계층적 특징 학습**이 가능해, 처음 합성곱층은 에지 같은 **저수준 특징**을, 깊어질수록 물체의 일부 같은 **고수준 특징**을 감지하게 된다.
- **CNN 아키텍처의 구성:** 일반적인 CNN은 **[CONV - ReLU - POOL]** 블록을 여러 번 거친 후 **[FC - Softmax]**로 분류 점수를 출력한다cs231n.github.iocs231n.github.io. 예를 들어 CIFAR-10에 대해 **`[INPUT 32x32x3] -> [CONV+ReLU (출력 32x32x16)] -> [POOL (출력 16x16x16)] -> [CONV+ReLU (출력 16x16x32)] -> [POOL (8x8x32)] -> [FC -> 10 scores]`** 같은 구조를 생각할 수 있다. 최근에는 VGG, ResNet 같은 복잡한 구조들이 제안되었지만, 기본 원리는 이러한 층의 조합으로 이루어진다cs231n.github.iocs231n.github.io.

**역사 및 응용:** CNN의 역사는 **LeCun의 LeNet-5** (1998, 우편번호 인식)에 뿌리를 두며, 2012년 **AlexNet**이 Imagenet 대회에서 압승하면서 현대 딥러닝 붐을 일으켰다. 이후 **VGGNet**(2014)은 심층화의 중요성을 보였고, **GoogLeNet(Inception)**(2014)은 풀링 대신 병렬 구조(Inception module)로 효율을 추구했으며, **ResNet**(2015)은 **잔차 연결(skip connection)**로 100+ 층 학습을 가능케 했다. 이러한 구조들은 Lecture 9에서 자세히 다룬다. CNN은 **컴퓨터 비전 외 분야**에도 활용되어, 음성 인식에서는 1D 합성곱으로 스펙트럼 특징을 잡거나, NLP에서는 텍스트의 n-그램 패턴을 인식하는 등 폭넓게 쓰이고 있다. 특히 시계열 데이터나 여러 신호 처리에 합성곱 개념이 응용되고 있으며, **DeepMind의 AlphaGo**도 관찰된 보드 상태를 CNN으로 처리했다. CNN은 현재 자율주행(객체 탐지), 의료영상(암 검출), 안면인식, 필기체 인식 등 다양한 응용의 기본 모델로 자리잡고 있다cs231n.github.iocs231n.github.io.

## **Lecture 6: Deep Learning Hardware and Software**

**강의 제목:** *Deep Learning Hardware and Software. CPUs, GPUs, TPUs, PyTorch, TensorFlow, Dynamic vs Static computation graphs*

**핵심 개념:** 딥러닝의 실용적인 측면으로, **학습에 사용되는 하드웨어**와 **딥러닝 프레임워크**에 대한 강의다. 딥러닝 모델 학습은 매우 높은 연산량을 요구하므로, **병렬 계산**에 특화된 하드웨어인 **GPU(Graphics Processing Unit)**의 역할이 중요하다. 또한 Google의 **TPU(Tensor Processing Unit)**와 같은 AI 가속기도 소개된다. 소프트웨어 측면에서는 현대 딥러닝을 쉽게 구현하게 해주는 **프레임워크**들 – 예컨대 **TensorFlow**, **PyTorch** – 의 특징과 **계산 그래프(computation graph)** 개념을 다룬다. 특히 PyTorch의 **동적 그래프(dynamic graph)**와 TensorFlow의 **정적 그래프(static graph)** 모델 간 차이를 설명하여, 연구 실험과 제품 배포 각각에 장단점이 있음을 짚는다.

**주요 내용:**

- **CPU vs GPU:** CPU는 소수의 코어로 **순차 연산**에 최적화된 반면, GPU는 수천 개의 코어로 **동시 다발 연산**에 강하다. 딥러닝 학습의 핵심 연산인 대규모 **행렬 곱셈**이나 **벡터 연산**은 GPU에서 병렬화하여 수행하면 훨씬 빠르다. 예를 들어 1000×10001000×1000 행렬 곱셈도 GPU 메모리에 모두 올려 놓고 CUDA 커널 하나로 병렬 곱셈을 수행할 수 있다. 또한 GPU의 메모리 대역폭이 높아 대량의 데이터를 빠르게 처리 가능하다. 단, CPU 대비 싱글 스레드 성능은 낮으므로 작은 연산에서는 오버헤드가 발생할 수 있다.
- **TPU 등 전용 가속기:** TPU는 Google이 딥러닝 계산 (특히 행렬 곱과 정수 연산)을 가속하기 위해 만든 ASIC 칩으로, TensorFlow 연산을 효율적으로 실행한다. TPU는 더욱 대규모 병렬 연산과 저전력으로 구글의 AI 서비스들을 뒷받침하며, 클라우드 플랫폼으로도 제공되어 연구자들이 대용량 모델을 학습하는데 쓰인다. 이와 유사하게, FPGA 등을 활용한 맞춤형 딥러닝 가속에 대한 연구들도 존재한다.
- **딥러닝 프레임워크:** **TensorFlow**는 Google Brain이 개발한 프레임워크로, **정적 계산 그래프** 방식을 채택하여 학습 과정을 그래프로 정의하고 이를 컴파일/최적화하여 효율적으로 실행한다. 장점은 모델을 정의한 뒤 그래프를 최적화하거나 분산학습에 투입하기 좋다는 것[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=This%20framework%20looks%20at%20AI,study%20and%20forecast%20what%E2%80%99s%20coming)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=,jobs%E2%80%94in%20the%20center%20of%20consideration). 반면 **PyTorch**는 Facebook AI Research가 개발한 프레임워크로, **동적 계산 그래프**(Define-by-Run) 방식을 따른다. 즉 실행 시점에 그래프가 생성되며, **파이썬처럼 직관적인 프로그래밍**이 가능하여 연구 실험에 용이하다. PyTorch는 eager execution 방식이라 디버깅이 쉽고 유연성이 높아 새로운 아이디어 구현에 유리하지만, 그래프 최적화나 배포 시 약간의 비효율이 있을 수 있다.
- **동적 vs 정적 그래프:** 정적 그래프 (예: TensorFlow 1.x)에서는 **`sess.run()`** 등을 통해 한번 정의된 그래프를 여러 번 실행하며, 모델 구조가 고정된다. 반면 동적 그래프 (예: PyTorch, TensorFlow 2.x의 eager mode)에서는 매 iteration마다 계산 흐름이 실행되며, **`if`**문이나 변수 길이 변화 등 **유연한 연산 흐름**을 지원한다. 따라서 순환신경망(RNN) 등에서 매 time-step마다 조건이 달라지는 경우 동적 그래프가 편리하다. 최근에는 TensorFlow도 eager 모드를 기본으로 전환하고, PyTorch도 JIT 컴파일 등으로 정적 그래프 최적화 기능을 도입하여 두 접근이 수렴하는 추세다.
- **프레임워크 사용법:** 본 강의에서는 간단한 예제로 PyTorch에서 Tensor 연산 및 오토그래드 활용, TensorFlow에서 placeholder와 session 개념 등을 시演한다. 예컨대 PyTorch로 2층 신경망을 구축하는 코드는 numpy와 유사한 연산으로 순전파를 수행하고, **`loss.backward()`** 호출로 자동으로 역전파가 실행되어 각 파라미터의 gradient가 **`param.grad`**에 채워지는 식임을 보여준다. TensorFlow의 경우 placeholder를 정의하고 **`feed_dict`**로 데이터를 주입하여 sess.run으로 연산하는 식의 그래프 실행 모델을 소개한다 (다만 2021년 시점에서는 TF2의 eager execution이 활성화되었음을 언급).

**응용 및 팁:** 실제 딥러닝 실험을 수행할 때 하드웨어 선택과 코드 구현 최적화는 성능에 큰 영향을 준다. 예를 들어, **배치 크기(batch size)**를 늘리면 GPU 활용도가 높아져도 메모리 한계에 걸릴 수 있고, 너무 작으면 연산 효율이 떨어진다. 또한 분산 학습(distributed training)을 위해 여러 GPU/TPU를 사용하는 전략 (데이터 병렬 또는 모델 병렬)도 개략적으로 언급된다. 강의에서는 Google Colab이나 AWS EC2처럼 GPU 인스턴스를 사용할 수 있는 환경도 소개하고, 학생들이 과제나 프로젝트에서 GPU를 활용하는 방법을 안내한다. 마지막으로 딥러닝 **소프트웨어 에코시스템**으로서 CuDNN, NCCL 등의 라이브러리와, ONNX 같은 모델 교환 표준에 대해서도 간략히 소개하여, 딥러닝 개발에 필요한 전반적인 도구 체인을 이해시킨다.

## **Lecture 7: Training Neural Networks, Part I**

**강의 제목:** *Training Neural Networks, part I. Activation functions, data processing, Batch Normalization, Transfer learning*

**핵심 개념:** 딥러닝 모델을 효과적으로 학습시키기 위한 다양한 **기법과 전략**을 다루는 첫 번째 강의이다. 여기서는 신경망 학습의 **실용적인 테크닉**으로, (1) 다양한 **활성화 함수(activation function)**의 선택과 특성, (2) **데이터 전처리(data preprocessing)**와 **정규화(normalization)**의 중요성, (3) 학습을 안정화하고 가속하는 **배치 정규화(Batch Normalization)**, (4) 부족한 데이터나 연산 자원이 있을 때 유용한 **전이 학습(transfer learning)** 등을 소개한다. 이 강의를 통해 단순한 SGD로는 부족한 **학습 트릭**들을 배우게 된다.

**주요 내용:**

- **활성화 함수 선택:** 시그모이드, tanh, ReLU 외에도 **Leaky ReLU**(음수 영역 기울기를 약간 양수로 둠)cs231n.github.io, **PReLU**(Leaky 기울기를 학습)cs231n.github.io, **Maxout**(두 선형 함수 중 큰 값 선택)cs231n.github.io 등이 소개된다. 일반적으로 **ReLU**가 기본값처럼 쓰이며, 음수 출력이 많은 경우 Leaky ReLU로 개선하거나, 매우 깊은 네트워크에서는 **Swish**나 **GELU** 등의 최신 함수가 쓰일 수도 있다. 중요한 것은 **활성화 함수가 학습과정 및 결과에 큰 영향**을 주며, 특히 시그모이드나 tanh는 잘못 사용하면 그래디언트 소실로 학습이 어려울 수 있다는 점이다cs231n.github.iocs231n.github.io. 강의에서는 “ReLU를 기본으로, 문제에 따라 다른 함수도 고려”하는 실무 관행을 전한다.
- **데이터 전처리:** 입력 데이터는 **0-mean, 1-std**로 정규화(z-score 정규화)하는 것이 표준이다[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Common%20pitfall,train%2Fval%2Ftest)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Weight%20Initialization). 또한 각 feature를 동일한 스케일로 맞추면 학습이 수월해진다. 이미지의 경우, 픽셀값을 0~255에서 0~1로 스케일링하거나 평균을 뺀 뒤 표준편차로 나누는 작업이 필요하다. **PCA/화이트닝** 등의 기법도 언급되는데, 이는 입력 feature 간 상관관계를 줄이고 모든 방향의 분산을 균일하게 만드는 변환이다[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=The%20last%20transformation%20you%20may,step%20would%20take%20the%20form)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=transformation%20is%20that%20if%20the,step%20would%20take%20the%20form). 다만, 현대 CNN에서는 처음 합성곱층이 이러한 역할을 어느 정도 대체하므로, 일반적으로는 단순 정규화 정도면 충분하다.
- **배치 정규화 (BatchNorm):** **Ioffe & Szegedy (2015)**의 기법으로, 신경망 각 층의 활성 값 분포를 정규화하여 학습을 빠르고 안정적으로 만드는 방법이다[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Batch%20Normalization,here%20because%20it%20is%20well)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=practice%20to%20use%20Batch%20Normalization,Neat). 구체적으로, 미니배치 단위로 각 활성 채널의 평균 μB*μB*와 분산 σB2*σB*2를 계산하고,
    
    h^i=hi−μBσB2+ϵ*h*^*i*=*σB*2+*ϵhi*−*μB*
    
    로 정규화한 뒤 스케일 및 시프트 파라미터 γ,β*γ*,*β*를 적용하여 yi=γh^i+β*yi*=*γh*^*i*+*β*로 출력한다. 이렇게 하면 각 층 입력 분포가 **N(0,1)**로 정규화되어 **층 간 입력 분포 변화(Internal Covariate Shift)**를 줄이고, 더 큰 학습률을 사용해도 학습이 안정된다[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Batch%20Normalization,has%20become%20a%20very%20common)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=practice%20to%20use%20Batch%20Normalization,Neat). 실제로 BatchNorm을 쓰면 기울기 소실이나 폭주를 방지하고, 어느 정도 **정규화 효과**도 있어서 Dropout 없이도 잘 동작하는 경우가 많다. 훈련 시엔 배치 통계치를 쓰고, 테스트 시엔 이동 평균으로 추정된 전체 통계치를 사용한다는 구현상의 세부도 있다. BatchNorm 이후 최근에는 **LayerNorm, InstanceNorm, GroupNorm** 등 변형들이 제안되었는데, 이는 특수 상황에서 사용된다.
    
- **드롭아웃(Dropout):** (강의자료에 있다면) 과적합 방지를 위한 기법으로, 학습 시 각 미니배치에서 **뉴런을 확률 p로 무작위 끄기** 한다. 이렇게 하면 뉴런들이 서로에게 너무 의존하지 않게 되고 **앙상블 효과**를 낸다[cs231n.github.iocs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Dropout%20is%20an%20extremely%20effective%2C,setting%20it%20to%20zero%20otherwise). 테스트 시에는 모든 뉴런을 켜두되 출력에 학습 때 껐던 확률 p를 곱하여 기대값을 맞춰준다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=%2A%20Concretely%2C%20what%20Mask%20R,of%20convolutions%20and%20upsampling%20layers)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,bottom%20left). Dropout은 주로 완전연결층에 적용하며, Conv층에는 채널 별로 적용하는 Spatial Dropout 같은 변형이 있다.
- **전이 학습:** 대규모 데이터셋(예: ImageNet)으로 미리 학습된 모델의 가중치를 새로운 과제에 활용하는 방법이다. **특성 추출기로서 고정**하거나, **일부 미세조정(fine-tuning)** 한다. 예를 들어, 의료 영상 분류처럼 데이터가 적은 작업에서는 ImageNet으로 학습된 ResNet의 마지막 출력만 바꿔 재학습하면 훨씬 적은 데이터로도 높은 성능을 얻는다. 강의에서는 “**미리 학습된 가중치(pretrained weights)**를 얼마나 사용할지” 결정하는 방법을 논한다. 만약 대상 데이터셋이 원본과 유사하다면 (예: 개 사진 → 개품종 분류) 거의 모든 층 가중치를 재사용하고 마지막 부분만 조정하며, 데이터셋 차이가 크다면 상위 몇 개 층만 재사용하고 하위층은 재학습한다. Transfer learning은 **딥러닝이 폭넓게 쓰이게 된 실용적 요인** 중 하나로, 컴퓨팅 자원과 시간 절약에 매우 유용하다.

**실용 팁:** 학습을 개선하기 위한 추가 팁으로 **가중치 초기화** 기법 (Xavier 초기화, He 초기화 등)이 언급된다. 예컨대 ReLU를 사용할 경우 출력 분산 유지에 유리한 He 초기화(N(0,2/nin)N(0,2/*n*in))가 자주 쓰인다. 또한 **학습률 조정** 스케줄 (에폭에 따라 감소 등), **조기 종료(early stopping)**, **데이터 증가(data augmentation)** 등이 언급되어, 과적합을 막고 일반화 성능을 높이는 법을 다룬다. 데이터 증강으로는 이미지 회전, 좌우반전, 색상 변화 등이 흔히 사용되며, 이는 **사실상 훈련 데이터를 늘리는 효과**가 있어 딥러닝 모델의 성능 향상에 큰 도움을 준다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=RNN%2C%20LSTM%20Language%20modeling%20Image,rnn%2C%20neuraltalk2)[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=Image%20captioning%2C%20Vision%20%2B%20Language,rnn). 이번 강의를 통해 학생들은 이론적으로 배운 신경망을 **실제로 학습**시킬 때 맞닥뜨리는 문제들과, 이를 해결하는 기법들을 습득하게 된다. 이는 이후 과제나 프로젝트에서 복잡한 모델을 다룰 때 매우 유용한 지침이 될 것이다.

## **Lecture 8: Training Neural Networks, Part II**

**강의 제목:** *Training Neural Networks, part II. Update rules, hyperparameter tuning, Learning rate scheduling, data augmentation*

**핵심 개념:** 지난 강좌에 이어, 신경망 학습을 더욱 최적화하기 위한 기법들을 살펴본다. 특히 딥러닝에서 중요한 **최적화 기법의 변형들**(업데이트 규칙)과 **하이퍼파라미터 탐색** 방법, **학습률 스케줄링** 전략 등을 중점적으로 다룬다. 또한 데이터 증강에 대해서도 더 구체적인 사례와 효과를 논의한다. 목표는 **SGD만으로 부족할 때** 쓸 수 있는 기술들을 익히고, 복잡한 모델의 학습 과정을 잘 **조율(tune)**하는 방법을 이해하는 것이다.

**핵심 내용:**

- **고급 업데이트 규칙:** 기본 SGD 외에 모멘텀, RMSProp, Adam 등을 소개한다.
    - **Momentum SGD:** 이전 기울기 업데이트 방향을 누적하여 관성처럼 사용하는 방법으로, 수식은 v:=αv+η∇WL*v*:=*αv*+*η*∇*WL*, W:=W−v*W*:=*W*−*v*이다 (여기서 α*α*는 모멘텀 계수, 예컨대 0.9). 모멘텀을 쓰면 **곡면의 골짜기에서 지그재그 움직임**을 줄이고 더 빠르게 수렴한다.
    - **RMSProp:** 각 파라미터별로 **기울기의 제곱 평균**으로 스케일을 조정하여, 흔히 움직임이 큰 방향은 학습률을 낮추고, 작은 방향은 높이는 효과를 준다. 공식은 E[g2]t=0.9E[g2]t−1+0.1gt2*E*[*g*2]*t*=0.9*E*[*g*2]*t*−1+0.1*gt*2, W:=W−ηE[g2]t+ϵgt*W*:=*W*−*E*[*g*2]*t*+*ϵηgt*와 같다 (AdaGrad의 발전형).
    - **Adam:** 모멘텀과 RMSProp을 결합한 기법으로 현재 가장 널리 쓰인다. 1차 모멘트(평균)와 2차 모멘트(분산)을 모두 추적하여 mt=β1mt−1+(1−β1)gt*mt*=*β*1*mt*−1+(1−*β*1)*gt*, vt=β2vt−1+(1−β2)gt2*vt*=*β*2*vt*−1+(1−*β*2)*gt*2, 그리고 편향 보정 거친 m^t,v^t*m*^*t*,*v*^*t*로 W:=W−ηm^tv^t+ϵ*W*:=*W*−*ηv*^*t*+*ϵm*^*t*. Adam은 별도의 학습률 조정 없이도 잘 동작하고, 대부분의 문제에서 default(β1=0.9, β2=0.999)를 사용하면 무난하다. 다만 극단적으로 큰 배치 사용 시에는 재조정이 필요할 수 있다.
    - 그 밖에 Nadam, Adagrad, Adadelta 등도 언급되나 Adam이 사실상 표준임을 이야기할 수 있다. 중요한 것은 너무 **복잡한 최적화 기법에 의존하기보다**, 모델 구조와 학습률 등의 튜닝도 병행해야 한다는 점이다.
- **하이퍼파라미터 튜닝:** 학습률, 배치 크기, 모멘텀 계수, 정규화 계수 등 값 설정이 모델 성능에 큰 영향을 미친다. 최적값을 찾기 위해 **그리드 탐색**이나 **랜덤 탐색**이 사용된다. 연구에 따르면, 중요한 몇 개 파라미터 외에는 **무작위 탐색(Random Search)**가 효율적인데, 이는 그리드보다 더 다양한 조합을 시도할 수 있기 때문이다. 실용적으로는 로그 스케일로 범위를 정해 랜덤 샘플링하거나, **베이지안 최적화** 툴을 쓰기도 한다. 강의에서는 학습률은 우선 거듭 바꿔가며(loss 곡선을 보며) 찾고, 그 다음에 다른 것들을 조정하는 순서를 권장할 수 있다. 또한 **학습 곡선(train/val loss)**을 지속적으로 모니터링하여 undeerfitting/overfitting 여부를 판단하고, 필요한 조치를 (모델 용량 증가, 더 많은 데이터, 정규화 추가 등) 언급한다.
- **학습률 스케줄링:** 고정 학습률보다는 학습이 진행됨에 따라 값을 조정하는 게 일반적이다.
    - **스텝 다운(step decay):** 몇 에폭마다 학습률을 1/10로 감소. 예: 100에폭 학습 시 30, 60, 90 에폭에 감소.
    - **지수 감소(exponential decay):** ηt=η0⋅γt*ηt*=*η*0⋅*γt* 식으로 매 스텝마다 조금씩 감소(γ<1*γ*<1).
    - **사이클링(cyclic) & warm-up:** 최근엔 학습 초반에는 낮게 시작해 서서히 올렸다가, 이후 서서히 내리는 **사이클**이나, **Cosine Annealing** 같은 스케줄도 쓴다. 예를 들어 **cosine annealing**은 학습률을 코사인 곡선 형태로 줄여 마지막엔 0에 가깝게 만든다.
    - **Plateau 기반 감소:** 검증 손실 향상이 일정 기간 없으면 학습률을 줄이는 방식도 있다.
        
        학습률 스케줄링은 **최종 정확도 향상과 수렴 안정화**에 중요하며, 딥러닝 프레임워크에서 콜백 등으로 쉽게 적용할 수 있다.
        
- **데이터 증강 (심화):** 전 강의에 이어, 특히 **컴퓨터 비전에서 필수적인 데이터 증강 기법**들을 강조한다. 예를 들어 **이미지 분류**에서는 랜덤 자르기(crop), 좌우 뒤집기, 밝기/대비 변환, 색상 채널 시프트 등을 통해 네트워크가 다양한 형태의 데이터를 보도록 한다. **객체 검출**에서는 스케일 변화, aspect 비율 변화, 배경 덧붙이기 등이 쓰인다. **치명적 증강(patchcut, mixup 등)**의 최신 기법들도 언급될 수 있다. 적절한 증강은 일반화 성능을 크게 높일 수 있으나, 과도한 증강은 오히려 **데이터 분포를 왜곡**할 위험도 있으므로 경험적으로 조율해야 함도 설명한다.

**종합:** Part I과 II를 통해 딥러닝 모델 학습의 **모범 사례(best practice)**가 정리된다. 이는 학생들이 과제나 연구 프로젝트에서 모델을 효과적으로 학습시키는 데 직접적인 가이드가 된다. 또한 부록으로, **모델 성능 개선을 위한 팁** (예: **앙상블(ensembling)**을 사용하면 일반화 성능이 향상된다는 점이나, **모델 체크포인팅**을 통해 최상의 validation 성능 모델을 저장하는 습관 등)도 함께 논의할 수 있다. 이로써 딥러닝 모델을 단순히 구축하는 단계를 넘어, **숙련되게 다루는 법**을 습득하게 된다.

## **Lecture 9: CNN Architectures**

**강의 제목:** *CNN Architectures. AlexNet, VGG, GoogLeNet, ResNet, etc*

**핵심 개념:** 이 강의에서는 현대 컴퓨터 비전의 성능을 끌어올린 대표적인 **CNN 구조들(CNN architectures)**을 살펴본다. 2012년부터 2015년 사이 ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 경쟁을 통해 발전해 온 **AlexNet, VGGNet, GoogLeNet(Inception), ResNet** 등 네트워크의 **구조적 특징과 혁신점**이 주요 내용이다. 이러한 아키텍처 비교를 통해 **신경망의 깊이, 폭, 모듈 구성** 등이 성능에 미치는 영향을 이해하고, 최신 모델 경향 (예: 더 깊고 복잡해지는 대신 나중에는 효율성 추구) 등을 학습한다.

**주요 아키텍처 개요:**

- **AlexNet (2012):** 현대 딥러닝 재부흥의 시초. 8층 구조(5개 Conv + 3개 FC)로 구성되었으며, **ReLU 활성화 함수**를 대규모 네트워크에 처음 적용하고, **드롭아웃**으로 FC층 과적합을 억제했다. 또한 **GPU 2장**으로 모델을 병렬 학습하여 약 1천만 개의 파라미터를 효과적으로 학습했다. 결과적으로 이미지넷 top-5 에러율을 기존 26%→16%로 크게 향상시켰다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%205%20CNN%20Architectures%20AlexNet%2C,May%207%20Recurrent%20Neural%20Networks)cs231n.github.io. **혁신:** ReLU 도입으로 학습 6배 가속cs231n.github.io, 지역 응답 정규화(LRN) 사용 (현재는 거의 사용되지 않음), 데이터 증강(이미지 자르기, 뒤집기) 적극 활용.
- **VGGNet (2014):** 옥스포드 VGG팀이 개발. **심층화(depth)**에 집중하여 16~19층 매우 깊은 네트워크를 제안. 모든 Conv를 3×33×3 작은 필터로 하고, 풀링으로 공간 축소 후 채널 수 증가 패턴을 반복했다. VGG-16은 약 **1.38억 개 파라미터**로 매우 크지만, 단순하고 규칙적인 구조 덕분에 널리 사용되었다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%205%20CNN%20Architectures%20AlexNet%2C,May%207%20Recurrent%20Neural%20Networks). **혁신:** 작은 필터 여러 개로 큰 수용영역 효과 (예: 3×33×3 conv 3개 = 7×77×7 효과), 네트워크 깊이가 성능에 중요함을 입증. 단점은 파라미터 수와 연산량이 너무 많아 실용적 제약.
- **GoogLeNet (Inception, 2014):** 구글 팀 제안. **Network-in-network** 아이디어로 **Inception 모듈**을 설계하여, 서로 다른 크기의 필터(1x1,3x3,5x5) 결과를 concat하는 블록을 쌓았다. 또한 **글로벌 평균 풀링**으로 FC층을 제거해 파라미터 수를 크게 줄였다. 22층 구조인데 파라미터는 1,200만 정도로 VGG보다 훨씬 효율적이다. **혁신:** **1x1 컨볼루션**으로 채널축 축소(차원 감소)하여 연산량 절감, 모듈화된 설계로 병렬 특징 추출. GoogLeNet은 ensemble 7개 모델로 6.7% top-5 error를 기록.
- **ResNet (2015):** MSRA He 등 제안. **잔차 학습(residual learning)** 개념 도입으로 152층까지 매우 깊은 네트워크 학습을 성공. 기본 아이디어는 **스킵 연결(skip connection)**로, H(x)*H*(*x*)를 직접 학습하기보다 F(x)=H(x)−x*F*(*x*)=*H*(*x*)−*x* 형태의 residual 함수를 학습하도록 함으로써 **기울기 소실 없이** 깊이 누적. 실험적으로 깊이가 늘어나 성능이 떨어지는 **degradation 문제**를 해결했다cs231n.github.iocs231n.github.io. ResNet-152는 2.5억 파라미터로 5.7% error 달성. **혁신:** 매우 깊은 망에서의 효율적 학습, 이후 다양한 변형(Pre-activation ResNet, ResNeXt 등)과 비전 외 분야에도 영향.
- **그 외 구조:** 2016년 이후 **DenseNet**(스킵을 더 촘촘히), **MobileNet**(경량화, depthwise conv), **EfficientNet**(NAS로 scale 조정 최적화) 등이 등장했다. 강의에서는 시간상 주요 4개에 집중하되, 이러한 이후 모델들도 간략 소개하여 추세를 보여준다. 특히 **효율성과 정확도의 trade-off**를 다루고, 실무에서는 ResNet류가 사실상 기본 백본(backbone)으로 쓰인다는 점을 언급한다.

**아키텍처 비교 정리:**

- *Depth(층 수)*: AlexNet(8) < VGG(16-19) < GoogLeNet(22) ≈ ResNet(>50~152) (ResNet은 skip으로 실질적 depth 극복)
- *Param 규모*: AlexNet(60M) > VGG-16(138M) >> GoogLeNet(12M) < ResNet-50(25M) (ResNet-152 ~60M)
- *특징*: AlexNet – 첫 대형 CNN, VGG – 깊이 증가와 통일된 필터, GoogLeNet – 멀티스케일 Inception모듈, ResNet – 초심층 및 skip연결
- *효과*: 깊어질수록 특성 표현력이 좋아져 대규모 데이터셋에서 성능 향상. 그러나 너무 깊으면 학습 어려움 -> ResNet으로 해결. 또한 파라미터 효율성과 정확도 모두 중요해짐 -> GoogLeNet/ResNet 방향.
    
    이러한 비교를 표나 bullet로 제시하여 학생들이 흐름을 파악하기 쉽게 한다.
    

**응용:** 이러한 아키텍처들은 **사전 학습 모델**로서도 쓰이며, 실제 다양한 비전 과제에서 특징 추출기나 백본으로 활용된다. 예를 들어 **Faster R-CNN**(객체 검출)은 ResNet-50이나 101을 백본으로 사용하고, **분할(segmentation)** 모델들도 백본을 공유한다. 또한 모델 경량화가 필요한 모바일/임베디드에서는 MobileNet처럼 파라미터를 줄인 변형이 쓰인다. 강의에서는 각 아키텍처가 발표된 당시의 임팩트를 역사적으로 설명하며, 학생들에게 논문을 직접 읽어보도록 권장한다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%205%20CNN%20Architectures%20AlexNet%2C,May%207%20Recurrent%20Neural%20Networks)[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=Vision%20%2B%20Language%20Attention%20,rnn). 각 구조의 핵심 표나 그림을 슬라이드로 보여주며, CNN 설계에 대한 직관을 키우는 것이 이 강의의 목표다.

## **Lecture 10: Recurrent Neural Networks**

**강의 제목:** *Recurrent Neural Networks. RNN, LSTM, Language modeling, Image captioning, Vision + Language, Attention*

**핵심 개념:** 순환 신경망(RNN)은 **순차 데이터(시퀀스)**를 다루는 신경망 구조로, 시간에 따라 **상태(state)**를 유지하며 입력을 처리한다. 이번 강의에서는 RNN의 기본 구조와 **LSTM(Long Short-Term Memory)**, **GRU(Gated Recurrent Unit)**와 같은 개선된 셀을 소개한다. 또한 **비전+자연어 결합** 응용으로, 이미지 특징을 RNN에 연결하여 **이미지 캡셔닝(Image Captioning)**을 수행하는 예제를 다룬다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%208%20Midterm%20Review%20,48%20VAE%20Notes)[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%2012%20Take,Notes%20NeurIPS%202016%20GAN%20Tutorial). 마지막으로 최근 딥러닝의 화두인 **어텐션(attention)** 메커니즘 개념을 언급하며, RNN과 attention이 결합된 구조(예: *Show, Attend and Tell* 모델)를 소개한다.

**주요 내용:**

- **RNN 기본 구조:** 순환신경망은 **은닉 상태(hidden state)** ht*ht*를 유지하면서, 시각 t*t*의 입력 xt*xt*를 처리하고 다음 시각으로 state를 전달한다. 수식으로 ht=f(Whhht−1+Wxhxt+bh)*ht*=*f*(*Whhht*−1+*Wxhxt*+*bh*), yt=Whyht+by*yt*=*Whyht*+*by* 형태로 표현된다[cs231n.stanford.edu](https://cs231n.stanford.edu/slides/2025/lecture_17.pdf#:~:text=,the%20world%20and%20have). 여기서 f*f*는 tanh 또는 ReLU 등이 사용된다. RNN은 **가변 길이 시퀀스**를 처리할 수 있으며, 내부 순환으로 인해 **시계열 의존성**을 모델링한다. 그러나 기본 RNN은 장기 의존(long-term dependency) 학습이 어려워, 역전파 시 **그래디언트 소실/폭발** 문제가 발생할 수 있다.
- **LSTM과 GRU:** 장기 의존 문제를 해결하기 위해 gating 메커니즘을 도입한 LSTM이 소개된다. LSTM 셀은 **입력게이트(input gate)**, **망각게이트(forget gate)**, **출력게이트(output gate)**를 두고, **셀 상태(cell state)** Ct*Ct*를 유지하여 중요한 정보를 오랫동안 보존한다. 핵심 수식으로:
    
    ft=σ(Wf[ht−1,xt]+bf)*ft*=*σ*(*Wf*[*ht*−1,*xt*]+*bf*) (forget gate)
    
    it=σ(Wi[ht−1,xt]+bi)*it*=*σ*(*Wi*[*ht*−1,*xt*]+*bi*) (input gate)
    
    ot=σ(Wo[ht−1,xt]+bo)*ot*=*σ*(*Wo*[*ht*−1,*xt*]+*bo*) (output gate)
    
    C~t=tanh⁡(WC[ht−1,xt]+bC)*C*~*t*=tanh(*WC*[*ht*−1,*xt*]+*bC*) (cell input)
    
    Ct=ft∗Ct−1+it∗C~t*Ct*=*ft*∗*Ct*−1+*it*∗*C*~*t*
    
    ht=ot∗tanh⁡(Ct)*ht*=*ot*∗tanh(*Ct*).
    
    이로써 그래디언트가 cell state 경로로 흐를 때 곱셈 게이트를 통과하며, 적절히 기억/삭제를 배우게 된다. **GRU**는 LSTM에서 게이트 수를 줄인 간소화 버전으로, update게이트 zt*zt*와 reset게이트 rt*rt* 두 개만 사용한다. 실제 성능은 두 셀이 비슷하며, 구조 단순한 GRU가 약간 적은 파라미터로 구현된다.
    
- **언어 모델링:** RNN의 전통적 과제는 주어진 단어 시퀀스로 다음 단어를 예측하는 것이다. 예를 들어 “The cat sat on the”까지 입력되면 RNN이 “mat”을 예측하는 식이다. 이런 **Language Model**은 단어 임베딩을 입력으로 받아 작동하며, 생성 모델로서 텍스트 생성, 음성 인식 후처리 등에 활용된다[cs231n.stanford.edu](https://cs231n.stanford.edu/slides/2025/lecture_17.pdf#:~:text=,the%20world%20and%20have). RNN 학습에는 **Teacher Forcing**(이전 출력을 정답으로 대치하여 입력)이나 BPTT(Backpropagation Through Time) 등의 기법이 쓰인다.
- **이미지 캡셔닝 (Vision+Language):** 이미지 캡셔닝은 **CNN+RNN 결합**의 대표적 사례다. 사전 학습된 CNN (예: ResNet)의 마지막 숨겨진 표현(특징 벡터)를 RNN의 초기 은닉상태 h0*h*0 또는 입력 x0*x*0로 사용하여, RNN이 이미지를 묘사하는 문장을 생성한다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%207%20Recurrent%20Neural%20Networks,rnn)[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=Language%20modeling%20Image%20captioning%2C%20Vision,slides). 예컨대, 이미지 특징을 입력받은 RNN이 “A cat sitting on a mat.”과 같은 문장을 순차적으로 출력한다. 이때 훈련은 이미지에 달린 캡션 텍스트를 교사신호로 하는 **교차 엔트로피 손실**로 이루어진다. 또한 성능 향상을 위해 **어텐션(attention)**을 도입할 수 있는데, 이는 RNN이 단어를 생성할 때 이미지의 특정 부분 특징에 가중치를 두어 **동적으로 참조**하는 방법이다.
- **어텐션 메커니즘:** 어텐션은 RNN이나 트랜스포머에서 매우 중요하며, 강의에서는 간략 개념만 소개한다. 이미지 캡셔닝 맥락에서는 CNN이 추출한 공간별 특징맵(예: 14x14 셀로 나눈 특징들)에 가중합을 구해, 매 단어 출력마다 어디를 볼지 달리한다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%207%20Recurrent%20Neural%20Networks,rnn). 이 가중치는 softmax로 정상화된 “attention weight”이며, 예를 들어 “cat” 단어를 낼 때는 이미지의 고양이 부근 픽셀 특징에 높은 어텐션을 주는 식이다. Attention 개념은 이후 Transformer 구조 (2017년 이후)에서 RNN을 대체하는 핵심으로 부상하지만, 본 강의에서는 RNN 보조 개념으로 맛보기만 다룬다.

**응용 사례:**

- **기계 번역:** RNN(혹은 LSTM) 인코더-디코더 + Attention이 과거 기계번역에 쓰였으며, 원문을 인코딩 후 Attention을 통해 각 번역 단어 생성 시 원문의 어떤 부분을 참고할지 결정했다. 이는 Vision이 아닌 NLP 사례지만, 시계열 어텐션의 대표적인 성공으로 언급된다.
- **비디오 처리:** RNN은 연속된 이미지(Frame) 처리에도 쓰여, 동영상 내 객체 동작 예측, 행동 인식 등에 활용된다. CNN이 각 프레임 특징을 뽑고, RNN이 시간적 패턴을 학습하는 형태다.
- **강의 언급 자료:** 권장 읽을거리로 Karpathy의 RNN 블로그 글, Andrej Karpathy의 char-RNN (문자 단위 언어모델) 예제 코드[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=Image%20captioning%2C%20Vision%20%2B%20Language,rnn), Show & Tell / Show, Attend & Tell 논문 등이 소개된다.
- **Transformer 언급:** 2021년 시점이므로, RNN 대안으로 self-attention 기반 Transformer 모델들도 흘끗 언급될 수 있다 (비전 트랜스포머 ViT 등). 다만 상세는 범위를 벗어나고, RNN의 한계 (장기 의존, 병렬화 어려움)를 해결하기 위한 방향성 정도만 짚고 넘어간다.

종합하면, 이 강의를 통해 학생들은 시계열 및 순차 데이터 처리를 위한 딥러닝 방법론을 배우고, **이미지+텍스트 멀티모달** AI의 기초도 접하게 된다. 이는 이후 프로젝트에서 캡션 생성, VQA(시각 질의응답) 등의 주제를 다루는 발판이 될 수 있다.

## **Lecture 11: Generative Models**

**강의 제목:** *Generative Models. PixelRNN/PixelCNN, Variational auto-encoders, Generative adversarial networks*

**핵심 개념:** 생성 모델(Generative Model)은 **데이터 분포 p(x)*p*(*x*)**를 학습하여 새로운 샘플을 생성하는 모델이다. 이 강의에서는 대표적인 생성 모델 세 가지를 다룬다: (1) **자기회귀 모델** PixelRNN/PixelCNN, (2) **변분 오토인코더(VAE)**, (3) **생성적 적대 신경망(GAN)**. 각 접근은 확률모델링 방식과 학습 목표가 다르며, 장단점을 갖는다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,for%20modeling%20the%20data%20likelihood)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,update%20its%20decision%20boundary%20to). 예를 들어 PixelCNN은 **정확한 확률모델**이지만 샘플링이 느리고, GAN은 빠르게 사실적인 샘플을 만들지만 명시적 확률을 제공하지 않는다. 강의는 이들 개념적 차이를 강조하고, 중요한 수식과 아이디어를 소개한다.

**주요 내용 및 수식:**

- **PixelRNN/CNN (자기회귀 생성)**: 이미지의 픽셀들을 **정해진 순서**(예: 왼쪽 위에서 오른쪽 아래로)로 생성하는 모델이다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,for%20modeling%20the%20data%20likelihood). 조건부 확률로 모델링하여 p(x)=∏ip(xi∣x1,…,xi−1)*p*(**x**)=∏*ip*(*xi*∣*x*1,…,*xi*−1)로 인수분해한다. PixelRNN은 RNN으로, PixelCNN은 CNN으로 이 조건부 확률들을 구현한다. 예컨대 PixelCNN은 **마스킹(masking)**된 합성곱을 사용하여 현재 픽셀을 미래 픽셀에 보지 않고 이전 픽셀들만 참고하도록 한다. 이 모델들은 **정확한 우도(likelihood)**를 계산할 수 있어 **확률적 생성**이 가능하지만, 단점은 픽셀단위 순차 생성이라 고해상도 이미지 샘플링이 매우 느리다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,for%20modeling%20the%20data%20likelihood)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=likelihood%20function,the%20data%20likelihood%20function%20over).
- **Variational Auto-Encoder (VAE):** VAE는 **확률적 인코더-디코더** 구조로, 숨겨진 **잠재 변수(latent variable) z*z**를 통해 데이터를 생성한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,to%20optimize%2C%20so%20we%20derived). 인코더 qϕ(z∣x)*qϕ*(*z*∣*x*)와 디코더 pθ(x∣z)*pθ*(*x*∣*z*)를 구성하고, **변분추론**으로 qϕ*qϕ*를 학습하여 **증거 하한(ELBO)**를 최대화한다. ELBO 수식은:
    
    L(θ,ϕ)=Eqϕ(z∣x)[log⁡pθ(x∣z)]−DKL(qϕ(z∣x)∥p(z))L(*θ*,*ϕ*)=E*qϕ*(*z*∣*x*)[log*pθ*(*x*∣*z*)]−*DKL*(*qϕ*(*z*∣*x*)∥*p*(*z*))
    
    이 값이 데이터의 log-likelihood log⁡pθ(x)log*pθ*(*x*)의 하한이라는 것을 이용한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,GANs%29%20which%20learn)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,between%20the%20generator%20and%20the). 첫 항은 **재구성 오류(reconstruction error)**, 둘째 항은 인코더 분포가 사전분포 p(z)*p*(*z*) (일반적으로 N(0,I)*N*(0,*I*))와 얼마나 다른지 측정하는 **KL 벌점**이다. VAE의 장점은 **명시적 밀도 추정**이 가능하고, 인코더 덕에 임의 데이터에 해당하는 z*z*를 추론할 수 있다는 점이다. 하지만 생성 샘플 선명도가 GAN보다 떨어지고, ELBO 근사 때문에 약간 블러(blur)된 결과가 나오는 경향이 있다. 학습에는 **reparameterization trick**이 핵심으로, z=μ(x)+σ(x)⊙ϵ,ϵ∼N(0,I)*z*=*μ*(*x*)+*σ*(*x*)⊙*ϵ*,*ϵ*∼*N*(0,*I*)로 gradient 전파가 가능하게 한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,train%20the%20entire%20VAE%20model).
    
- **Generative Adversarial Network (GAN):** Ian Goodfellow 등이 제안한 GAN은 **게임 이론적** 프레임워크로 **두 네트워크 (발생기 G, 판별기 D)**가 경쟁하며 학습한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,update%20its%20decision%20boundary%20to)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,%E2%80%9Cnaturality%E2%80%9D%20of%20the%20generated%20images). 목표는 G가 진짜같은 데이터를 생성하면, D는 입력이 진짜 데이터인지 G의 가짜 샘플인지 맞추는 것이다. **미니맥스 오브젝티브**로 표현하면:
    
    min⁡Gmax⁡D  V(D,G)=Ex∼pdata[log⁡D(x)]+Ez∼p(z)[log⁡(1−D(G(z)))]min*G*max*DV*(*D*,*G*)=E*x*∼*p*data[log*D*(*x*)]+E*z*∼*p*(*z*)[log(1−*D*(*G*(*z*)))]
    
    G는 고정된 잠재분포 p(z)*p*(*z*) (예: N(0,I)*N*(0,*I*))로부터 샘플을 받아 가짜 데이터를 만들고, D는 입력이 진짜일 확률을 출력한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=discriminator%20to%20tell%20if%20the,update%20its%20decision%20boundary%20to)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,to%20train%20the%20networks%20iteratively). 학습은 번갈아 가며 D를 올리고 G를 내리는 식으로 이뤄지며, 이상적으로는 G가 데이터 분포를 모방하여 D를 속일 확률 0.5를 만드는 균형점에 도달한다. **장점:** GAN은 **명시적 확률 정의 없이** 직접 샘플을 만들어 이미지가 매우 선명하고 사실적이다. **단점:** 훈련이 불안정하여 **모드 붕괴(mode collapse)** (다양한 샘플 미생성) 등의 문제가 있고, likelihood 평가가 불가능하다. 이후 개선으로 WGAN(Wasserstein GAN), DCGAN(안정된 구조 제안) 등이 나왔지만, 기본 아이디어는 판별자를 속이는 생성자 훈련이다.
    
- **비교:** PixelCNN과 VAE는 **확률 모델**로서 likelihood를 다루고 추론이 가능하지만, 출력물 선명도는 제한적이다. GAN은 확률모델은 아니지만 고품질 샘플을 생성한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,for%20modeling%20the%20data%20likelihood)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,update%20its%20decision%20boundary%20to). 이들을 **Explicit vs Implicit**, **Approximate vs Exact inference** 기준으로 분류하면 좋은 정리가 된다. (예: PixelCNN - explicit & exact, VAE - explicit & approximate, GAN - implicit & no inference 필요).

**응용 및 발전:**

- **이미지 생성:** 이 모델들로 고해상도 인물 얼굴 생성, 가상 환경 생성 등이 가능해졌다. 특히 GAN 기반 **딥페이크**나 **이미지-to-이미지 변환**(CycleGAN 등)이 사회적으로도 이슈가 되었다.
- **데이터 증강:** 생성 모델로부터 샘플을 뽑아 데이터셋을 보강하거나, GAN으로 **의미적 편집**(예: 스케치→사진) 등의 응용이 가능하다.
- **모델 결합:** VAE와 GAN을 결합한 VAE-GAN, Auto-regressive GAN hybrids 등 다양한 연구가 진행되었으며, 2021년 즈음 **Diffusion Model**이라는 새로운 생성 패러다임도 등장했다 (Zeitgeist로 간략 언급). 하지만 강의 범위에서는 PixelCNN/VAE/GAN 3대장에 집중한다.

강의는 OpenAI의 **DALL-E**, **GPT 계열**처럼 멀티모달/거대 모델의 방향도 간략 언급할 수 있다. 예를 들어 “이러한 생성 모델 아이디어가 결국 거대 언어 모델과 결합되어 놀라운 결과를 내고 있다” 정도로 연결. 또한 학생들이 **deepgenerativemodels** 사이트나 GAN 튜토리얼[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=May%2014%20Generative%20Models%20PixelRNN%2FPixelCNN,Notes%20NeurIPS%202016%20GAN%20Tutorial)[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=Variational%20auto,Notes%20NeurIPS%202016%20GAN%20Tutorial)를 참고하도록 권장하며, 과제로 간단한 VAE 혹은 GAN을 구현해보는 것을 제안할 수도 있다. 이 강의를 통해 학생들은 생성모델의 기본 개념과 수학적 원리를 익혀, 생성적 AI의 토대를 이해하게 된다.

## **Lecture 12: Detection and Segmentation**

**강의 제목:** *Detection and Segmentation. Semantic segmentation, Object detection, Instance segmentation*

**핵심 개념:** 이제 이미지 분류를 넘어 **이미지 내의 자세한 이해**로 확장한다. **객체 검출(Object Detection)**은 이미지 안에 **여러 객체의 위치(바운딩 박스)와 종류**를 찾아내는 과제이고, **분할(Segmentation)**은 이미지의 모든 픽셀에 라벨을 지정하는 과제이다. 분할에는 **장면 분할(Semantic Segmentation)**과 **인스턴스 분할(Instance Segmentation)**이 있는데, 전자는 같은 클래스는 구분 없이 한 카테고리로 묶고, 후자는 같은 클래스라도 개별 객체를 분리한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,shown%20below)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=box%2C%20we%E2%80%99re%20basically%20doing%20instance,segmentation). 이 강의에서는 이 세 가지 문제의 대표적인 해결 방법들을 소개하고, 분류와 무엇이 다른지 강조한다. 또한 **탐지와 분할을 위한 CNN 구조**(R-CNN 계열, Fully Convolutional Network 등)을 개략적으로 다룬다.

**주요 내용:**

- **객체 검출 (Object Detection):** 이미지를 입력받아 사각형 바운딩 박스들과 클래스 레이블들을 출력한다. 과거에는 **슬라이딩 윈도우 + 분류기** 방식으로, 다양한 위치/크기의 윈도우를 일일이 분류했으나 **계산량이 막대**했다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,or%20simply%2C%20%E2%80%9Cobject%20detection%E2%80%9D)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,problems%20of%20segmentation%20and%20detection). 현대적 방법은 **지역 제안(Region Proposal)**과 CNN을 결합한 **R-CNN 계열**이 대표적이다.
    - *R-CNN:* (2013) **Selective Search** 등 알고리즘으로 ~2000개의 후보영역(region)을 추출 → 각 영역을 CNN으로 분류 (AlexNet 등) → Post-processing(NMS)로 최종 결정. 단점: CNN forward를 2000번 하니 매우 느림.
    - *Fast R-CNN:* (2015) 한 장의 이미지에 대해 **하나의 CNN**으로 전체 특징맵을 추출하고, 각 region을 특징맵 위에서 **RoI Pooling**으로 고정크기 피쳐로 뽑아 한 번에 분류/회귀. 훨씬 빠르지만 여전히 region proposal은 별도 단계.
    - *Faster R-CNN:* (2015) CNN의 중간 feature맵에서 **Region Proposal Network (RPN)**을 통해 region도 CNN이 직접 예측하도록 함. 엔드투엔드 학습 가능, 거의 실시간 가까이 속도 개선.
    - *SSD/YOLO:* (2016) **단일 단계(single-stage)** 검출로, 이미지 특징맵의 여러 스케일 위치마다 바운딩박스와 클래스 예측. 속도가 매우 빠르나, 작은 객체 등에서 정확도는 두단계 방식보다 약간 떨어질 수 있음[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,faster%20but%20not%20as%20accurate)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Object%20Detection%3A%20Summary). 그러나 기법 발전으로 SSD/YOLO 계열 성능도 많이 올라와, **모바일/실시간 응용**에 주로 사용.
    
    > ※ 성능 비교: Faster R-CNN (two-stage) 계열은 정확도 높음 (예: COCO mAP↑) 그러나 속도 느림; YOLO/SSD (one-stage)는 속도 빠름 (실시간 가능) 그러나 약간 정확도 손해aman.aiaman.ai. 선택은 응용에 따라 trade-off.
    > 
    - **평가 지표:** IoU(Intersection over Union) > 0.5 기준 **mAP(mean Average Precision)** 등을 사용. IoU는 예측박스와 정답박스의 교집합면적을 합집합면적으로 나눈 값으로, 1이면 완벽히 일치, 0이면 전혀 안 겹침이다.
- **전장면 분할 (Semantic Segmentation):** **픽셀 단위 분류**로 볼 수 있다. naive한 접근으로 **슬라이딩 윈도우 픽셀 분류**가 가능하나, 픽셀마다 CNN 적용은 매우 느리다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Semantic%20Segmentation)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Image). 2015년 **Fully Convolutional Network (FCN)**이 나오면서 일반 CNN 분류기를 **컨볼루션+업샘플링** 구조로 바꿔 이미지 크기 출력으로 확장하였다. 핵심은, 분류 CNN의 FC층을 **1x1 conv**로 대체하고, 다운샘플된 특징맵을 **deconvolution(Transpose Conv) 또는 업샘플링**으로 원래 크기로 복원하여 픽셀 라벨맵을 얻는 것[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Convolution)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Image). 이후 **U-Net, SegNet, DeepLab** 등 다양한 개선이 나와 경계 세밀화, 다중 스케일 처리 등을 한다. 장면 분할의 평가지표는 **픽셀 정확도** 또는 **IoU per class** 등 사용.
- **인스턴스 분할 (Instance Segmentation):** 이는 **검출 + 분할**의 조합 문제로 볼 수 있다. 대표적 방법은 **Mask R-CNN**(2017)으로, Faster R-CNN의 각 Region에 대해 **마스크 분할 브랜치**를 추가한 것이다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,CNN%E2%80%9D%20%282017%29%20does)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=%2A%20Concretely%2C%20what%20Mask%20R,of%20convolutions%20and%20upsampling%20layers). RoI Align 등을 통해 각 region을 작은 고정 크기(예:14x14)로 샘플링하고, 이를 deconv 등으로 upsample하여 **이진 마스크**(그 region 내 해당 객체의 픽셀=1)를 출력한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=%2A%20Concretely%2C%20what%20Mask%20R,of%20convolutions%20and%20upsampling%20layers)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,bottom%20left). Mask R-CNN은 분할 외에, 추가로 **키포인트 검출(사람 포즈)** 등도 병렬로 확장 가능함을 논문에서 시연했다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Image). 인스턴스 분할 평가는 **AP_mask** 등의 지표로 COCO dataset에서 수행.

**종합:**

Detection과 Segmentation은 분류와 달리 **출력의 공간적 구조**를 다룬다. 모델이 복잡해지고 multi-task화되지만, 근본은 CNN 특징 추출이다. 강의에서는 슬라이드로 R-CNN부터 Mask R-CNN까지 구조 그림을 보여주며, 시간이 허락하면 YOLO 등의 예시도 시각화해준다. 특히 **한계 및 도전과제**도 논의하는데, 예를 들어 작은 객체 검출의 어려움, overlap 많은 객체 분할의 애로, **Speed vs Accuracy** trade-off, 그리고 최근 **PANet, U2Net** 등 최신 모델 간략 소개. 또한 **데이터셋** 소개도 중요: COCO, PASCAL VOC, Cityscapes 등 검출/분할 주요 벤치마크를 언급한다.

**응용:** 이러한 기술은 **자율주행차** (도로 객체 인식, 차선 분할), **의료 영상** (종양 영역 분할), **증강현실** (장면 이해) 등에 직접 활용된다. 산업적 임팩트가 크기에, **실시간 처리**와 **정확도 향상** 둘 다 연구의 초점이다. 강의는 Detectron2, TensorFlow API 등의 **오픈소스 툴** 소개[aman.ai](https://aman.ai/cs231n/detection/#:~:text=Open%20Source%20Frameworks)도 할 수 있으며, 프로젝트로 학생들이 자신만의 검출기를 fine-tune 해보도록 장려한다. Lecture 12를 통해 학생들은 딥러닝이 **이미지의 위치적 정보를 어떻게 다루는지** 이해하고, 분류 외의 비전 과제들에 대한 시야를 넓히게 된다.

## **Lecture 13: Visualizing and Understanding**

**강의 제목:** *Visualizing and Understanding. Feature visualization and inversion, Adversarial examples, DeepDream and style transfer*

**핵심 개념:** 딥러닝 모델은 높은 성능을 보이지만 **“블랙박스”**라는 한계가 있다. 이 강의는 신경망의 내부를 들여다보고 직관을 얻기 위한 여러 기법들을 다룬다: (1) **특징 시각화(feature visualization)** – 뉴런이 학습한 패턴을 이미지 형태로 만들어보기, (2) **네트워크 반전(network inversion)** – 중간층 표현으로부터 원본 입력 재구성, (3) **적대적 예제(adversarial example)** – 모델을 속이는 작은 입력 교란, (4) **딥드림(DeepDream)** – 입력 이미지의 과장된 패턴 시각화, (5) **신경 스타일 변환(neural style transfer)** – 콘텐츠 이미지와 스타일 이미지를 합성하는 기법. 이를 통해 딥러닝 모델의 해석 가능성, 취약점, 창의적 응용을 배우게 된다.

**주요 내용:**

- **특징 시각화 및 뉴런 활성화 이해:** 특정 레이어나 뉴런이 무엇을 감지하는지 알기 위해, **이미지 공간에서 그 뉴런의 활성을 최대화하는 입력**을 최적화로 찾는다. 예를 들어, Conv5 레이어의 어떤 채널이 “고양이 귀” 패턴에 반응한다면, 그 채널 출력을 최대화하도록 초기 이미지를 경사상승(gradient ascent)하면 귀 모양을 띤 시각적 패턴이 나타난다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,class%20and%20their%20semantic%20relationships). 이를 **딥비전(Deep Visualization)** 기법이라고 하며, Zeiler & Fergus (2013)의 deconvnet을 사용한 시각화도 소개된다. 그들은 Conv 특징 맵을 역으로 deconv하여 픽셀공간 투영함으로써, 어떤 입력 부분이 활성화의 원인인지 보였다. 이러한 방법으로 CNN이 **엣지, 질감, 물체 부분** 등을 단계별로 학습함을 확인할 수 있다.
- **적대적 예제 (Adversarial Example):** 인간에겐 똑같아 보이지만 모델엔 오분류되도록 의도적으로 만든 입력이다. 일반적으로 입력 이미지 x*x*에 아주 작은 교란 δ*δ*를 더해 (예: 노이즈가 평균 ±몇 LSB 수준) 모델 출력이 잘못되게 한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,). 수식으로, 대상 분류기가 f(x)*f*(*x*)라고 할 때 argmaxyf(x+δ)≠ytrueargmax*yf*(*x*+*δ*)=*y*true이면서 ∥δ∥∥*δ*∥는 아주 작게 만든다. 흔히 **FGSM(Fast Gradient Sign Method)**: x′=x+ϵ⋅sign(∇xL(f(x),ytrue))*x*′=*x*+*ϵ*⋅sign(∇*xL*(*f*(*x*),*y*true))으로 1-step 공격하거나, PGD 같은 iterative 방법도 있다. 이러한 공격은 모델의 **취약성**을 보여주며, 보안 이슈나 신뢰성 문제로 이어진다. 방어법으로 적대적 훈련(adversarial training) 등이 있지만, 고양이-쥐 게임 양상이다.
- **DeepDream:** 구글이 공개한 흥미로운 시각화로, 이미지의 특정 레이어 활성화를 증폭시키는 기법이다. 예컨대 원본 이미지에 대해 합성곱층 출력을 가져와 거기서 많이 발견된 패턴을 이미지에 더 강하게 되도록 역전파로 이미지를 수정한다. 그러면 이미지에 숨어있던 얼굴, 단풍 같은 패턴이 과장되어 *꿈꾸는 듯한* 그림이 된다[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=DeepDream%20and%20style%20transfer%20,style)[cs231n.stanford.edu](https://cs231n.stanford.edu/2021/syllabus.html#:~:text=Feature%20visualization%20and%20inversion%20Adversarial,style). DeepDream은 원래 네트워크 시각화 일환이었으나 예술적으로 큰 반향을 일으켰다. 구현상으로 특정 레이어 L*L*의 활성 AL*AL*에 대해 ∂sum(AL)∂x∂*x*∂sum(*AL*)를 계산하여 입력에 더해주는 식이다.
- **Style Transfer:** 2015년 Gatys 등이 발표한 기법으로, **콘텐츠 이미지**(예: 사진의 구조)와 **스타일 이미지**(예: 화가의 화풍)를 합성한 그림을 생성한다. 하나의 CNN(VGG 등)에서, 콘텐츠 이미지의 **중간층 feature map**은 고유한 구조를, 스타일 이미지의 **feature 통계(Gram matrix)**는 질감/화풍 정보를 나타낸다는 점을 활용한다. **손실 함수**는 콘텐츠 손실 Lc=∥Fl(xgen)−Fl(xcontent)∥2*Lc*=∥*Fl*(*x*gen)−*Fl*(*x*content)∥2 (어떤 레이어 l*l*의 feature 맵 차이)와 스타일 손실 Ls=∑l∥Gl(xgen)−Gl(xstyle)∥2*Ls*=∑*l*∥*Gl*(*x*gen)−*Gl*(*x*style)∥2 (여러 층 l*l*에서 Gram matrix 차이)를 합친 형태다. 생성 이미지를 초기화(보통 콘텐츠 이미지로)한 후 경사하강으로 이 손실을 최소화하면, 생성 이미지가 콘텐츠 형태를 가지면서 스타일 색감과 질감을 띠게 된다. 수식으로 Gram matrix Gijl=∑kFiklFjkl*Gijl*=∑*kFiklFjkl* (채널 간 상관)이며, 이는 질감을 표현한다. Style transfer는 iteration 몇백번으로 수렴하고, 결과는 예술적으로 매우 인상적이다. 이후 real-time 적용을 위해 **피드포워드 네트워크** 학습(Perceptual Loss by Johnson 등)이 나왔다고 언급 가능.

**응용:**

- 특징 시각화는 **네트워크 디버깅**에 쓰일 수 있다. 모델이 이상한 패턴(엣지가 아닌 글자패치 등)에 반응하면 데이터 편향을 의심해볼 수 있다.
- 적대적 예제는 **모델 배포시 보안** 이슈로 중요하다. 자율주행 차량의 표지판 인식 모델이 공격당하면 큰 위험이 있으므로, robust 모델 연구가 진행 중이다.
- DeepDream과 Style Transfer는 **창의적 콘텐츠 생성**의 예로, 예술과 AI의 접목을 보여준다. Neural Style Transfer 앱/소프트웨어가 대중적으로 인기를 끌기도 했다.
- 모델 해석 측면에서, **Grad-CAM** 같은 기법도 언급될 수 있다. 이는 특정 분류 결과에 기여한 이미지 영역을 heatmap으로 시각화하는 방법으로, CNN의 마지막 conv 출력과 gradient를 이용해 중요도를 계산한다. Grad-CAM은 실무에서 **시각적 설명(visual explanation)**으로 활용된다.

강의에서는 이러한 다양한 기법 시연 이미지를 많이 보여주며 (예: adversarial panda->gibbon 예시, DeepDream 개 이미지, Van Gogh 스타일 변환 등), 학생들의 흥미를 유발한다. 또한 **모델 신뢰성**과 **윤리적 이슈**(적대적 공격 악용 등)에 관한 짧은 토론을 유도할 수도 있다. 이 강의를 통해 딥러닝 내부에서 벌어지는 일을 조금 더 *“들여다볼”* 수 있게 되며, 동시에 AI와 예술의 접목 같은 폭넓은 활용 가능성도 엿보게 된다.

## **Lecture 14: Fairness Accountability Transparency and Ethics in AI**

**강의 제목:** *Fairness Accountability Transparency and Ethics in AI*

**핵심 개념:** 이 강의는 기술적인 내용에서 한발 물러나, **인공지능의 사회적 영향과 윤리**를 다룬다. AI 시스템이 편향되거나 차별적으로 작동하는 문제, 결과를 설명하기 어려운 투명성 부족, 잘못된 사용으로 인한 책임 소재 등이 주요 주제다. 특히 컴퓨터 비전 분야에서 불거진 **편향(bias)** 사례 (예: 얼굴인식에서 특정 인종/성별 성능차) 등을 통해 **공정성(fairness)**의 중요성을 논의한다[digitalgovernmenthub.org](https://digitalgovernmenthub.org/library/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/#:~:text=significant%20disparities%20in%20accuracy%20based,on%20gender%20and%20skin%20type)[digitalgovernmenthub.org](https://digitalgovernmenthub.org/library/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/#:~:text=Darker,and%20accountability%20in%20AI%20facial). 또한 데이터셋 구축 단계부터 윤리적 고려와 프라이버시 보호 등이 필요함을 강조한다. 이 강의는 Timnit Gebru 등 전문가의 견해를 통해, 기술 발전과 사회적 책임의 균형을 생각하도록 유도한다.

**주요 내용:**

- **AI 편향과 차별:** 머신러닝 모델은 학습 데이터의 편향을 그대로 답습하거나 증폭할 수 있다. 예로 **Gender Shades 연구**(Buolamwini & Gebru, 2018)를 보면, 상업 안면 인식기의 **성별 분류 정확도**가 인종과 성별에 따라 큰 차이를 보였다. 밝은 피부 남성의 오류율은 1% 미만인데, 어두운 피부 여성은 오류율이 34%까지 치솟았다[digitalgovernmenthub.org](https://digitalgovernmenthub.org/library/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/#:~:text=significant%20disparities%20in%20accuracy%20based,on%20gender%20and%20skin%20type)[digitalgovernmenthub.org](https://digitalgovernmenthub.org/library/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/#:~:text=Darker,and%20accountability%20in%20AI%20facial). 이러한 “인터섹션al” 편향은 데이터셋에 백인 남성 얼굴이 과다대표되었기 때문으로 분석되었다. 결과적으로, ML 시스템이 특정 집단에 불리하게 작용하면 사회적 불평등을 강화할 위험이 있다. 강의에서는 또 다른 예로 구글 포토가 흑인 인물을 “고릴라”로 태깅한 사고, 자율주행 데이터셋에 보행자로 백인만 많은 문제 등도 언급된다. **대처 방안:** 데이터 수집 단계에서 다양성 확보, 편향성 측정 지표 활용, 결과의 영향도 분석 등이 필요하다.
- **책임성과 투명성:** 딥러닝 모델의 결정은 복잡한 내부 연산 결과라 직관적으로 이해하기 어렵다. 하지만 응용에 따라 **설명가능성(Explanability)**이 필수인 경우가 있다. 예를 들어 범죄 수사나 의료 진단에 AI를 쓸 때, 왜 그런 결정을 했는지 설명을 요구받을 수 있다. **법/규제** 측면에서도 EU의 GDPR은 자동 결정에 대한 설명권리를 포함하고 있다. 이에 따라 **모델 해석 기법**(Lecture 13 Grad-CAM 등)이나 **간소한 대체모델**로 설명 생성 등이 연구되고 있다. 또한 **책임성(Accountability)**은 AI 오작동시 누구의 책임인가의 문제다. 예를 들어 자율주행차 사고시 제조사 vs 개발자 vs 사용자 책임이 불명확하다. 이를 위해 AI 시스템 개발자는 **윤리 가이드라인**을 따르고, 법/제도도 정비되어야 한다는 논의가 진행 중이다.
- **프라이버시와 감시:** 얼굴인식 기술이 프라이버시를 침해할 가능성, 국가 기관이 대규모 CCTV 얼굴인식으로 감시사회화하는 우려 등도 언급된다. **딥페이크** 기술의 악용 (음란물 합성, 가짜뉴스 영상 등) 역시 윤리적 이슈다. 이러한 기술에는 법적 규제와 함께, 기술적 대응 (딥페이크 탐지모델, dataset 수집 윤리) 등이 필요하다.
- **AI 윤리 원칙:** 강의에서는 공정성, 책임, 투명성 외에도 **유익성(Beneficence)**, **비유해성(Non-maleficence)** 같은 윤리 원칙을 소개할 수 있다. IEEE, EU, 각 대기업 등이 발표한 AI 윤리 가이드라인 (예: **Human-Centered AI** 원칙 – Lecture 15 주제와 연결) 등을 통해, 미래 AI 개발에는 기술적 우수성 뿐 아니라 인권, 평등, 환경 등의 가치가 함께 고려되어야 함을 강조한다.

**실세계 사례와 토론:** 이 강의는 학생들의 의견을 나누는 형태로 진행될 가능성이 높다. 구체적 사례 (아마존 채용 AI가 여성 지원자 차별한 사례, MS 챗봇 Tay의 부적절 발언 사건 등)를 소개하고, “어떻게 해야 하나”를 토론하게 할 수 있다. **기술적 대응**으로 **de-biasing** 방법 (re-sampling data, fairness constraint 학습 등)이나 **연합학습(Federated Learning)**을 통한 프라이버시 보호 학습 등도 언급된다. 또한 AI 연구 커뮤니티의 노력 (논문 공개시 **Datasheets for Datasets**나 **Model Cards** 작성 권장[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=Batch%20Normalization,and%20before%20non)[cs231n.github.io](https://cs231n.github.io/neural-networks-2/#:~:text=that%20use%20Batch%20Normalization%20are,Neat) 등)을 소개하며, 학생들이 앞으로 개발자가 되었을 때 **윤리적 책임 의식**을 갖출 것을 당부한다.

**Fei-Fei Li & Timnit Gebru 견해:** Timnit Gebru는 AI 윤리와 공정성 연구를 이끌던 인물로, 그가 강조한 “프로젝트 초기부터 다양성과 윤리를 고려해야 한다”는 메시지, “기술 업계 내부자의 책임있는 목소리”의 중요성을 이야기한다. Fei-Fei Li는 **인간 중심 AI**를 주창하며, 인간의 존엄과 복지를 중심에 둔 기술 개발을 역설한다[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=We%20also%20recognize%20that%20the,centered%20AI)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=,jobs%E2%80%94in%20the%20center%20of%20consideration). 이를 Lecture 15와 연결하며, 기술적 부분을 넘어 사회과학, 철학 등과 교류하는 **다학제적 접근**이 필요함을 주장한다[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=This%20framework%20looks%20at%20AI,study%20and%20forecast%20what%E2%80%99s%20coming)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=We%20use%20AI%20to%20do,study%20and%20forecast%20what%E2%80%99s%20coming).

결론적으로, 이 강의를 통해 학생들은 AI 시스템이 미치는 **사회적 함의**를 성찰하게 된다. “정의롭고 투명한 AI”를 구현하기 위해 어떤 노력이 필요한지 배우며, 엔지니어로서 가져야 할 **윤리의식**과 **협업 자세**(법률가/사회학자와 소통 등)를 인식하게 될 것이다.

## **Lecture 15: Human-Centered Artificial Intelligence**

**강의 제목:** *Human-Centered Artificial Intelligence*

**핵심 개념:** 인간 중심 AI는 기술 개발의 패러다임을 인간의 필요와 복지에 맞추는 접근이다. Fei-Fei Li 교수 등이 주창한 이 개념은, AI를 **인간을 증강(augment)**하는 도구로 보고, **인간의 존엄성과 가치**를 우선에 두는 것을 의미한다[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=We%20also%20recognize%20that%20the,centered%20AI)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=we%20think%20about%20this%20technology%2C,centered%20AI). 또한 AI 연구에 인문사회과학을 통합하여, AI가 사회 전반에 긍정적으로 기여하도록 하자는 다학제적 비전이다. 이 강의에서는 Human-Centered AI의 철학과 몇 가지 예시를 소개하며, 앞으로 AI 개발자가 나아갈 방향에 대해 논의한다.

**주요 내용:**

- **Human-in-the-loop:** 인간 중심 AI에서는 종종 **인간이 프로세스에 적극 개입**한다. 예를 들어, 완전 자율 시스템 대신 **반자율** 시스템으로 인간 전문가가 AI의 결정을 모니터링/승인하도록 설계하거나, AI가 인간에게 설명과 옵션을 제시하고 최종 결정을 인간이 내리게 하는 것이다. 이렇게 함으로써 AI 오작동을 검증하고, **인간의 판단**과 **맥락적 이해**를 활용할 수 있다. 의료 분야에서 AI가 진단 후보를 제시하고 의사가 판단을 확정하는 협업 진단 시스템이 좋은 예다.
- **증강지능 (Augmented Intelligence):** AI를 인간을 대체하는 것이 아니라 **능력 확장**의 수단으로 본다. 예컨대 시각장애인을 위한 **보조 비전 앱**(카메라로 본 장면을 설명해주는 AI)은 인간의 감각을 보완한다. 교육 분야에서는 AI 튜터가 있지만, 목표는 교사를 대체하는 게 아니라 **교사의 역량을 강화**하고 학생 개개인에 맞춤 지원을 제공하는 것이다. 이러한 접근은 일자리 측면에서도, AI 자동화로 인한 대체가 아닌 **인공지능 + 인간 팀**의 효율 증대를 지향한다. 실제로 고객센터에 챗봇이 투입되지만 최종 어려운 상담은 사람이 처리하되 AI가 요약/추천을 돕는 식으로 운영되기도 한다.
- **다양성 & 포용:** 인간 중심 AI 연구에는 **다양한 배경의 사람들** 참여가 중요하다. 기술 개발 과정에 여성, 소수인종, 사회과학자 등이 포함되어야 제품이 편향을 덜 가지며, 다양한 사용자 요구를 반영할 수 있다. Fei-Fei Li는 “AI는 컴퓨터 과학만의 영역이 아니라 인간에 관한 것이기 때문에, **모든 사람**이 AI 미래의 일부가 되어야 한다”고 강조한다. Stanford HAI 연구소의 구성원도 법학자, 철학자, 심리학자 등 다분야로 이루어져 있으며, 이는 AI 정책, 윤리 교육, 경제적 영향 연구 등을 활발히 하는 원동력이다.
- **윤리 원칙 & 거버넌스:** Human-Centered AI는 Lecture 14의 주제들과 연계된다. 특히 AI 개발 시 **인간의 프라이버시, 안전, 공정**을 기본 원칙으로 세우고, 이를 어기는 방향으로 나아가지 않도록 **가드레일(guardrails)**이 필요함을 역설한다[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=There%20are%20also%20a%20lot,centered%20AI%20framework)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=future%2C%20so%20that%20this%20technology,centered%20AI%20framework). 예를 들어, AI를 개발할 때 사전에 윤리적 위험을 평가하고 최소화하는 절차를 갖추는 것, 배포 후에도 지속적으로 영향을 모니터링하고 피드백을 반영하는 **거버넌스 체계** 마련 등이 필요하다[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=by%20a%20large%20language%20model,centered%20AI)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=I%20think%20putting%20guardrails%20and,the%20facts%20of%20this%20technology). 여기에는 정부의 역할(규제)과 산업계의 자기 규제, 시민사회의 감시가 모두 포함된다. Fei-Fei Li는 “이 거대 기술에 인간의 존엄, 인간의 행복을 중심에 두어야 한다”고 말하며[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=We%20also%20recognize%20that%20the,centered%20AI)[mckinsey.com](https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-dr-fei-fei-li-sees-worlds-of-possibilities-in-a-multidisciplinary-approach-to-ai#:~:text=we%20think%20about%20this%20technology%2C,centered%20AI), 이는 곧 기술의 목표 설정부터 인간을 위한 것으로 삼으라는 뜻이다.
- **사례 연구:** 실제 Human-Centered AI 프로젝트 사례로, 노인 돌봄을 위한 **동반 로봇** 연구, 정신건강 지원 챗봇, 개발도상국 농업 지원 AI, 환경 보호를 위한 보존 기술 (스마트 센싱) 등이 소개될 수 있다. 이런 사례들은 AI가 **인류 보편적 문제**(고령화, 건강, 빈곤, 환경)에 기여하도록 설계된 것들이다. 또 Stanford HAI에서 추진한 **COVID-19 대응 AI** (의료자원 배분 지원 등) 같은 최근 활동도 언급될 수 있다.

**학습 목표:** 학생들은 AI 개발에 있어 기술 지표(정확도, 속도)뿐 아니라 **사회적 지표(신뢰, 만족, 영향)**를 고려하는 시각을 배우게 된다. 또한 자신의 커리어에서 **윤리와 인간존중을 잊지 말 것**을 다짐받는다. Fei-Fei Li의 이야기 중 “AI의 가장 중요한 사용은 인간을 돕는 것이며, 인간의 일자리를 기계가 아니라 더욱 가치 있게 만들 것”이라는 메시지가 강조될 수 있다.

마지막으로, Human-Centered AI는 **교육적 측면**도 포함한다. 즉 AI 교육을 컴퓨터 과학자뿐 아니라 모든 시민에게 제공해 **AI 리터러시**를 높여야 한다는 주장이다. 그래야 모두가 AI 시대에 소외되지 않고, 공동으로 방향을 정할 수 있기 때문이다. 이러한 맥락에서 본 교과목 자체도 공학뿐 아니라 사회 맥락을 다루는 시도가 되고 있으며, 학생들이 **넓은 관점**을 가지는 것이 중요함을 일깨운다.

## **Lecture 16: 3D Deep Learning**

**강의 제목:** *3D Deep Learning*

**핵심 개념:** 지금까지는 2D 이미지 위주의 비전이었지만, 현실 세계는 3차원으로 구성되어 있다. 본 강의에서는 **3D 데이터**(예: 점군point cloud, 격자voxel, 격자mesh) 처리에 특화된 딥러닝 방법을 다룬다. 3D Deep Learning의 응용은 **자율주행**(LiDAR 센서 데이터 처리), **로봇공학**(3D 환경 인식), **가상현실/증강현실**(3D 객체 조작) 등 다양하다. Hao Su 등의 연구를 소개하며, 대표적으로 **PointNet** 구조와 **3D Convolutional Network**, 그리고 **그래프 신경망**을 활용한 3D 객체 처리 등을 논의한다.

**주요 내용:**

- **3D 데이터 표현과 난제:** 3차원 형상은 여러 방식으로 표현된다. **Voxel Grid**는 3D 공간을 격자로 나누어 각 셀에 occupancy나 거리를 저장하는 방식 (이미지의 3D 확장)으로, 기존 CNN을 3D convolution으로 일반화해 적용 가능하다. 하지만 해상도를 높이면 **메모리와 연산량**이 기하급수적으로 증가한다. **Mesh(폴리곤 망)**는 표면을 삼각형 등으로 근사한 구조로, 그래프로 볼 수 있으나 불규칙적 connectivity로 CNN 적용이 어렵다. **Point Cloud(점군)**는 표면을 샘플링한 점들의 집합 (예: LiDAR 출력)으로, 크기가 가변이고 순서없음(unordered) 특성이 있다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=3D%20Object%20Detection)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,y). 이러한 3D 표현들의 특성을 설명하며, 3D 딥러닝은 주로 **Point cloud**와 **voxel** 기반으로 발전해왔음을 이야기한다.
- **PointNet (2017):** 점군 데이터에 직접 적용되는 최초의 딥러닝 구조. 포인트는 순서가 없기 때문에, PointNet은 각 점에 동일한 MLP를 적용하여 고차원 특징을 뽑고, **대칭 함수(symmetric function)** (예: max-pooling)을 통해 점들로부터 **순서 불변 글로벌 피처**를 얻는다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=3D%20Object%20Detection)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=to%203D%20object%20detection,y). 수식으로, 입력 포인트 집합 {xi}i=1N,xi∈Rd{*xi*}*i*=1*N*,*xi*∈R*d*에 대해, 특징 추출 함수 f:Rd→Rk*f*:R*d*→R*k* (MLP)와 대칭 풀링 g(⋅)*g*(⋅) (예: max⁡imax*i*)를 사용하여 h=g({f(xi)}i=1N)*h*=*g*({*f*(*xi*)}*i*=1*N*)을 구한다. 이 h*h*가 점군 전체를 대표하는 벡터로, 이후 분류나 다른 과제용 MLP로 연결된다. PointNet은 변환 불변성 (입력 회전 등에 robust) 강화를 위해 입력에 정렬작업(T-Net)도 포함했다. **장점:** 효율적, 간단, 어떤 순서의 점에도 동일 처리. **한계:** 국소 구조 반영 부족 – 이를 보완해 PointNet++에서는 주변점들로 local feature를 추출하는 계층적 구조를 도입했다.
- **Voxel CNN:** 3D ConvNet으로 3D 격자를 직접 처리. 각 voxel에 binary occupancy나 TSDF (서페이스까지 거리) 등을 채워 3D 컨볼루션 수행. 기본적으로 3D CNN은 2D보다 차원이 늘어났을 뿐 동일하다. 예를 들어 3D LeNet 같은 구조로 작은 3D 입력(예: 323323 voxel)을 분류하는 모델을 만들 수 있다. 그러나 voxel 해상도를 높이면 parameter 폭증하므로, **sparseness 활용** 연구가 나왔다. **Octree**를 사용해 빈 공간은 거칠게, 표면 부근은 촘촘히 샘플링하는 OctNet (Riegler et al.)이나, SparseConvNet (Submanium et al.)처럼 sparse 연산만 하는 라이브러리가 개발되었다.
- **Graph/Mesh Network:** 3D mesh나 point간 국소연결을 그래프로 보고 GCN(Graph Convolutional Network)을 적용하는 접근도 있다. 예를 들어 **MeshCNN**은 mesh의 edge를 기본 단위로 convolution을 정의하거나, **GCN**으로 점들 간 kNN 그래프를 구성해 메시지를 주고받으며 특징을 학습한다. Graph convolution 수식은 hv(k+1)=σ(W⋅AGGu∈N(v)∪{v}hu(k))*hv*(*k*+1)=*σ*(*W*⋅AGG*u*∈N(*v*)∪{*v*}*hu*(*k*)) 꼴이며[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,class%20and%20their%20semantic%20relationships), 점군에서 N(v)N(*v*)는 인접 점들(kNN이나 반경 내). 이를 통해 국소 패턴(곡률 등)을 학습 가능.
- **3D 객체 인식 등 과제:** 기본은 **3D Shape Classification** (점군 또는 합성곱 통해 한 객체가 차인지 의자 인지), **3D 객체 파트 분할** (점단위로 어떤 부분인지 라벨링, 마치 2D seg과 유사), **3D 복원(reconstruction)** (이미지로부터 3D 모형 생성) 등이 있다. 자율주행에서는 **3D 객체 검출**이 중요 – LiDAR의 3D 점군에서 차량, 보행자 등의 **3D bounding box** 찾기. 이는 2D 검출과 달리 yaw, pitch, roll orientation도 예측해야 하고, 아웃풋 박스가 3D여서 더 복잡하다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=3D%20Object%20Detection)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,y). 이때 **Frustum PointNet** 처럼, 먼저 2D 검출→해당 frustum의 3D 점 추출→PointNet으로 분류/박스 회귀 하는 방법 등이 사용되었다.
- **3D Generative & beyond:** VAE 또는 GAN을 3D에 응용한 **3D-GAN** (Voxel 공간에서 학습), **PointFlow** (point 분포 학습) 등도 연구된다. 또한 3D 공간에서 **강화학습** (로봇 움직임 등)과 결합해, 에이전트가 3D 환경을 인지하고 행동하도록 하는 등 멀티모달 발전도 있다.

**응용 사례:**

- **자율주행**: LiDAR 점군 처리 (Waymo, KITTI dataset) – PointPillars (point->pseudo image), PV-RCNN 등 실제 모델 언급.
- **의료**: CT, MRI 같은 3D 이미징에 3D CNN 활용 (종양 검출 등).
- **AR/VR**: 3D pose estimation, 공간 지도화 (SLAM) 등에 딥러닝 적용.
- **3D 디자인/프린트**: GAN으로 가구 모양 생성, Part assembly 모델 등.

Hao Su (강사)의 연구인 PointNet 계열, 3D Scene Understanding 등을 중심으로 설명했을 것이다. 중요한 것은 3D에서는 **데이터 구조가 다양하고 복잡**해서, 그에 맞춘 창의적 네트워크 구조가 필요함을 이해하는 것. 학생들은 2D 지식을 확장하면서, 차원 증가가 가져오는 **연산량 증가** 문제와 **불규칙 데이터** 처리 방법론을 엿보게 된다. 이 강의는 최신 연구색이 강하므로, 하나하나 깊이보다는 개괄 소개에 집중했을 가능성이 크다.

## **Lecture 17: Deep Reinforcement Learning**

**강의 제목:** *Deep Reinforcement Learning. Policy gradients, hard attention, Q-Learning, Actor-Critic*

**핵심 개념:** 강화학습(RL)은 **시행착오를 통한 학습**으로, 에이전트가 환경과 상호작용하며 보상(reward)을 최대화하는 행동 정책(policy)를 학습한다. Deep Learning과 결합하여, 복잡한 상태의 가치나 정책을 신경망으로 표현하는 **Deep RL**이 탄생했고, 그 성과로 **Atari 게임 인간수준 플레이**, **AlphaGo** 등이 있다. 이 강의에서는 RL의 기본 개념 (상태, 행동, 보상, 가치)과 대표 기법들을 개괄한다. 특히 **값 기반(value-based) 방법**의 대표인 **Q-러닝** 및 DQN, **정책 기반(policy-based)** 방법인 **정책 경사 (Policy Gradient)**, 그리고 두 접근을 혼합한 **Actor-Critic** 방법을 소개한다. 또한 **Hard Attention**이 RL 문제로 볼 수 있다는 것을 짚으며, Vision에서의 활용 예도 논한다.

**주요 내용:**

- **Markov Decision Process (MDP):** RL 문제는 MDP로 모형화된다: 상태 s*s*, 행동 a*a*, 상태전이 확률 P(s′∣s,a)*P*(*s*′∣*s*,*a*), 보상 함수 R(s,a)*R*(*s*,*a*), 감가율 γ*γ*로 구성. 에이전트의 목표는 **누적 보상 (return)** Gt=∑k=0∞γkrt+k*Gt*=∑*k*=0∞*γkrt*+*k*의 기대값을 최대화하는 정책 π(a∣s)*π*(*a*∣*s*)를 찾는 것.
- **값 함수와 Q-러닝:** 상태 가치함수 Vπ(s)=Eπ[Gt∣st=s]*Vπ*(*s*)=E*π*[*Gt*∣*st*=*s*], 행동-가치함수 Qπ(s,a)=Eπ[Gt∣st=s,at=a]*Qπ*(*s*,*a*)=E*π*[*Gt*∣*st*=*s*,*at*=*a*]. 최적 정책 π∗*π*∗의 Q함수는 벨만 최적 방정식 Q∗(s,a)=E[r+γmax⁡a′Q∗(s′,a′)∣s,a]*Q*∗(*s*,*a*)=E[*r*+*γ*max*a*′*Q*∗(*s*′,*a*′)∣*s*,*a*]를 만족. **Q-러닝**은 이 식을 근사 iterative하게 푸는 오프폴리시 방법으로, 업데이트: Q(s,a):=Q(s,a)+α[r+γmax⁡a′Q(s′,a′)−Q(s,a)]*Q*(*s*,*a*):=*Q*(*s*,*a*)+*α*[*r*+*γ*max*a*′*Q*(*s*′,*a*′)−*Q*(*s*,*a*)]. Deep Q-Network (DQN)은 Q(s,a)*Q*(*s*,*a*)를 신경망 Q(s,a;θ)*Q*(*s*,*a*;*θ*)로 근사하고, 경험 재생(replay buffer)과 타깃 네트워크 등의 트릭으로 학습 안정화를 이뤘다[cs231n.stanford.edu](https://cs231n.stanford.edu/slides/2020/lecture_17.pdf#:~:text=Learning%20from%20batches%20of%20consecutive,inefficient%20learning). DQN (Mnih et al. 2015)은 Atari 2600 여러 게임에서 인공지능이 인간 수준을 넘어서는 것을 보여주었다. Q-러닝은 **정책을 명시적으로 저장하지 않고** Q로부터 π(s)=arg⁡max⁡aQ(s,a)*π*(*s*)=argmax*aQ*(*s*,*a*) 선택한다 (off-policy).
- **정책 경사 (Policy Gradient):** 정책을 직접 파라미터화 πθ(a∣s)*πθ*(*a*∣*s*)하고, 성능 목표 J(θ)=E[Gt]*J*(*θ*)=E[*Gt*]를 θ*θ*에 대해 극대화한다. **REINFORCE 알고리즘** (Williams 1992)은 확률적 정책의 **그라디언트 추정** 공식을 사용한다:
    
    ∇θJ=Eπ[∇θlog⁡πθ(a∣s) Gt]∇*θJ*=E*π*[∇*θ*log*πθ*(*a*∣*s*)*Gt*]
    
    직관: 에이전트가 취한 행동의 확률을, 얻은 리턴 Gt*Gt* 크게 (좋은 결과면 증가, 나쁘면 감소) 변화시킨다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,update%20its%20decision%20boundary%20to). 실제 구현에서 Gt*Gt* 대신 누적보상의 추정이나 advantage A=Gt−V(s)*A*=*Gt*−*V*(*s*) 사용, baseline(기댓값) 감산 등으로 분산을 줄인다. Policy Gradient는 on-policy이고, **Continuous action**에도 바로 적용 가능하며, 안정적이나 지역해에 수렴할 수 있다.
    
- **Actor-Critic:** 정책(Actor)과 가치 평가(Critic)를 동시에 학습하여 결합한 방법. Actor는 정책 πθ(a∣s)*πθ*(*a*∣*s*), Critic은 가치함수 Vw(s)*Vw*(*s*)나 Qw(s,a)*Qw*(*s*,*a*) 근사. Actor 업데이트는 ∇θlog⁡πθ(a∣s)(r+γVw(s′)−Vw(s))∇*θ*log*πθ*(*a*∣*s*)(*r*+*γVw*(*s*′)−*Vw*(*s*)) 꼴로 Critic이 Advantage 역할, Critic은 벨만 에러 최소화 MSE로 학습. 이를 통해 high variance의 REINFORCE 문제를 완화한다. 대표적으로 A3C(Asynchronous Advantage Actor-Critic) 등 발전된 기법들이 OpenAI Gym 등에서 좋은 성능을 보였다.
- **Hard Attention as RL:** Vision에서 **Hard Attention**이란 이미지를 한 부분씩 순차적으로 보며 최종 결정을 내리는 모델(예: Recurrent Attention Model, Mnih et al. 2014). 이 경우, 어디를 볼 지 (glimpse location) 선택이 미분 불가능한 결정이므로, REINFORCE 등 RL 기법으로 훈련한다[cs231n.stanford.edu](https://cs231n.stanford.edu/schedule.html#:~:text=CS231n%3A%20Deep%20Learning%20for%20Computer,Learning%20Model%20Learning%20Robotic%20Manipulation). 즉, glimpsing을 환경, 위치 선택을 행동, 분류 결과 보상을 주는 MDP로 만들어, 올바른 분류시 보상 +1 등으로 강화학습. 이렇게 하면 네트워크가 사람 시각처럼 중요한 부분을 골라보는 능력을 갖출 수 있다. Hard Attention은 deterministic attention(soft attention)과 달리 stochastic & non-differentiable이라 RL로 풀어야 함을 강조한다.
- **응용과 미래:** Deep RL은 **게임 AI** (Atari, AlphaGo), **로보틱스** (팔 제어, 보행), **자율주행** (운전 정책 학습) 등에 활용되고 있다. 또한 **시뮬레이션 최적화**나 **추천 시스템**에도 응용 연구가 있다. 그러나 RL의 난점은 sample efficiency (데이터 많이 필요), 안정성, 보상 설계 등이다. 강의에서는 OpenAI Five (DotA2)나 AlphaStar (StarCraft) 같은 거대 RL 성공 사례도 소개 가능. 향후 **상황이 복잡한 현실**에서 RL을 쓰기 위한 **탐험 vs 이용(exploration)** 문제, **안전한 RL** (훈련 중 위험 행동 방지) 등의 연구 방향도 언급될 수 있다.

**비전-강화 결합:** **딥 RL+비전**은 **DeepMind의 DQN**이 이미 CNN으로 화면을 상태로 받아 처리했고, 더 나아가 **ViZDoom** FPS 게임, **자율 주행 시뮬레이터** 등에서 perception과 decision을 끝까지 함께 학습하는 방향도 있다. 이는 **End-to-End** 자율 에이전트를 만드는 꿈으로 이어진다. 다만 아직은 안정성 문제로, 실제 차량에는 규칙 기반과 인지모델 혼합 접근이 쓰인다.

이 강의는 CS231n의 다른 비전 중심 강의들에 비해 RL 기본 설명이 많았을 것으로 보인다. 핵심은 **supervised vs RL의 차이** – 정답이 아니라 보상 신호로 학습, **Trial-and-error** 과정, exploration 필요성 등을 이해하는 것. Vision과 연결해 attention 문제로 RL을 소개한 것은 학생들이 RL 개념을 접하는 진입장벽을 낮췄을 것이다. 마지막으로, 수학적 깊이보다는 아이디어 이해에 초점을 맞추고, 알고리즘들은 pseudocode나 개념적으로 설명했다.

학생들은 이를 통해 **강화학습의 사고 방식**을 배울 수 있고, 스스로 게임 AI나 간단한 RL 실습을 해보고 싶어질 수 있다. (과제나 프로젝트로 CartPole balancing 혹은 Pong 게임 배우기 등을 권장 가능) CS231n 범위상 깊이보다는 맛보기지만, 최신 AI 트렌드에서 빼놓을 수 없는 주제라 강의 포함된 것으로 보인다.

## **Lecture 18: Scene Graphs**

**강의 제목:** *Scene Graphs. Visual Relationships, Graph Neural Networks*

**핵심 개념:** 장면 그래프(Scene Graph)는 이미지의 **높은 수준 구조 표현**으로, **객체(Node)**들과 **객체 간 관계(Edge)**들을 그래프 형태로 나타낸 것이다. 예를 들어 이미지에 사람이 자전거를 타고 있으면, 노드: {사람, 자전거}, 엣지: {사람 -타고있다-> 자전거}로 표현한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,class%20and%20their%20semantic%20relationships). 장면그래프는 이미지 이해를 **기호 구조**로 바꾸어, 보다 풍부한 질의응답이나 추론에 활용될 수 있다. 강의에서는 Visual Genome 등에서 정의된 scene graph 생성 문제와, 이를 풀기 위한 모델들 (객체 검출 + 관계 분류 구조, Graph Neural Network 활용 등)을 다룬다. 또한 이러한 고수준 표현이 향후 **이미지 캡션**이나 **비전-질의응답(VQA)**, **자율 로봇 환경 이해** 등에 쓰일 수 있음을 논한다.

**주요 내용:**

- **Scene Graph 정의:** 그래프 G=(V,E)로, V는 객체(보통 “명사”), E는 관계(“동사” 또는 “전치사 구”). 관계는 ⟨subject,predicate,object⟩⟨*subject*,*predicate*,*object*⟩ 삼원소(triplet)로 나타낸다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=%3E%20%20%20,). 예: <남자, 타고 있다, 자전거>, <남자, 옆에, 자동차>. 관계는 시각적이고 물리적인 것뿐 아니라, 속성(남자-노란 셔츠) 같은 것도 포함 가능. Visual Genome 데이터셋에는 이미지마다 수십 개 객체와 관계 주석이 있다.
- **Scene Graph Generation 문제:** 입력 이미지 -> 출력: 그래프로 나타낸 모든 객체+관계. 두 단계로 나눌 수 있다: (1) **객체 감지**: 바운딩박스+클래스 (Lecture 12 기술 사용), (2) **관계 예측**: 감지된 두 객체 쌍마다 관계 식별. 후자는 조합 폭발(수천 쌍) 문제가 있으므로, 모델이 **context**를 고려해 유망한 관계들만 잘 골라야 한다.
- **모델 접근:** 기본 구조는 Faster R-CNN 등의 백본으로 객체들을 잡고, 그 feature들을 입력으로 **relationship classifier**를 돌리는 것이다. Early 연구(2017)에서는 각 객체 pair의 CNN feature+object embeddings를 합쳐 fully-connected로 관계 분류했다 (예: Neural Motif Network 등). 하지만 이 방식은 이미지의 **global context**를 잘 활용 못하고, 관계들 간 종속 (모티프) 등을 놓칠 수 있다.
    - **Graph Neural Network 활용:** Xu et al. 2017, 2018 등의 **Graph R-CNN** 계열은 객체들을 노드로, 초기 예측된 관계를 엣지로 갖는 그래프를 구성하고, GNN으로 노드와 엣지 표현을 iterative refinement한다[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,class%20and%20their%20semantic%20relationships). 즉, 초기 객체 분류 결과와 박스, CNN 특성을 노드 임베딩 hi*hi*로, 노드쌍 연결 임베딩(예: concat of node feats)으로 엣지 임베딩 eij*eij* 시작 -> 메시지 패싱 통해 맥락 반영 -> 노드(객체 클래스)와 엣지(관계 클래스) 갱신. 이러한 방식은 “남자-자전거”와 “남자-자동차” 중 더 그럴듯한 관계를 판별할 때, 맥락(자동차도 주변 있다던지)을 이용할 수 있게 한다.
    - **단계적 접근:** 일부 모델은 **객체 확인 -> 각 객체의 가능한 관계 대상 제안 -> 관계 판별**의 파이프라인을 사용. 또한 predicate 빈도 등 **모티프**를 고려 (예: “on”이 가장 흔함)하는 통계기반 prior도 활용되었다.
- **Scene Graph 응용:** 생성된 그래프는 이미지에 대한 구조적 질의응답 (ex: “Who is on the bike?” -> 그래프 탐색으로 답) 등에 사용될 수 있다. 또한 **이미지 검색**에 “여자가 피아노 치는 사진”처럼 관계 있는 질의를 지원하거나[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,)[aman.ai](https://aman.ai/cs231n/detection/#:~:text=%3E%20%20%20,), **자동 주석**에서 단순 캡션보다 세밀한 정보 저장으로 활용 가능. 일부 연구는 **그래프 -> 이미지 생성**(scene graph to image)도 시도하여, 주어진 장면 그래프에 맞는 이미지를 GAN으로 합성하기도 했다.
- **도전과제:** Scene Graph 생성은 완전한 의미 이해를 요구하므로 매우 어렵다. 데이터 편향(일부 관계 치중)으로 모델이 “on”만 남발하거나, 드문 관계(“standing behind”)는 잘 못 맞추는 이슈가 있다. 평가도 어렵다: Recall@50 등의 지표 쓰나, 인간이 그래프 완전 주석하기 어렵고 주관적 차이도 있다. 강의에서는 이러한 한계도 지적하면서, scene graph가 **이미지 이해의 궁극 목표** 중 하나임을 강조할 수 있다.

**연관 주제:**

- **Vision-Language 공동 학습:** Scene Graph는 일종의 시맨틱 구조이므로, **자연어**와 접합 지점이 있다. 예컨대, 이미지 캡션을 잘 생성하려면 내재적으로 scene graph를 이해하는 게 유리하다. 일부 연구는 캡션/QA 모델 내부에 그래프 추론 모듈을 두기도 한다.
- **Graph Neural Networks 일반:** 이 주제가 GNN 맛보기이기도 해서, image 이외 **과학분야**(social network, molecules)에도 GNN이 쓰임을 잠깐 소개할 수도 있다. 다만 초점은 시각 관계에 맞춰짐.

강의자 Hao Su는 3D GN도 했지만 scene graph는 Stanford Fei-Fei Li 그룹(Visual Genome: Ranjay Krishna 등) 작업이라, 게스트였을지. 어쨌든 이 마지막 강의로 **컴퓨터 비전 10년간의 확장** (2D -> 3D -> 비전+언어 -> 그래프 추론)을 훑으며, 학생들에게 연구 프론티어를 보여줬을 것이다.

마무리로, scene graph를 포함한 **구조적 예측**이 비전의 다음 과제라고 강조하며 코스를 끝맺었을 것으로 예상된다. Also mention current 2025 context: Graph Transformers, CLIP-like models unify modalities – but those might be beyond scope.

**참고 슬라이드/문헌:** Visual Genome paper, Xu et al. (2017) Scene Graph Generation by Iterative Message Passing[aman.ai](https://aman.ai/cs231n/detection/#:~:text=,class%20and%20their%20semantic%20relationships) 등이 소개되었을 것. 학생들에게 “이제 여러분도 이 영역 연구에 기여할 수 있다”는 격려와 함께, CS231n 여정을 마쳤을 것이다.