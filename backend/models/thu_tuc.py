from sqlalchemy import Column, String, Integer

from backend.models.base import BareBaseModel

class ThuTuc(BareBaseModel):
    __tablename__ = "thu_tuc"

    ma_thu_tuc = Column(String(50), index=True)
    ten_thu_tuc = Column(String, nullable=False)
    co_quan_thuc_hien = Column(String, nullable=False)
    linh_vuc_thuc_hien = Column(String, nullable=False)
    thanh_phan_ho_so = Column(String, nullable=False)
    le_phi = Column(String, nullable=False)
    thoi_han_giai_quyet = Column(String, nullable=False)
    cach_thuc_thuc_hien = Column(String, nullable=False)
    trinh_tu_thuc_hien = Column(String, nullable=False)
    duong_dan = Column(String, nullable = False)
    doi_tuong_thuc_hien = Column(String, nullable = False)
    so_luong_bo_ho_so = Column(String, nullable = False)
    yeu_cau_dieu_kien = Column(String, nullable = False)
    can_cu_phap_ly = Column(String, nullable = False)
    bieu_mau_dinh_kem = Column(String, nullable = False)


# mã thủ tục, tên thủ tục, cơ quan thực hiện, lĩnh vực thực hiện, thành phần hồ sơ
# lệ phí, thời hạn giải quyết, cách thức thực hiện, trình tự thực hiện