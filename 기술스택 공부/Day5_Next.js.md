https://www.opentutorials.org/course/5098

# Next.js(Full Stack Web Application Framework)
- React로 만든 서버 사이드 렌더링 프레임워크

## Rendering
- 요청 받은 내용을 브라우저 화면에 표시하는 것  

### Client Side Rendering(클라이언트가 주체)
- 클라이언트 사이드에서 HTML을 반환한 후, JS가 동작하면서 데이터만을 주고 받아서 클라이언트에서 렌더링을 진행하는 것
- 첫 페이지 로딩 시, SSR에 비해 속도가 다소 느림
- 자바 스크립트가 로드되지 않는 경우 아무런 정보가 보이지 않음. 따라서 구글 검색 엔진의 경우, 자바 스크립트가 로드되지 않으면, 검색 엔진에서 스캔하는데 검색에 아무 페이지도 걸리지 않게 됨. SEO 문제 발생함.
- Single Page Application
  - 하나의 페이지에서 내용을 동적으로 변경함으로써 사용자 웹앱을 의미함
  - SPA 구현 방식은 여러가지가 있는데, 대표적인 방식으로 Ajax를 통한 콘텐츠 로드
  - 페이지 새로 고침 없이 데이터가 교환되고 업데이트되는 것

### Server Side Rendering(서버가 주체) - Next.js가 지원함
- 클라이언트인 브라우저가 서버에 매번 데이터를 요청하여 서버에서 처리하는 방식
- 클라이언트의 요청이 들어올 때마다 매번 서버에서 새로운 화면을 만들어 제공
- SEO(검색 엔진 최적화 : 검색 결과에서 내 콘텐츠가 상위에 노출될 수 있도록 콘텐츠를 최적화하는 방식) 문제 해결
- 초기 로딩 이후 페이지 이동 시, CSR에 비해 속도가 다소 느림  
(각 페이지에 접근할 때마다 새로운 리소스를 요청해야 하기 때문)

## next.js가 제공하는 주요 기능
- hot reloading  
개발 중 저장되는 코드는 자동으로 새로고침됨
- automatic routing  
pages 폴더에 있는 파일이 해당 파일의 이름으로 라우팅됨  
(예시 : pages/page1.tsx -> localhost:3000/page1)  
public 폴더도 pages의 폴더와 동일하게 라우팅할 수 있음. 그러나 모든 사람이 페이지에 접근할 수 있으므로 지양함
- single file components  
style jsx를 사용함으로써 컴포넌트 내부에 해당 컴포넌트만 scope를 가지는 css를 만들 수 있음  
- server landing  
서버 렌더링을 함. 클라이언트 렌더링과 다르게 서버 렌더링을 한 페이지의 소스 보기를 클릭하면 내부에 소스가 있음
- code splitting  
dynamic import를 이용하면 손쉽게 code splitting이 가능해짐  
code splitting : 내가 원하는 페이지에서 원하는 자바스크립트와 라이브러리를 렌더링하는 것  
모든 번들(chunk.js)이 하나로 묶이지 않고 각각으로 나뉘어, 좀 더 효율적으로 자바스크립트 로딩 시간을 개선할 수 있음
- typescript  
타입스크립트의 활용을 위해 웹팩을 만지거나 바벨을 만질 필요 없음. 타입스크립트를 설치하고 명령어(yarn run dev)를 실행하면 자동으로 tsconfig, next-end.d.ts가 생성되어 타입스크립트로 코딩이 가능해짐  
<br>

## _document.tsx
```
// pages/_document.tsx
import Document, { Html, Head, Main, NextScript } from "next/document";

export default class CustomDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          // 모든 페이지에 아래 메타테크가 head에 들어감
          // 루트 파일이기에 가능함
          // 적은 코드만 넣어야함(전역 파일을 엉망으로 만들면 안됨)
          <meta property="custom" content="123123" />
        </Head>
        <body>
          <Main />
        </body>
        <NextScript />
      </Html>
    );
  }
}
```

- meta 태그를 정의하거나, 전체 페이지에 관려하는 컴포넌트
- 이곳에서의 console은 서버에서만 보이고, 클라이언트에서는 안 보임
- render 요소는 반영하지만 페이지 구성 요소만 반영되고, js는 반영하지 않기 때문에 console이 보이지 않음
- componentDidMount 같은 Hook도 실행되지 않음
- 정말 static한 상황에서만 사용  
<br>

