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
    "thoi_han_xu_ly": "Thời hạn xử lý của thủ tục",
    "duong_dan": "Đường dẫn đến trang thông tin của thủ tục",
    "doi_tuong_thuc_hien": "Đối tượng thực hiện của thủ tục",
    "so_luong_bo_ho_so": "Số lượng bộ hồ sơ của thủ tục",
    "yeu_cau_dieu_kien": "Yêu cầu/ Điều kiện của thủ tục",
    "can_cu_phap_ly": "Căn cứ pháp lý của thủ tục",
    "bieu_mau_dinh_kem": "Biểu mẫu đính kèm của thủ tục"
}

def get_connection():
    return sqlite3.connect(DB_PATH)

def get():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
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


def get_by_id(id: int, params = []):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    always_fields = ["ten_thu_tuc", "co_quan_thuc_hien", "linh_vuc_thuc_hien"]
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


def to_string(thu_tuc_row):
    text = f"Đây là thủ tục **{thu_tuc_row['always_fields']['ten_thu_tuc']}** thuộc lĩnh vực **{thu_tuc_row['always_fields']['linh_vuc_thuc_hien']}** do **{thu_tuc_row['always_fields']['co_quan_thuc_hien']}** thực hiện."

    params_info = ""
    for key, value in dict(thu_tuc_row)["params"].items():
        if key in {"id", "duong_dan"}:
            continue
        
        if key in atrs:
            if value == "":
                params_info += f"\n\n**{atrs[key]}**:\nKhông có thông tin về {atrs[key]}"
            else:
                params_info += f"\n\n**{atrs[key]}**:\n{value}"

    if params_info:
        text += "\n\n**Thông tin bạn cần tìm kiếm như sau:**" + params_info

    text += f"\n##### Cần thêm thông tin:"
    text += f" [Xem thêm]({dict(thu_tuc_row)['params']['duong_dan']})"
    return text

thu_tucs = get()

procedure_descriptions = "\n".join([
    f"- {id}: {description}" for id, description in thu_tucs.items()
])