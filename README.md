# 성남 미디어센터 장비 대여 관리 시스템

경기도 성남시 미디어센터의 장비 대여 현황 정보를 기반으로 한 웹 애플리케이션

## 프로젝트 개요
 
- **이름** : 김종우 (202101663)
- **목적** : 성남 미디어센터의 촬영/조명/사운드 장비 대여 현황을 효율적으로 관리

## 주요 기능

- **장비 목록 조회**: 전체 장비 목록 확인
- **카테고리 필터**: 촬영, 조명, 사운드, 편집, 상영, 기타 카테고리별 필터링
- **장비 추가**: 새로운 장비 등록
- **장비 수정**: 기존 장비 정보 수정
- **장비 삭제**: 불필요한 장비 삭제

## 기술 스택

- **Backend**: Python 3.x, Flask 3.0.0
- **Database**: SQLite
- **Frontend**: HTML5, CSS3
- **데이터 출처**: 공공데이터포털 (data.go.kr) - 경기도 성남시 미디어센터 장비대여 정보

## 데이터베이스 스키마

```sql
CREATE TABLE equipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,              -- 장비명
    category TEXT NOT NULL,          -- 분류
    rental_fee INTEGER NOT NULL,     -- 대여료
    quantity INTEGER NOT NULL,       -- 보유수량
    availability TEXT NOT NULL       -- 대여가능여부
);
