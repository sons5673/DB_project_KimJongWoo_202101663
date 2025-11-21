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

    conn.commit()
    conn.close()
    print("데이터베이스 초기화 완료!")

if __name__ == '__main__':
    init_database()