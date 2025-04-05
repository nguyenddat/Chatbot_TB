import sqlite3
from database.base import get_db
from models.thu_tuc import ThuTuc

DB_PATH = "chatbot.db"
def get_connection():
    return sqlite3.connect(DB_PATH)

def get():
    conn = get_connection()
    conn.row_factory = sqlite3.Row  # Trả về dict-like rows
    cursor = conn.cursor()

    query = """
    SELECT rowid AS id, ten_thu_tuc, co_quan_thuc_hien, linh_vuc_thuc_hien
    FROM thu_tuc
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    resp_objs = {}
    for row in rows:
        resp_objs[row["id"]] = f"Đây là thủ tục {row['ten_thu_tuc']} thuộc lĩnh vực {row['linh_vuc_thuc_hien']} do {row['co_quan_thuc_hien']} thực hiện."

    conn.close()
    return resp_objs


def get_by_id(id: int):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT * FROM thu_tuc WHERE rowid = ?"
    cursor.execute(query, (id,))
    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise ValueError("Thủ tục không tồn tại")

    return row


def to_string(thu_tuc_row):
    return f"""
    Đây là thủ tục {thu_tuc_row['ten_thu_tuc']} thuộc lĩnh vực {thu_tuc_row['linh_vuc_thuc_hien']} do {thu_tuc_row['co_quan_thuc_hien']} thực hiện.
    Trình tự thực hiện: {thu_tuc_row['trinh_tu_thuc_hien']}
    Thời hạn giải quyết: {thu_tuc_row['thoi_han_giai_quyet']}
    Phí và lệ phí: {thu_tuc_row['le_phi']}
    Thành phần hồ sơ:
    {thu_tuc_row['thanh_phan_ho_so']}
    """

thu_tucs = get()

# def get():
#     db = next(get_db())

#     try:
#         thu_tucs = db.query(
#             ThuTuc.id, 
#             ThuTuc.ten_thu_tuc,
#             ThuTuc.co_quan_thuc_hien,
#             ThuTuc.linh_vuc_thuc_hien,
#         ).all()

#         resp_objs = {}
#         for thu_tuc in thu_tucs:
#             resp_objs[thu_tuc.id] = f"Đây là thủ tục {thu_tuc.ten_thu_tuc} thuộc lĩnh vực {thu_tuc.linh_vuc_thuc_hien} do {thu_tuc.co_quan_thuc_hien} thực hiện."
        
#         return resp_objs

#     finally:
#         db.close()


# def get_by_id(db, id):
#     thu_tuc = db.query(ThuTuc).filter(ThuTuc.id == id).first()
#     if not thu_tuc:
#         raise ValueError("Thủ tục không tồn tại")
    
#     return thu_tuc

# def to_string(thu_tuc):
#     return f"""
#     Đây là thủ tục {thu_tuc.ten_thu_tuc} thuộc lĩnh vực {thu_tuc.linh_vuc_thuc_hien} do {thu_tuc.co_quan_thuc_hien} thực hiện.
#     Trình tự thực hiện: {thu_tuc.trinh_tu_thuc_hien}
#     Thời hạn giải quyết: {thu_tuc.thoi_han_giai_quyet}
#     Phí và lệ phí: {thu_tuc.le_phi}
#     Thành phần hồ sơ:
#     {thu_tuc.thanh_phan_ho_so}
#     """
