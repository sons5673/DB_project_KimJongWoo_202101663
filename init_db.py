import sqlite3
import csv

DATABASE = 'equipment.db'

def init_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # 기존 테이블이 있으면 삭제
    cursor.execute('DROP TABLE IF EXISTS equipments')

    # equipments 테이블 생성
    cursor.execute('''
        CREATE TABLE equipments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            rental_fee INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            availability TEXT NOT NULL
        )
    ''')
    print("equipments 테이블 생성 완료!")

    # CSV 파일에서 데이터 읽기
    csv_file = '경기도 성남시_성남 미디어센터 장비대여 정보_20250529.csv'

    with open(csv_file, 'r', encoding='cp949') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            # CSV 데이터를 DB에 insert하는 코드가 여기에 들어갈 예정
            pass

    print("CSV 파일 읽기 완료!")

    conn.commit()
    conn.close()
    print("데이터베이스 초기화 완료!")

if __name__ == '__main__':
    init_database()