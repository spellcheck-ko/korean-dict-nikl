# 국립국어원 사전

국립국어원 사이트에서 다운로드할 수 있는 사전 데이터입니다.

- 한국어기초사전: https://krdict.korean.go.kr/
- 표준국어대사전: https://stdict.korean.go.kr/
- 우리말샘: https://opendict.korean.go.kr/

파생 작업에서 편리하게 사용할 수 있도록 다운로드해 관리합니다. 이 저장소는
국립국어원에서 관리하지 않으며, 내용에 대해 책임을 지지 않습니다.

## 업데이트

비정기적으로 국립국어원 사이트에서 다운로드한 데이터로 업데이트됩니다.

한국어기초사전의 경우, 하단의 "사전 전체 내려받기"에서 XML ZIP 파일을
받습니다. 표준국어대사전 및 우리말샘은, 각 사이트에 회원 가입을 하고 로그인을
한 뒤, "내 정보 관리" -> "사전 내려받기" 메뉴에서 "전체 내려받기"를 눌러 XML
ZIP 파일을 받습니다. 파일을 받았으면 해당 폴더에서 `python3 update.py
파일이름.zip`과 같이 실행하면 됩니다.

## 빌드

- dict FIXME
- XDXF FIXME

## 저작권 정보

이 저작물은 크리에이티브 커먼즈 저작자표시-동일조건변경허락 2.0 대한민국
라이선스에 따라 이용할 수 있습니다. 라이선스 전문을 보려면
https://creativecommons.org/licenses/by-sa/2.0/kr/ 을 방문하거나 다음의 주소로
서면 요청해 주십시오. Creative Commons, PO Box 1866, Mountain View, CA 94042,
USA.

### 저작권 정책 참고

국립국어원은 한국어기초사전, 표준국어대사전, 우리말샘의 데이터를 2019년 3월
11일부터 CC-BY-SA 2.0 KR 라이선스로 배포하고 있습니다.

- https://krdict.korean.go.kr/kor/kboardPolicy/copyRightTermsInfo
- https://stdict.korean.go.kr/join/copyrightPolicy.do
- https://opendict.korean.go.kr/service/copyrightPolicy

### 저작권 관련 주의

- 예문: 표준국어대사전, 우리말샘 사전에 포함된 사전 예문 중에서 출판물, 신문
  등에서 인용된 예문은 보도·비평·교육·연구 등 저작권법에 명시된 공정 이용의
  범위에서 이용할 수 있을 뿐, __오픈소스가 아니며__, 자유로운 사용이
  불가합니다.

- 미디어 파일: 국립국어원 사이트로 링크되어 있는 이미지, 동영상, 소리, 발음
  등의 미디어 파일은 모두 __오픈소스가 아니며__, 재배포 불가능합니다(2019년
  7월 기준). URL에 "naver"가 들어가 있는 네이버문화재단에서 후원한 발음 파일과
  그렇지 않은 발음 파일 모두 그렇습니다.