## _app.tsx
```
function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

- _app.tsx에서 렌더링하는 값은 모든 페이지에 영향을 줌
- 최초로 실행되는 것은 _app.tsx
- _app.tsx은 클라이언트에서 띄우길 바라는 전체 컴포넌트  
-> 공통 레이아웃으로 최초 실행되며, 내부에 컴포넌트들을 실행함
- 내부에 컴포넌트가 있다면, 전부 실행하고 html의 body로 구성
- component, pageProps를 받음  
  - 여기서 props로 받은 component는 요청한 페이지
  - GET / 요청을 보냈다면, component에는 /pages/index.js 파일이 props로 내려오게 됨
  - pageProps : 페이지 getInitialProps를 통해 내려받은 props들을 의미
- 그 다음 _document.tsx가 실행됨
- 페이지를 업데이트 하기 전에 원하는 방식으로 페이지를 업데이트하는 통로
- _app.tsx에서 console.log 실행 시, client, server 둘 다 콘솔에 찍힘  
(localhost:3000 웹과 터미널에서 둘 다 콘솔 보임)

## import style component
```
import styles from "./test.module.css";

function Heading(props) {
  // const variable = "red";
  return (
    <div className="title">
      <h1 className={styles.red}>{props.heading}</h1>
    </div>
  );
}

export default function Home() {
  return (
    <div>
      <Heading heading="heading" />
      <h1>스타일</h1>
    </div>
  );
}
```
```
// test.module.css

h1.red {
  color: blue;
}
```

## sass 사용하기
- 따로 config 파일을 정의하지 않고, css 파일을 scss로 바꾸고, yarn add sass --dev를 해주면 next에서 알아서 설정해줌

## Link 사용하기
```
import Link from "next/link";

const Index = () => (
  <div>
    <Link href="/blog">
      <a>Blog</a>
    </Link>
    // 동적 link시 [] 사용
    <Link href="/blog/[address]">
      <a>Blog</a>
    </Link>
  </div>
);
```
- 보통 페이지 간 이동은 a 태그를 사용하나, next에서는 사용하지 않음
- a 태그를 사용하면, 처음 페이지에 진입할 때 번들 파일을 받게 되는데, a 태그에 의해 라우팅하게 되면 다시 번들 파일을 받기 때문
- redux를 사용하는 경우, store의 state 값이 증발되는 현상도 발생함
- 그렇기 때문에 a 태그는 완전히 다른 사이트로 페이지를 이동시켜 다시 돌아오지 않는 경우만 사용하고, 그 이외에는 모든 Link를 사용

## 동적 url (dynamic route)
```
// pages/[id].tsx

import { useRouter } from "next/router";

export default () => {
  const router = useRouter();

  return (
    <>
      <h1>post</h1>
      <p>postid: {router.query.id}</p>
    </>
  );
};
```

- 가변적으로 변하는 url에 대해 동적 url을 지원
- [] 문법으로 동적 페이지를 생성하는 동적 url을 만들 수 있음
- 위처럼 작성하면 localhost:3000/123으로 접속 시, postid가 123으로 나옴
- router.query.id의 id는 postid와 동일

## Optional catch all routes
- dynamic route를 사용하고 싶지 않을 때, dynamic page를 optional하게 주는 문법을 사용하면 됨
- [[...page]].tsx와 같은 형식으로 파일을 만들면 됨. [page].tsx와 다른 점은 router.query.page의 값이 배열로 담기는 것  
예를 들어 page/test/[[...page]].tsx가 경로일 때, url이 /test/1/2/3으로 들어왔다면, router.query.page의 값은 ['1', '2', '3'] 이렇게 들어옴
- router.query.page의 타입은 undefined, string, string[]으로 페이지 변경에 따라 보여줄 컴포넌트가 다르다면, 이 세 타입에 대한 조건을 모두 걸어줘야 함

## prefetching
- 백그라운드에서 페이지를 미리 가져옴. 기본값은 true
- <Link /> 뷰포트에 있는 모든 항목(초기 또는 스크롤을 통해)이 미리 로드됨
- 정적 생성을 사용하느 JSON페이지는 더 빠른 페이지 전환을 위해 데이커가 포함된 파일을 미리 로드함
- Link 컴포넌트를 사용함. Link 컴포넌트를 렌더링할 때 <Link prefetch href="..."> 형식으로 prefetch 값을 전달해주면 데이터를 먼저 불러온 뒤, 라우팅을 시작
- 프로덕션 레벨에서만 이루어짐

## next/router 사용법
```
import { useEffect } from "react";
import { useRouter } from "next/router";
import posts from "../posts.json";

export default () => {
  const router = useRouter();

  const post = posts[router.query.id as string];
  if (!post) return <p>noting</p>;

  useEffect(() => {
    router.prefetch("/test");
  }, []);

  return (
    <>
      <h1>{post.title}</h1>
      <h1>{post.content}</h1>
      <button onClick={() => router.push("test")}>go to Test</button>
    </>
  );
};
```

- react의 react-router-dom과 사용 방법이 거의 유사함
- Link에 있는 prefetch 기능도 사용 가능함

[출처 : https://kyounghwan01.github.io/blog/React/next/basic/#server-side-lifecycle]