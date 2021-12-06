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

<br/>

### Blocking vs Non-Blocking

<br/>

### GIL(Global Interpreter Lock)
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter

- Python의 Garbage Collector가 Reference Counting으로 메모리를 해제하므로, GIL이 존재한다.
  - 예를 들어 GIL이 없을 경우, 멀티 스레딩 구조에서 A라는 스레드가 reference count가 0이 된 후 garbage collector가 사용하던 변수를 지워버리고, A스레드와 같은 자원을 공유하고 있던 B라는 스레드가 뒤늦게 지워진 변수에 접근하려 하면 에러가 발생함.

**문제점 해결방안(병렬 프로그래밍 방법):**
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

### Reference

- [realpython](https://realpython.com/python-gil/)
- [튜나 개발일기](https://devuna.tistory.com/82)