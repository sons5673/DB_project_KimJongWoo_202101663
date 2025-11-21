import sqlite3
import csv

DATABASE = 'equipment.db'

def init_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # 여기에 테이블 생성 코드가 들어갈 예정

    conn.commit()
    conn.close()
    print("데이터베이스 초기화 완료!")

if __name__ == '__main__':
    init_database()