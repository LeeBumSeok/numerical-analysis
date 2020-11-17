#### 20171664 소프트웨어학부 이범석



# HW6 p167 ~ p225 In and Out Practice



## 실습 결과

1. numpy와 matplotlib을 import했습니다.

   또한 나이와 몸무게의 인공 데이터를 생성했습니다.

   ![image-20200527100211447](/home/leebumseok/.config/Typora/typora-user-images/image-20200527100211447.png)

2. X의 내용(나이)을 표시했습니다.

   ![image-20200527100330231](/home/leebumseok/.config/Typora/typora-user-images/image-20200527100330231.png)

3. np.round 함수를 사용해 소수점 이하 표시를 반올림하였습니다.

   ![image-20200527100406513](/home/leebumseok/.config/Typora/typora-user-images/image-20200527100406513.png)

4. T의 내용(키)도 확인하였습니다.

   ![image-20200527100448569](/home/leebumseok/.config/Typora/typora-user-images/image-20200527100448569.png)

5. X와 T를 그래프로 표시하였습니다.

   ![image-20200527100547874](/home/leebumseok/.config/Typora/typora-user-images/image-20200527100547874.png)

6. 기울기를 나타내는 w0과 절편을 나타내는 w1의 값을 결정하고 평균 제곱 오차 J를 계산한 그래프를 나타냈습니다.

   ![image-20200527102228925](/home/leebumseok/.config/Typora/typora-user-images/image-20200527102228925.png)

7. 인수 데이터를 전달하여 기울기를 반환하는 함수를 만들었습니다.

   ![image-20200527102424653](/home/leebumseok/.config/Typora/typora-user-images/image-20200527102424653.png)

8. w = [10, 165] 의 기울기를 구해보았습니다.

   ![image-20200527105031233](/home/leebumseok/.config/Typora/typora-user-images/image-20200527105031233.png)

9. 경사 하강법의 함수를 구현하고, 기울기의 각 요소의 절댓값이 eps = 0.1보다 작을 때까지 구현하고,

   마지막으로 얻어진 w값을 표시하고, w의 갱신 내역을 그래프로 표현했습니다.

   ![image-20200527105908088](/home/leebumseok/.config/Typora/typora-user-images/image-20200527105908088.png)

10. 구한 W0과 W1의 값을 직선 식에 대입하여 데이터 분포에 겹쳐서 그려 보았습니다.

    ![image-20200527110006797](/home/leebumseok/.config/Typora/typora-user-images/image-20200527110006797.png)

11. 입력 데이터 X와 목표 데이터 T의 값을 식에 넣어 w(해석해)를 찾았습니다.

    경사 하강법과 근사한 결과가 얻어졌습니다.

    ![image-20200527110338417](/home/leebumseok/.config/Typora/typora-user-images/image-20200527110338417.png)

12. 몸무게는 키의 제곱에 비례한다는 식을 만들었습니다.

    원래 나이 x를 x0, 몸무게의 데이터를 X1로 추가했습니다.

    ![image-20200527111051262](/home/leebumseok/.config/Typora/typora-user-images/image-20200527111051262.png)

13. 데이터를 표시했습니다.

    ![image-20200527111355677](/home/leebumseok/.config/Typora/typora-user-images/image-20200527111355677.png)

14. 16명의 X0, X1, T를 3차원 플롯 그래프로 표시했습니다.

    ![image-20200527111448748](/home/leebumseok/.config/Typora/typora-user-images/image-20200527111448748.png)

15. 임의의 w에 대해 면을 그리는 함수와 평균 제곱 오차를 계산하는 함수를 만들었습니다.

    그리고 면의 함수를 3차원으로 나타냈습니다.

    ![image-20200527113237424](/home/leebumseok/.config/Typora/typora-user-images/image-20200527113237424.png)

    16. 해석해에 의한 평면 모델의 피팅 결과를 나타냈습니다.

        ![image-20200527113432030](/home/leebumseok/.config/Typora/typora-user-images/image-20200527113432030.png)

17. 위에서 작성한 데이터를 로드했습니다.

    ![image-20200527114213282](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114213282.png)

18. 가우스 함수를 정의했습니다.

    ![image-20200527114238145](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114238145.png)

19. 4개의 가우스 함우를 나이의 범위 5~30으로 정하고 이를 나타냈습니다.

    ![image-20200527114412814](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114412814.png)

20. 선형 기저 함수 모델을 정의했습니다.

    ![image-20200527114449703](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114449703.png)

