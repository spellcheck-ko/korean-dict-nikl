# 국립국어원 사전

국립국어원 사이트에서 다운로드할 수 있는 사전 데이터입니다.

- 한국어기초사전: https://krdict.korean.go.kr/
- 표준국어대사전: https://stdict.korean.go.kr/
- 우리말샘: https://opendict.korean.go.kr/

## 업데이트

비정기적으로 국립국어원 사이트에서 다운로드한 데이터로 업데이트됩니다.

직접 업데이트하려면 각 사이트에 회원 가입을 하고 로그인을 한 뒤, "내 정보
관리" -> "사전 내려받기" 메뉴에서 "전체 내려받기"를 눌러 XML ZIP 파일을 받아
해당 폴더에서 `python3 update.py 파일이름.zip`과 같이 실행하면 됩니다.

단 이 파일은 미리 만들어 놓은 버전이기 때문에 빨리 다운로드할 수 있지만,
최신의 내용이 들어있지 않을 수도 있습니다. 최신의 데이터를 받으려면 각
사이트에서 로그인한 뒤 "자세히 검색"에서 "내려받기"를 눌러 XML 형식으로
다운로드하면 되지만 다운로드할 파일이 준비되기까지 수시간에서 하루 이상 걸릴
수도 있습니다.

## 빌드

- dict FIXME
- XDXF FIXME

## 저작권 정보

이 저작물은 크리에이티브 커먼즈 저작자표시-동일조건변경허락 2.0 대한민국
라이선스에 따라 이용할 수 있습니다. 라이선스 전문을 보려면
https://creativecommons.org/licenses/by-sa/2.0/kr/ 을 방문하거나 다음의 주소로
서면 요청해 주십시오. Creative Commons, PO Box 1866, Mountain View, CA 94042,
USA.

### 저작권 관련 주의

- 표준국어대사전, 우리말샘 사전에 포함된 사전 예문 중에서 출판물, 신문 등에서 
  인용된 예문은 공정 사용의 범위에서 이용할 수 있을 뿐 자유로운 사용이 불가합니다.

- 2019년 7월 현재 국립국어원 사이트로 링크되어 있는 발음 파일은 모두 재배포
  불가능하다는 답을 받았습니다. URL에 "naver"가 들어가 있는 네이버문화재단에서
  후원한 발음 파일과 그렇지 않은 발음 파일 모두 그렇습니다.
