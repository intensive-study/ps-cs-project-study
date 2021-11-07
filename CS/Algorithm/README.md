# Algorithm
![time_complexity](https://lamfo-unb.github.io/img/Sorting-algorithms/Complexity.png)
## 정렬
### 거품 정렬 (Stable)
![거품 정렬](https://gmlwjd9405.github.io/images/algorithm-bubble-sort/bubble-sort.png)
- 장점
  - 간단한 구현
  - ~~경우에 따라 한번만 스왑하고 끝낼수 있음 ex) [2, 1, 3, 4, 5] - optimized version 적용시~~

- 단점
  - 순서에 맞지 않은 요소를 인접한 요소와 교환한다.
  - 하나의 요소가 가장 왼쪽에서 가장 오른쪽으로 이동하기 위해서는 배열에서 모든 다른 요소들과 교환되어야 한다.
  - 특히 특정 요소가 최종 정렬 위치에 이미 있는 경우라도 교환되는 일이 일어난다.
- 일반적으로 자료의 교환 작업(SWAP)이 자료의 이동 작업(MOVE)보다 더 복잡하기 때문에 버블 정렬은 단순성에도 불구하고 "거의 쓰이지 않는다."

### 선택 정렬 (Unstable)
![선택 정렬](https://gmlwjd9405.github.io/images/algorithm-selection-sort/selection-sort.png)
- 장점
  - 자료 이동 횟수가 미리 결정된다.
- 단점
  - 같은 값의 상대적인 위치가 변경될 수 있다. ex) [2, 1, 2, 1]

### 삽입 정렬
![삽입 정렬](https://gmlwjd9405.github.io/images/algorithm-insertion-sort/insertion-sort.png)
- 장점
  - 안정한 정렬 방법
  - 레코드의 수가 적을 경우 알고리즘 자체가 매우 간단하므로 다른 복잡한 정렬 방법보다 유리할 수 있다.
  - '거의 정렬된' 상태라면 매우 효율적이다. ex) [2, 3, 4, 5, 6, 1]
- 단점
  - 비교적 많은 레코드들의 이동을 포함한다.
  - 레코드 수가 많고 레코드 크기가 클 경우에 적합하지 않다.

### 퀵 정렬


# Reference
- https://gmlwjd9405.github.io/tags.html#algorithm