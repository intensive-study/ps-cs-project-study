## 인터페이스
하나의 계산기 클래스는 만드는 개발자가 있고,

이를 이용한것을 구현하는 개발자가 있을시,

동시에 진행을 하기위해 더미 클래스로 생성하여 이용자구현을 진행했지만,

추후에 완성 된 버젼을 받았을시 미스커뮤니케이션으로 인하여

계산기 클래스의 피연산자의 갯수가 바껴서 코드를 수정해야하는 번거로움이 있었다.

- 인터페이스에서 명시한 방식을 따르지 않으면, 컴파일이 실패되기때문에 사전에 약속한 내용이 파기될 가능성을 줄일수 있다.

- 인터페이스의 메소드의 접근제어자는 반드시 public이여야 함!!! 아닌경우는 정의할수없음 (에러발생)

- 인터페이스도 상속이 된다.

        interface I3 {
            public void x();
        }

        //상속
        interface I4 extends() I3 {
            public void z();
        }


        class B implement I4 {
          public void x() {}
          public void z() {}
        }
## Interface vs Abstract

- 인터페이스는 클래스가 아닌 인터페이스라는 고유한 형태를 지녔지만, 추상 클래스는 일반적인 클래스다
- 인터페이스는 구체적인 로직이나 상태를 가지고 있을수 없고, 추상 클래스는 구체적인 로직이나 상태를 가질수 있다.