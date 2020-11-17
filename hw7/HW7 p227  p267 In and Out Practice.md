20171664 소프트웨어학부 이범석



# HW7 p227 ~ p267 In and Out Practice



## 실습 결과

1. 30개의 무게 데이터 X와 성별 T를 생성했습니다.

   ![image-20200604013626057](/home/leebumseok/.config/Typora/typora-user-images/image-20200604013626057.png)

2. 작성한 데이터를 표시했습니다.

   ![image-20200604013712100](/home/leebumseok/.config/Typora/typora-user-images/image-20200604013712100.png)

3. 로지스틱 회귀 모델을 정의했습니다.

   ![image-20200604013743155](/home/leebumseok/.config/Typora/typora-user-images/image-20200604013743155.png)

4. 로지스틱 회귀 모델의 결정 경계와 값을 출력했습니다.

   ![image-20200604013837458](/home/leebumseok/.config/Typora/typora-user-images/image-20200604013837458.png)

5. 평균 교차 엔트로피 오차를 계산하는 함수를 정의했습니다.

   ![image-20200604013906650](/home/leebumseok/.config/Typora/typora-user-images/image-20200604013906650.png)

6. 평균 교차 엔트로피 오차의 모양을 확인했습니다.

   ![image-20200604014123436](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014123436.png)

7. 평균 교차 엔트로피 오차의 미분을 구현했습니다.

   ![image-20200604014204980](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014204980.png)

8. 경사 하강법으로 로지스틱 회귀 모델의 매개 변수를 찾았습니다.

   ![image-20200604014248562](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014248562.png)

9. 데이터를 재설정했습니다.

   ![image-20200604014327606](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014327606.png)

10. 2클래스의 분류와 3클래스의 분류 데이터를 함께 만들었습니다.

    ![image-20200604014522790](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014522790.png)

11. 입력 데이터 X의 첫 5개를 출력했습니다.

    ![image-20200604014602454](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014602454.png)

12. 클래스 데이터 T2의 처음 5개를 출력했습니다.

    ![image-20200604014631120](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014631120.png)

13. 클래스 데이터 T3의 처음 5개를 출력했습니다.

    ![image-20200604014700759](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014700759.png)

14. T2와 T3를 그림으로 표시했습니다.

    ![image-20200604014820347](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014820347.png)

15. 로지스틱 회귀 모델을 정의했습니다.

    ![image-20200604014855548](/home/leebumseok/.config/Typora/typora-user-images/image-20200604014855548.png)

16. 2차원 로지스틱 회귀 모델과 데이터를 3D로 표시했습니다.

    ![image-20200604015048680](/home/leebumseok/.config/Typora/typora-user-images/image-20200604015048680.png)

17. 로지스틱 회귀 모델을 등고선으로 출력했습니다.

    ![image-20200604021234119](/home/leebumseok/.config/Typora/typora-user-images/image-20200604021234119.png)

18. 상호 엔트로피 오차를 계산하는 함수를 정의했습니다.

    ![image-20200604021317655](/home/leebumseok/.config/Typora/typora-user-images/image-20200604021317655.png)

19. 편미분을 계산하는 함수를 정의하고 실행했습니다.

    ![image-20200604024028722](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024028722.png)

20. 평균 교차 엔트로피 오차가 최소가 되도록 로지스틱 회귀 모델의 매개 변수를 구한 후 결과를 표시했습니다.

    ![image-20200604024108837](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024108837.png)

21. 3클래스용 로지스틱 회귀 모델을 구현했습니다.

    ![image-20200604024141397](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024141397.png)

22. 교차 엔트로피 오차를 계산하는 함수를 정의했습니다.

    ![image-20200604024218424](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024218424.png)

23. 각 매개 변수에 대한 미분값을 출력하는 함수를 정의했습니다.

    ![image-20200604024345343](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024345343.png)

24. 매개 변수 검색을 수행하는 함수를 만들었습니다.

    ![image-20200604024513866](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024513866.png)

25. 등고선에 결과를 표시하는 함수를 만들었습니다.

    ![image-20200604024539992](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024539992.png)

26. 데이터들을 피팅했습니다.

    ![image-20200604024631722](/home/leebumseok/.config/Typora/typora-user-images/image-20200604024631722.png)

------

로지스틱 회귀 모델을 구현해보며 직선으로 구성된 경계선의 조합을 보았습니다.

모호성을 조건부 확률로 근사하니 오차가 줄어들고 정답과 비슷한 값의 확률이 높아서 좋은 모델인 것 같습니다.

------

이범석

국민대학교 소프트웨어학부, 20171664

Mobile 010-6401-6042

qpwoeiru6486@gmail.com

ijkoo16@kookmin.ac.kr