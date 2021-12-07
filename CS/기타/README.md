# 공통 질문

### 동적타입(Dynamically Typed) vs 정적타입(Statically Typed)

<br/>

#### 정적타입
- **컴파일시** 변수의 타입이 결정됨
- ex) Java, C, C++, C#, Haskell 등

**장점**
- 컴파일시 미리 타입을 결정하므로 실행속도가 빠름 
- 타입에러를 초기에 발견 가능하여 안정성이 높다

**단점**
- 코드 작성시 매번 변수의 자료형을 신경써서 결정해야함

<br/>

#### 동적타입

- 컴파일 시 자료형을 정하는 것이 아니라, **런타임**시 결정됨
- ex) Python, Javascript, Ruby, Groovy, PHP 등

**장점**
- 컴파일시 타입을 명시해주지 않아도 되기 때문에 빠르게 코드작성이 가능
- 런타임까지 타입에 대한 결정을 끌고 갈수 있기에 **유연성**이 높음

**단점**
- 실행 도중에 변수에 예상치 못한 타입이 들어와 타입에러가 발생할 수 있음

동적타입 언어는 런타임 시 확인할 수 밖에 없기 때문에, 코드가 길고 복잡해질 경우 타입 에러를 찾기가 어려워 집니다.
이러한 불편함을 해소하기 위해 TypeScipt나 Flow 등을 사용할 수 있습니다.

<br/>

### 동기(Sync) vs 비동기(Async)
동기/비동기: 호출되는 함수의 작업 완료 여부를 신경쓰는지의 차이

**동기**
- A함수가 B함수를 호출 뒤, 함수 B의 리턴값을 계속 확인하면서 기다림

**비동기**
- A함수가 B함수를 호출 뒤, 함수 B의 작업 완료 여부를 신경쓰지 않음
- A함수가 B함수를 호출할 때 콜백 함수를 함께 전달해서, B함수의 작업이 완료되면 함께 보낸 콜백함수를 실행한다.

<br/>

### Blocking vs Non-Blocking
블로킹/논블로킹: 제어권을 누가 소유하는지 차이

**블로킹**
- A함수가 B함수를 호출하면, 제어권을 A가 호출한 B에게 넘겨준다.

**논블로킹**
- A함수가 B함수를 호출해도 제어권은 A 자신이 가지고 있는다.

<br/>

### GIL(Global Interpreter Lock)
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter

- Python의 Garbage Collector가 Reference Counting으로 메모리를 해제하므로, GIL이 존재한다.
  - 예를 들어 GIL이 없을 경우, 멀티 스레딩 구조에서 A라는 스레드가 reference count가 0이 된 후 garbage collector가 사용하던 변수를 지워버리고, A스레드와 같은 자원을 공유하고 있던 B라는 스레드가 뒤늦게 지워진 변수에 접근하려 하면 에러가 발생함.

**해결방안(병렬 프로그래밍 방법)**
1. GIL이 없는 다른 구현체 사용하기
   - ex) Jython(Java), IronPython(C#)
2. Python에서 제공하는 **multiprocessing** 라이브러리 사용
   - GIL 자체가 stack메모리를 공유하는 스레드의 동시 접근을 제한함 --> 멀티 프로세싱 적용시, GIL을 우회 시킬수 있어 병렬처리 가능
3. CPU-bound 코드를 C로 짜여진 라이브러리를 사용
   - Python 바깥에서 멀티 스레드로 효율적인 연산 가능
   - ex) numpy, scipy

<br/>

### 일반 함수 vs 람다 함수(익명함수)
- 일반적으로 **여러번** 사용하고 복잡한 로직이 필요한 경우 일반 함수(def)를 사용한다.
- 간단한 로직이나, **일회성**으로 사용되는 함수같은 경우 람다함수를 이용한다.


        #일반 함수 버전
        def is_even(x):
            return x % 2 == 0
        result = list(filter(is_even, range(7)))
        # result = [0, 2, 4, 6]
         
        #람다 함수 버전
        result = list(filter((lambda x: x % 2 == 0), range(7)))
        # result = [0, 2, 4, 6]

<br/>

### List Comprehension vs Generator
```
# list comprehension(eager loading)
for a in [n for n in range(1,11)]:
    print(a)
```
```
# generator(lazy loading)
for a in (n for n in range(1,11)):
    print(a)
```
**List Comprehension**
- 첫번째 예시는 list가 반환되어 쓰였고, 두번째 예시는 Generator가 반환돼 쓰였다. 하지만 이 둘에는 큰 차이가 있는데 내부적으로 컴퓨터 메모리와 관련이 있다.

![list_comprehesion](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2F7Gh3L%2FbtqXXjWUn88%2FcaJKDmiNKf4QR9AUkEQ1gk%2Fimg.png)
- 중요한 것은 1번과 같이 list comprehension 식을 입력했을 때 메모리에 배열의 크기에 비례하는 공간이 바로 할당된다는 것이다.
- 위의 예에서라면 10개의 정수가 배열에 있으므로 이 배열의 총 크기는 40 byte(4 * 10)이 될 것이다.

**Generator**
- generator expression을 통해 생성한 generator는 숫자 10개를 생성할 예정이지만 그것을 배열 등의 구체적인 형태로 가지고 있지 않다.
- generator expression은 지정한 규칙대로 값을 반환할 규칙과 현재 어디까지 반환했는지 들을 관리할 여러 상태 값을 담고 있지만 배열과 달리 값 모두를 generator를 생성할 당시에 메모리에 할당하지 않는다는 결정적인 차이가 있다.

**Generator 장점**

1. 메모리를 효율적으로 사용할 수 있다.
    - list 는 리스트 안의 모든 데이터를 메모리에 저장하기 때문에 list 의 크기만큼 메모리 용량을 사용하게 됩니다.
    - 반면에 generator 는 데이터 값을 모두 저장하는 것이 아니고 next() 메소드를 통해 값에 접근할 때마다 메모리에 저장하는 방식이어서 메모리 효율이 좋다는점.
2. Lazy evaluation(말그대로 실행을 지연시킨다는 의미)을 통해 메모리 부족으로 프로그램이 실패하는 것을 방지함으로써 보장되는 안정성

<br/>

### Reference

- [튜나 개발일기](https://devuna.tistory.com/82)
- [realpython](https://realpython.com/python-gil/)
- [coding-lks](https://coding-lks.tistory.com/m/140?category=446043)