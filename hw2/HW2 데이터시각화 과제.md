20171664 소프트웨어학부 이범석



# HW2 데이터시각화 과제



## 실습 결과

1. mpl, plt, np를 각각 import 했습니다.

   ![image-20200327172444593](/home/leebumseok/.config/Typora/typora-user-images/image-20200327172444593.png)

2. magic 명령을 이용하여 그림을 notebook에 표시하도록 지정했습니다.

   ![image-20200327172608742](/home/leebumseok/.config/Typora/typora-user-images/image-20200327172608742.png)

3. 변하는 값을 plot 명령에 데이터 리스트로 넣어 주었습니다.

   이 때, x 값은 자동으로 0, 1, 2, 3 으로 설정되었습니다.

   ![image-20200327173143191](/home/leebumseok/.config/Typora/typora-user-images/image-20200327173143191.png)

4. x 값의 위치를 명시하기 위해 x의 리스트, y의 리스트를 plot 명령에 넣어 주었습니다.

   x 값이 변함에 따라 y의 값이 변하는 그래프를 시각화하게 되었습니다.

   ![image-20200327173330057](/home/leebumseok/.config/Typora/typora-user-images/image-20200327173330057.png)

5. 폰트를 설치하고 폰트 목록을 확인했습니다.

   ![image-20200327173500110](/home/leebumseok/.config/Typora/typora-user-images/image-20200327173500110.png)

6. rc parameter를 이용하여 이후에 그릴 그림 전체에 폰트를 적용했습니다.

   ![image-20200327173627762](/home/leebumseok/.config/Typora/typora-user-images/image-20200327173627762.png)

7. 한글이 정상적으로 설치된 모습입니다.

   ![image-20200327173802160](/home/leebumseok/.config/Typora/typora-user-images/image-20200327173802160.png)

   8. 폰트, 색상, 크기를 각자 지정하여 fontdict 안에 넣고 그래프를 출력한 모습입니다.

   ![image-20200327173734798](/home/leebumseok/.config/Typora/typora-user-images/image-20200327173734798.png)

9. 그래프의 스타일을 달리한 모습입니다.

   ![image-20200327174906215](/home/leebumseok/.config/Typora/typora-user-images/image-20200327174906215.png)

10. 또 다른 스타일의 그래프 모습입니다.

    ![image-20200327174948488](/home/leebumseok/.config/Typora/typora-user-images/image-20200327174948488.png)

11. xlim, ylim 명령으로 x축과 y축의 최대, 최솟값을 지정해준 모습입니다.

    ![image-20200327175041991](/home/leebumseok/.config/Typora/typora-user-images/image-20200327175041991.png)

12. tick label 을 지정해준 모습입니다.

    ![image-20200327175213852](/home/leebumseok/.config/Typora/typora-user-images/image-20200327175213852.png)

13. laTeX 문자열($$)로 pi 문자를 그래프에 적용시킨 모습입니다.

    ![image-20200327175307178](/home/leebumseok/.config/Typora/typora-user-images/image-20200327175307178.png)

14. default 그래프에 Grid 선이 없었지만 plt.grid(False) 명령을 통해 Grid 선을 제거한 모습입니다.

    ![image-20200327175536240](/home/leebumseok/.config/Typora/typora-user-images/image-20200327175536240.png)

15. x, y, 스타일 데이터를 plot 명령에 여러 개를 넘겨서 여러 개의 선을 한 개의 그래프에 그렸습니다.

    ![image-20200327180219312](/home/leebumseok/.config/Typora/typora-user-images/image-20200327180219312.png)

16. 여러 개의 plot 명령을 한 그래프에 표현했습니다.

    ![image-20200327180400603](/home/leebumseok/.config/Typora/typora-user-images/image-20200327180400603.png)

17. plt.legend 명령을 통해 인수 목록을 표시해 주었습니다.

    ![image-20200327180521886](/home/leebumseok/.config/Typora/typora-user-images/image-20200327180521886.png)

18. x축과 y축의 위치에 각각 label을 붙이고, 플롯의 위에 제목을 붙였습니다.

    ![image-20200328232635498](/home/leebumseok/.config/Typora/typora-user-images/image-20200328232635498.png)

19. figure 명령과 figsize 인수를 사용해 그림의 크기를 정하고 그래프를 그렸습니다.

    ![image-20200328232823133](/home/leebumseok/.config/Typora/typora-user-images/image-20200328232823133.png)

20. gcf 명령을 사용하여 현재 figure 객체를 가져왔습니다.

    ![image-20200328233256887](/home/leebumseok/.config/Typora/typora-user-images/image-20200328233256887.png)

21. subplot 명령을 사용하여 figure 안에 두 개의 axes 객체들을 생성했습니다.

    그리고 tight_layout 명령을 실행하여 플롯간의 간격도 맞춰줬습니다.

    ![image-20200328233633639](/home/leebumseok/.config/Typora/typora-user-images/image-20200328233633639.png)

    22. subplot의 인수를 하나의 숫자를 줄이고, axes를 4개 생성했습니다.

        ![image-20200328233750001](/home/leebumseok/.config/Typora/typora-user-images/image-20200328233750001.png)

23. subplots 명령을 이용하여 간단하게 2x2개의 axes 객체를 동시에 생성했습니다.

    2차원 ndarray 형태로 axes들이 반환되었습니다.

    ![image-20200328233954641](/home/leebumseok/.config/Typora/typora-user-images/image-20200328233954641.png)

24. twinx 명령을 이용하여 복수의 y축을 가진 플롯을 만들었습니다.

    ![image-20200328234104935](/home/leebumseok/.config/Typora/typora-user-images/image-20200328234104935.png)

------

이번 과제를 하며 함수들이 주어지지 않았다면 결코 쉽지 않았을 것이라고 생각했습니다.

그리고 수학과 컴퓨터가 밀접한 관계에 있다는 생각 또한 하게 되었고, 노력하겠습니다.



------

이범석

국민대학교 소프트웨어학부, 20171664

Mobile 010-6401-6042

qpwoeiru6486@gmail.com

ijkoo16@kookmin.ac.kr