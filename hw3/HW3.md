20171664 소프트웨어학부 이범석



# HW3 p57 ~ p90 In and Out Practice



## 실습 결과

1. enumerate를 이용하여 list num의 값들에 2를 곱한 리스트를 출력했습니다.

   ![image-20200414003015728](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003015728.png)

2. list 형이 벡터로 처리되는지 확인했습니다.

   벡터로 처리되는 것이 아닌 str형 + 연산자로 처리되어 연결됩니다.

   ![image-20200414003155436](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003155436.png)

3. 넘파이 라이브러리를 import 했습니다.

   ![image-20200414003452920](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003452920.png)

4. list 형으로 정의된 np.array를 x에 저장하고 x를 출력했습니다.

   ![image-20200414003637788](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003637788.png)

5. print(x) 를 통해 깔끔하게 x를 출력했습니다.

   ![image-20200414003710092](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003710092.png)

6. np.array로 처리한 변수들은 벡터로 처리되어 요소들이 더해집니다.

   ![image-20200414003755074](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003755074.png)

7. type(x)를 통해 x의 type을 확인했습니다.

   ![image-20200414003828548](/home/leebumseok/.config/Typora/typora-user-images/image-20200414003828548.png)

8. 요소 참조는 파이썬의 list와 동일했습니다.

   ![image-20200414004113325](/home/leebumseok/.config/Typora/typora-user-images/image-20200414004113325.png)

9. 요소 수정을 해 주었습니다.

   ![image-20200414004207558](/home/leebumseok/.config/Typora/typora-user-images/image-20200414004207558.png)

10. 연속된 정수 벡터를 생성해 주었습니다.

    ![image-20200414004301805](/home/leebumseok/.config/Typora/typora-user-images/image-20200414004301805.png)

11. arange 안에 범위를 지정하고 지정한 범위의 배열을 만들었습니다.

    ![image-20200414004438331](/home/leebumseok/.config/Typora/typora-user-images/image-20200414004438331.png)

12. ndarray 함수에서 요소를 수정했습니다.

    copy를 하지 않고 b의 요소를 수정한 결과 a[0]과 b[0] 이 같은 값으로 변했습니다.

    ![image-20200414004618153](/home/leebumseok/.config/Typora/typora-user-images/image-20200414004618153.png)

13. copy를 사용하여 b를 a와 다른 독립된 변수로 취급한 후 b[0]의 값만 바꿔 주었습니다.

    ![image-20200414004808126](/home/leebumseok/.config/Typora/typora-user-images/image-20200414004808126.png)

14. ndarray의 2차원 배열을 정의했습니다.

    ![image-20200414005327956](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005327956.png)

15. shape 명령으로 행렬의 크기를 출력했습니다.

    ![image-20200414005411543](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005411543.png)

16. w, h 변수에 행렬의 각 크기를 저장해 주었습니다.

    ![image-20200414005528151](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005528151.png)

17. 각 차원을 ',' 로 구분하여 요소를 참조했습니다.

    ![image-20200414005621865](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005621865.png)

18. 요소를 참조하고 해당 요소를 수정했습니다.

    ![image-20200414005718027](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005718027.png)

19. zeros 함수를 이용하여 길이가 10고 모든 요소가 0인 벡터를 생성했습니다.

    ![image-20200414005813560](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005813560.png)

20. 2 x 10 크기의 모든 요소가 0인 행렬을 생성했습니다.

    ![image-20200414005912043](/home/leebumseok/.config/Typora/typora-user-images/image-20200414005912043.png)

21. 2 x 10 크기의 모든 요소가 1인 행렬을 생성했습니다.

    ![image-20200414010407963](/home/leebumseok/.config/Typora/typora-user-images/image-20200414010407963.png)

22. 임의의 요소로 이루어진 행렬을 생성했습니다.

    ![image-20200414010512419](/home/leebumseok/.config/Typora/typora-user-images/image-20200414010512419.png)

23. 연속된 정수 벡터를 생성해 주었습니다.

    ![image-20200414010616356](/home/leebumseok/.config/Typora/typora-user-images/image-20200414010616356.png)

24. reshape를 사용하여 벡터를 행렬로 바꾸었습니다.

    ![image-20200414010651706](/home/leebumseok/.config/Typora/typora-user-images/image-20200414010651706.png)

25. 요소끼리 사칙연산이 되는지 확인했습니다.

    ![image-20200414010749673](/home/leebumseok/.config/Typora/typora-user-images/image-20200414010749673.png)

26. 스칼라를 행렬에 곱했습니다.

    ![image-20200414010858593](/home/leebumseok/.config/Typora/typora-user-images/image-20200414010858593.png)

27. exp 함수를 모든 요소에 적용시켰습니다.

    ![image-20200414011000950](/home/leebumseok/.config/Typora/typora-user-images/image-20200414011000950.png)

28. dot을 이용하여 요소별로 계산하지 않는 행렬을 곱해줬습니다.

    ![image-20200414011157230](/home/leebumseok/.config/Typora/typora-user-images/image-20200414011157230.png)

29. 해당 숫자까지 벡터를 슬라이싱했습니다.

    ![image-20200414012008019](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012008019.png)

30. 해당 숫자에서 마지막 요소까지 슬라이싱해서 출력했습니다.

    ![image-20200414012100587](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012100587.png) 

31. 3번 인덱스에서 7번 인덱스까지 출력했습니다.

    ![image-20200414012157002](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012157002.png)

