#### 20171664 소프트웨어학부 이범석



# HW8 p269 ~ p321 In and Out Practice



## 실습 결과

1. 3클래스 분류 데이터와 동일한 데이터를 만들었습니다.

   ![image-20200609173507690](/home/leebumseok/.config/Typora/typora-user-images/image-20200609173507690.png)

2. 데이터를 훈련 데이터와 테스트 데이터로 나누고 데이터를 저장했습니다.

   ![image-20200609173601282](/home/leebumseok/.config/Typora/typora-user-images/image-20200609173601282.png)

3. 분할한 데이터를 출력했습니다.

   ![image-20200609173920091](/home/leebumseok/.config/Typora/typora-user-images/image-20200609173920091.png)

4. 시그모이드 함수를 정의하고 네트워크 프로그램을 작성해 중간층과 출력층의 정보를 출력했습니다.

   ![image-20200609174108776](/home/leebumseok/.config/Typora/typora-user-images/image-20200609174108776.png)

5. 평균 교차 엔트로피 오차를 구현했습니다.

   ![image-20200609174226758](/home/leebumseok/.config/Typora/typora-user-images/image-20200609174226758.png)

6. 평균 교차 엔트로피 오차 함수의 수치 미분을 출력하는 함수를 만들고 출력했습니다.

   ![image-20200609174425834](/home/leebumseok/.config/Typora/typora-user-images/image-20200609174425834.png)

7. 수치 미분을 사용한 경사 하강법 함수를 구현하고 실행 시간을 표현했습니다.

   ![image-20200609194640783](/home/leebumseok/.config/Typora/typora-user-images/image-20200609194640783.png)

8. 오차 역전파법으로 구한 데이터를 그림으로 표현했습니다.

   ![image-20200609195434782](/home/leebumseok/.config/Typora/typora-user-images/image-20200609195434782.png)

9. 가중치의 시간 변화를 그림으로 표현했습니다.

   ![image-20200609195509587](/home/leebumseok/.config/Typora/typora-user-images/image-20200609195509587.png)

10. 수치 미분법에 의한 경사 하강법에서 얻은 클래스 간의 경계선을 그림으로 표현했습니다.

    ![image-20200609195650345](/home/leebumseok/.config/Typora/typora-user-images/image-20200609195650345.png)

11. 오차 역전파법으로 ![CodeCogsEqn](/home/leebumseok/Downloads/CodeCogsEqn.gif)와 ![CodeCogsEqn (1)](/home/leebumseok/Downloads/CodeCogsEqn (1).gif)를 구하는 프로그램을 만들고 그림으로 표현했습니다.

    ![image-20200609195837115](/home/leebumseok/.config/Typora/typora-user-images/image-20200609195837115.png)

12. 수치 미분으로 풀었던 분류 문제를 오차 역전파법으로 풀었습니다.

    수치 미분에 비해 훨씬 적은 실행 시간을 보였습니다.

    ![image-20200609204601263](/home/leebumseok/.config/Typora/typora-user-images/image-20200609204601263.png)

13. 해석적 미분을 사용한 오차 역전파법의 실행 결과를 그림으로 표현했습니다.

    수치 미분과 거의 같은 결과를 얻었습니다.

    ![image-20200609204704413](/home/leebumseok/.config/Typora/typora-user-images/image-20200609204704413.png)

14. 각 뉴런의 특성을 그림으로 표현했습니다.

    x0, x1의 쌍이 입력된 경우는 각 변수의 값을 나타냈습니다.

    중간측 입력 총합은 선형의 합이므로 입출력 맵은 평면입니다.

    ![image-20200609204840079](/home/leebumseok/.config/Typora/typora-user-images/image-20200609204840079.png)

15. 메모리를 초기화했습니다.

    ![image-20200609205015677](/home/leebumseok/.config/Typora/typora-user-images/image-20200609205015677.png)

16. 필요한 라이브러리를 import하고, 저장된 데이터를 불러왔습니다.

    ![image-20200609205052811](/home/leebumseok/.config/Typora/typora-user-images/image-20200609205052811.png)

17. 데이터를 그림으로 그리하는 함수를 재정의했습니다.

    ![image-20200609205135197](/home/leebumseok/.config/Typora/typora-user-images/image-20200609205135197.png)

18. 케라스를 사용하여 2층 피드백 신경망 모델을 만들고 학습시켰습니다.

    ![image-20200609205211808](/home/leebumseok/.config/Typora/typora-user-images/image-20200609205211808.png)

19. 케라스 사용의 흐름의 과정과 그 결과를 그래프로 표시했습니다.

    ![image-20200609205353456](/home/leebumseok/.config/Typora/typora-user-images/image-20200609205353456.png)

------



## 수행 소감

신경망 프로그램 구현과 라이브러리 이용으로 데이터 학습을 할 수 있다는 사실 자체로 학습 효과가 있었습니다.

더 복잡한 프로그램을 구현할 때는 효과적으로 원하는 근사 데이터를 얻을 수 있을 것 같습니다.

------

이범석

국민대학교 소프트웨어학부, 20171664

Mobile 010-6401-6042

qpwoeiru6486@gmail.com

ijkoo16@kookmin.ac.kr