21. 평균 제곱 오차를 계산하는 함수를 만들었습니다. 이는 피팅의 수준을 산출합니다.

    ![image-20200527114617472](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114617472.png)

22. 선형 기저 함수 모형의 매개 변수의 해석해를 제공하는 함수를 만들었습니다.

    ![image-20200527114900448](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114900448.png)

23. 선형 기저 함수 모델의 피팅 결과를 나타냈습니다.

    ![image-20200527114933608](/home/leebumseok/.config/Typora/typora-user-images/image-20200527114933608.png)

24. M을 늘리며 표준 편차를 줄여보았지만 가우스 기저 함수가 변했습니다.

    과적합이 일어났습니다.

    ![image-20200527115304585](/home/leebumseok/.config/Typora/typora-user-images/image-20200527115304585.png)

25. M이 2일때부터 9까지의 표준 편차를 계산하고 그래프로 나타냈습니다.

    M이 증가함에 따라 표준 편차는 감소했습니다. 하지만 이는 최적의 M의 기준으로는 볼 수 없습니다.

    ![image-20200527115446501](/home/leebumseok/.config/Typora/typora-user-images/image-20200527115446501.png)

26. 최적의 M을 찾기 위하여 X와 t의 1/4을 테스트 데이터로, 나머지 3/4를 훈련 데이터로 나누고,

    w는 훈련 데이터만을 사용하여 최적화합니다. 훈련 데이터의 평균 제곱 오차를 최소화하도록 w를 선택합니다.

    w를 사용하여 테스트 데이터의 평균 제곱 오차를 계산하고, M의 평가 기준으로 삼습니다.

    이처럼 훈련에 이용하지 않은 미지의 데이터에 대한 예측 오차로 M을 평가하는 것을 홀드 아웃 검증이라고 합니다.

    이 데이터에 대한 그래프를 표현했습니다.

    ![image-20200527115948270](/home/leebumseok/.config/Typora/typora-user-images/image-20200527115948270.png)

27. 훈련 데이터와 데스트 데이터의 오차를 그래프로 나타냈습니다.

    M = 4의 경우가 데이터에 가장 적합하다는 결론이 나왔습니다.

    ![image-20200527120058689](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120058689.png)

28. 데이터를 K 분할하여 각각의 평균 제곱 오차를 출력하는 함수를 만들었습니다.

    ![image-20200527120206496](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120206496.png)

29. n을 k로 나눈 나머지를 출력하는 함수의 결과를 출력했습니다.

    ![image-20200527120353651](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120353651.png)

30. 기저 수 M = 4, 분할 수 K = 4 로 함수를 실행해 보았습니다.

    ![image-20200527120440094](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120440094.png)

31. 분할 수를 16으로 하고, 2에서 7까지의 M의 오차 평균을 계산하여 그래프로 나타냈습니다.

    M이 3일 때 테스트 데이터의 오차가 가장 작은 것을 알 수 있었습니다.

    ![image-20200527120556217](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120556217.png)

32. M = 3이 최적이므로 해당 결과를 대입하고, w의 모든 데이터를 사용해 계산했습니다.

    ![image-20200527120722128](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120722128.png)

33. 새로운 모델 A를 정의하고, 표시용 함수와 MSE 출력 함수를 정의했습니다.

    ![image-20200527120905607](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120905607.png)

34. 매개 변수의 최적화 함수를 만들었습니다.

    ![image-20200527120946040](/home/leebumseok/.config/Typora/typora-user-images/image-20200527120946040.png)

35. 최적화 함수를 움직여 보았습니다.

    오차의 표준 편차가 직선 모델과 선형 기저 함수 모델보다 훨씬 낮아졌습니다.

    ![image-20200527121122449](/home/leebumseok/.config/Typora/typora-user-images/image-20200527121122449.png)

36. 선형 기저 함수 모델과 모델 A의 LOOCV를 실시하여 비교한 그래프를 나타냈습니다.

    모델 A가 데이터에 잘 어울린다고 생각할 수 있습니다.

    ![image-20200527121339903](/home/leebumseok/.config/Typora/typora-user-images/image-20200527121339903.png)

------



## 수행 소감

수많은 트러블슈팅을 통해 최적화된 모델을 구현하는 방법이 여러 가지라는 것을 알게 되었습니다.

수많은 데이터들을 효율적으로 해석할 수 있는 방법이었다고 생각합니다.



긴 글 읽어 주셔서 감사합니다.



------

이범석

국민대학교 소프트웨어학부, 20171664

Mobile 010-6401-6042

qpwoeiru6486@gmail.com

ijkoo16@kookmin.ac.kr