32. 3번 인덱스에서 7번 인덱스까지 2의 간격으로 출력했습니다.

    ![image-20200414012225881](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012225881.png)

33. 배열의 순서를 반대로 바꿨습니다.

    ![image-20200414012338837](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012338837.png)

34. 1차원 이상의 배열도 슬라이싱해 보았습니다.

    ![image-20200414012437368](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012437368.png)

35. bool 형식의 배열을 반환했습니다.

    ![image-20200414012902845](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012902845.png)

36. bool 배열의 요소를 참조하여 true인 요소만 출력했습니다.

    ![image-20200414012943504](/home/leebumseok/.config/Typora/typora-user-images/image-20200414012943504.png)

37. 조건을 충족하는 요소만 바꾸었습니다.

    ![image-20200414013033894](/home/leebumseok/.config/Typora/typora-user-images/image-20200414013033894.png)

38. help를 사용하여 함수의 사용법을 출력해 보았습니다.

    ![image-20200414013537222](/home/leebumseok/.config/Typora/typora-user-images/image-20200414013537222.png)

39. Hi를 출력하는 함수를 만들고 실행했습니다.

    ![image-20200414013629268](/home/leebumseok/.config/Typora/typora-user-images/image-20200414013629268.png)

40. a, b를 받아 더한 값을 c에 저장하고 return해주는 함수를 만들고, 실행했습니다.

    ![image-20200414013715817](/home/leebumseok/.config/Typora/typora-user-images/image-20200414013715817.png)

41. D를 입력받아 1차원ndarray 형으로 함수에 전달하고, 평균값과 표준편차를 출력하는 함수를 만들었습니다.

    ![image-20200414013820318](/home/leebumseok/.config/Typora/typora-user-images/image-20200414013820318.png)

42. 변수에 각각 평균값과 표준편차를 넣어 주고 형식에 맞게 출력해 주었습니다.

    ![image-20200414014223955](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014223955.png)

43. 하나의 변수에 두 개의 반환값을 tuple 형으로 받고 출력했습니다.

    ![image-20200414014325495](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014325495.png)

44. 하나의 ndarray 형을 save를 이용하여 파일에 저장하고, load 를 이용하여 읽어왔습니다.

    ![image-20200414014428048](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014428048.png)

45. savez를 이용하여 여러 ndarray 형을 저장했습니다.

    ![image-20200414014525295](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014525295.png)

46. 임의의 그래프를 출력했습니다.

    ![image-20200414014632493](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014632493.png)

47. 정한 리스트 번호의 규칙 이력을 삭제했습니다.

    ![image-20200414014834876](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014834876.png)

48. 함수 f(x)를 정의했습니다.

    ![image-20200414014921220](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014921220.png)

49. x에 숫자를 넣고, 대응하는 값을 출력했습니다.

    ![image-20200414014950929](/home/leebumseok/.config/Typora/typora-user-images/image-20200414014950929.png)

50. ndarray 배열 각각에 대응한 f를 ndarray로 반환받았습니다.

    ![image-20200414015049798](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015049798.png)

51. x의 범위와 간격을 정의했습니다.

    ![image-20200414015219365](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015219365.png)

52. x의 범위를 linspace를 이용해 일정 간격으로 구간을 나눈 값을 출력했습니다.

    ![image-20200414015356198](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015356198.png)

53. x의 값으로 그래프를 출력했습니다.

    ![image-20200414015421977](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015421977.png)

54. 구간을 세밀하게 나눠 매끄러운 그래프를 출력하고, 그리드, 라벨, 제목, 범례를 같이 출력했습니다.

    ![image-20200414015533582](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015533582.png)

55. 사용할 수 있는 색상들을 출력했습니다.

    ![image-20200414015741988](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015741988.png)

56. subplot을 이용하여 여러 그래프를 출력했습니다.

    ![image-20200414015843023](/home/leebumseok/.config/Typora/typora-user-images/image-20200414015843023.png)

57. f3을 정의하고 x0, x1값에 대한 f3의 값을 계산했습니다.

    ![image-20200414020001411](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020001411.png)

58. xn이 9이므로 x0은 9개의 요소를 가지고 있습니다.

    ![image-20200414020042835](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020042835.png)

59. 해당 자리수의 소수값까지 round를 이용하여 반올림해주었습니다.

    ![image-20200414020135926](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020135926.png)

60. 2차원 행렬의 요소를 색상으로 표현했습니다.

    ![image-20200414020210713](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020210713.png)

61. 3차원의 입체 그래프로 출력했습니다.

    ![image-20200414020259693](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020259693.png)

62. x0, x1의 내용을 확인했습니다.

    ![image-20200414020346577](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020346577.png)

63. meshgrid 명령으로 2차원 배열을 생성했습니다.

    ![image-20200414020413435](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020413435.png)

64. x1도 2차원 배열이 되었습니다.

    ![image-20200414020454520](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020454520.png)

65. 함수의 높이를 등고선 플롯으로 출력했습니다.

    ![image-20200414020530513](/home/leebumseok/.config/Typora/typora-user-images/image-20200414020530513.png)

------



배열을 이용하여 그래프를 효과적으로 그리는 방법을 알게 되었습니다.

직관적이고 명확한 그래프가 나오는 것 같습니다.



------

이범석

국민대학교 소프트웨어학부, 20171664

Mobile 010-6401-6042

qpwoeiru6486@gmail.com

ijkoo16@kookmin.ac.kr