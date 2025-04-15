import sqlite3
from backend.database.base import get_db
from backend.models.thu_tuc import ThuTuc

DB_PATH = "chatbot.db"
atrs = {
    "id": "rowid",
    "ma_thu_tuc": "Mã thủ tục",
    "ten_thu_tuc": "Tên thủ tục",
    "cach_thuc_thuc_hien": "Cách thức thực hiện của thủ tục",
    "co_quan_thuc_hien": "Cơ quan thực hiện",
    "linh_vuc_thuc_hien": "Lĩnh vực thực hiện của thủ tục",
    "trinh_tu_thuc_hien": "Trình tự thực hiện của thủ tục",
    "thoi_han_giai_quyet": "Thời hạn giải quyết của thủ tục",
    "le_phi": "Lệ phí của thủ tục",
    "thanh_phan_ho_so": "Thành phần hồ sơ của thủ tục",
    "duong_dan": "Đường dẫn",
    "doi_tuong_thuc_hien": "Đối tượng thực hiện",
    "so_luong_bo_ho_so": "Số lượng bộ hồ sơ",
    "yeu_cau_dieu_kien": "Yêu cầu, điều kiện thực hiện",
    "can_cu_phap_ly": "Căn cứ pháp lý",
    "bieu_mau_dinh_kem": "Biểu mẫu đính kèm"
}

def get_connection():
    return sqlite3.connect(DB_PATH)

def get():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = """SELECT * FROM thu_tuc"""
    cursor.execute(query)
    rows = cursor.fetchall()

    resp_objs = {}    
    for row in rows:
        resp_objs[row["id"]] = f"""{row['ten_thu_tuc']}

- {row["id"]}: Đây là thủ tục {row['ten_thu_tuc']} thuộc lĩnh vực {row['linh_vuc_thuc_hien']} do {row['co_quan_thuc_hien']} thực hiện.
"""
        
    conn.close()
    return resp_objs


def get_by_id(id: int, params = []):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    always_fields = ["ma_thu_tuc", "ten_thu_tuc", "co_quan_thuc_hien", "linh_vuc_thuc_hien"]
    if not params:
        query = "SELECT * FROM thu_tuc WHERE rowid = ?"
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        conn.close()

        return {
            "always_fields": {key: row[key] for key in always_fields if key in row.keys()},
            "params": {key: row[key] for key in row.keys() if key not in always_fields}
        }    
    else:
        selected_fields = always_fields + params
        query = f"SELECT {', '.join(selected_fields)} FROM thu_tuc WHERE rowid = ?"
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        conn.close()

        if row is None:
            raise ValueError("Thủ tục không tồn tại")

        return {
            "always_fields": {key: row[key] for key in always_fields if key in row.keys()},
            "params": {key: row[key] for key in params if key in row.keys()}
        }


def get_random_thu_tuc(limit=10):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = f"""
        SELECT rowid as id, * 
        FROM thu_tuc 
        ORDER BY RANDOM() 
        LIMIT ?
    """
    cursor.execute(query, (limit,))
    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        thu_tuc_info = {
            "id": row["id"],
            "ma_thu_tuc": row["ma_thu_tuc"],
            "ten_thu_tuc": row["ten_thu_tuc"],
            "co_quan_thuc_hien": row["co_quan_thuc_hien"],
            "linh_vuc_thuc_hien": row["linh_vuc_thuc_hien"]
        }
        result.append(thu_tuc_info)
    
    random_procedures = "\n".join([
        f"- {row['id']}: Đây là thủ tục **{row['ten_thu_tuc']}** thuộc lĩnh vực **{row['linh_vuc_thuc_hien']}** do **{row['co_quan_thuc_hien']}** thực hiện." for row in result
    ])
    return random_procedures


def to_string(thu_tuc_row):
    text = f"Đây là thủ tục **{thu_tuc_row['always_fields']['ten_thu_tuc']}** thuộc lĩnh vực **{thu_tuc_row['always_fields']['linh_vuc_thuc_hien']}** do **{thu_tuc_row['always_fields']['co_quan_thuc_hien']}** thực hiện."

    params_info = ""
    for key, value in dict(thu_tuc_row)["params"].items():
        if key == "id" or value == "":
            continue
        
        if key in atrs:
            params_info += f"\n\n**{atrs[key]}**:\n{value}"

    if params_info:
        text += "\n\n**Thông tin bạn cần tìm kiếm như sau:**" + params_info

    return text

procedures = get()