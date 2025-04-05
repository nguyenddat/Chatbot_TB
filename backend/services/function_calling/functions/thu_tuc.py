from database.base import get_db
from models.thu_tuc import ThuTuc

def get():
    db = next(get_db())

    try:
        thu_tucs = db.query(
            ThuTuc.id, 
            ThuTuc.ten_thu_tuc,
            ThuTuc.co_quan_thuc_hien,
            ThuTuc.linh_vuc_thuc_hien,
        ).all()

        resp_objs = {}
        for thu_tuc in thu_tucs:
            resp_objs[thu_tuc.id] = f"Đây là thủ tục {thu_tuc.ten_thu_tuc} thuộc lĩnh vực {thu_tuc.linh_vuc_thuc_hien} do {thu_tuc.co_quan_thuc_hien} thực hiện."
        
        return resp_objs

    finally:
        db.close()


def get_by_id(db, id):
    thu_tuc = db.query(ThuTuc).filter(ThuTuc.id == id).first()
    if not thu_tuc:
        raise ValueError("Thủ tục không tồn tại")
    
    return thu_tuc

def to_string(thu_tuc):
    return f"""
    Đây là thủ tục {thu_tuc.ten_thu_tuc} thuộc lĩnh vực {thu_tuc.linh_vuc_thuc_hien} do {thu_tuc.co_quan_thuc_hien} thực hiện.
    Trình tự thực hiện: {thu_tuc.trinh_tu_thuc_hien}
    Thời hạn giải quyết: {thu_tuc.thoi_han_giai_quyet}
    Phí và lệ phí: {thu_tuc.le_phi}
    Thành phần hồ sơ:
    {thu_tuc.thanh_phan_ho_so}
    """

thu_tucs = get()