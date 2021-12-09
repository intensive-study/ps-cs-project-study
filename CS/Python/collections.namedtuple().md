## collections.namedtuple()

```
import collections

# Person 객체 만들기
Person = collections.namedtuple("Person", 'name age gender')
P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')

for n in [P1, P2]:
    print('%s는(은) %d세의 %s성 입니다.' % n)
>>Jhon는(은) 28세의 남성 입니다.
>>Sally는(은) 28세의 여성 입니다.

print(P1.name, P1.age, P1.gender)
print(P2.name, P2.age, P2.gender)
>>Jhon 28 남
>>Sally 28 여
```
- 예를들어 필드명 x 와 y 를 지정할 경우 'x y' 나 'x, y'와 같이 입력해야한다. 다른방법으로는 ['x', 'y']와 같이 리스트(list)형식으로 필드명을 지정해줄 수 있다.

## namedtuple()의 메소드

1. _make(iterable)

collections.namedtuple()의 _make()함수는 기존에 생성된 namedtuple()에 새로운 인스턴스(객체)를 생성하는 메소드이다.
```
import collections

Person = collections.namedtuple("Person", 'name age gender')
P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')

# _make()를 이용하여 새로운 객체 생성
P3 = Person._make(['Tom', 24, '남'])

for n in [P1, P2, P3]:
    print('%s는(은) %d세의 %s성 입니다.' % n)
>>Jhon는(은) 28세의 남성 입니다.
>>Sally는(은) 28세의 여성 입니다.
>>Tom는(은) 24세의 남성 입니다.
```

2. _asdict()

기존에 생성된 namedtuple()의 인스턴스(객체)를 OrderedDict로 변환해 주는 함수이다.
```
import collections

Person = collections.namedtuple("Person", 'name age gender')

P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')
P3 = Person._make(['Tom', 24, '남'])

# _asdict()를 이용하여 OrderedDict로 변환
print(P3._asdict())
>>OrderedDict([('name', 'Tom'), ('age', 24), ('gender', '남')])
```

3. _replace(kwargs)

기존에 생성된 namedtuple()의 인스턴스(객체)의 값을 변경할때 사용하는 함수이다.

```
import collections

Person = collections.namedtuple("Person", 'name age gender')
P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')
P3 = Person._make(['Tom', 24, '남'])

for n in [P1, P2, P3]:
    print('%s는(은) %d세의 %s성 입니다.' %n)
>>Jhon는(은) 28세의 남성 입니다.
>>Sally는(은) 28세의 여성 입니다.
>>Tom는(은) 24세의 남성 입니다.

# _replace()를 이용하여 인스턴스 값 변경
P1 = P1._replace(name='Neo')
P2 = P2._replace(age=27)
P3 = P3._replace(age=26)
print('-'*20)
for n in [P1, P2, P3]:
    print('%s는(은) %d세의 %s성 입니다.' %n)
--------------------
>>Neo는(은) 28세의 남성 입니다.
>>Sally는(은) 27세의 여성 입니다.
>>Tom는(은) 26세의 남성 입니다.
```

4. _fields

생성된 namedtuple()의 필드명(field_names)를 tuple()형식으로 return해준다.

```
import collections

Person = collections.namedtuple("Person", 'name age gender')
P1 = Person(name='Jhon', age=28, gender='남')

# _fields를 이용하여 필드명 출력
print(P1._fields)
>>('name', 'age', 'gender')
```

5. getattr()

getattr()는 collections.namedtuple()의 메소드는 아니지만, field_names로 namedtuple()의 인스턴스(객체)의 값을 추출해준다.

```
import collections

Person = collections.namedtuple("Person", 'name age gender')
P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')
P3 = Person._make(['Tom', 24, '남'])

print(getattr(P1, 'name'))
>>Jhon
print(getattr(P2, 'gender'))
>>여
print(getattr(P3, 'age'))
>>24
```

6. dictionary 에서 namedtuple()로 변환(**dict)

double-star-operator(**)는 딕셔너리(dict)를 namedtuple()로 변환해준다.

double-star-operator (dict -> namedtuple)
```
import collections

Person = collections.namedtuple("Person", 'name age gender')

P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')

# double-star-operator
dic = {'name' : 'Tom', 'age' : 24, 'gender' : '남'}
P3 = Person(**dic)

for n in [P1, P2, P3]:
    print(n)

Person(name='Jhon', age=28, gender='남')
Person(name='Sally', age=28, gender='여')
Person(name='Tom', age=24, gender='남')
```


출처: [EXCELSIOR](https://excelsior-cjh.tistory.com/entry/collections-모듈-namedtuple?category=966334)