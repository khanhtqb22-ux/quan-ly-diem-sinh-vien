
# QUAN LY DIEM SINH VIEN - STREAMLIT

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# 1. Tao du lieu sinh vien
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Em",
        "Vo Thi Hoa",
        "Do Van Hung",
        "Bui Thi Lan",
        "Dang Van Minh",
        "Nguyen Thi Nga"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 5, 9, 7, 10],
    "Giua_ky":    [8, 7, 6, 9, 5, 8, 4, 9, 7, 8],
    "Cuoi_ky":    [9, 8, 7, 9, 4, 9, 5, 8, 6, 10]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# 3. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Tieu de website
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý, tính điểm và xếp loại sinh viên.")

# 5. Hien thi bang diem
st.subheader("1. Bảng điểm sinh viên")

bang_diem = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_diem, use_container_width=True)

# 6. Thong ke
st.subheader("2. Thống kê kết quả")

diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Điểm trung bình", f"{diem_tb:.2f}")
cot2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
cot3.metric("Điểm cao nhất", f"{sv_max['Tong_ket']:.2f}")
cot4.metric("Điểm thấp nhất", f"{sv_min['Tong_ket']:.2f}")

st.write(
    f"**Sinh viên cao điểm nhất:** "
    f"{sv_max['Ho_ten']} ({sv_max['Tong_ket']:.2f} điểm)"
)

st.write(
    f"**Sinh viên thấp điểm nhất:** "
    f"{sv_min['Ho_ten']} ({sv_min['Tong_ket']:.2f} điểm)"
)

# 7. Chon sinh vien bang Selectbox
st.subheader("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Ho_ten']}")

c1, c2, c3 = st.columns(3)
c1.metric("Chuyên cần", f"{sv['Chuyen_can']:.1f}")
c2.metric("Giữa kỳ", f"{sv['Giua_ky']:.1f}")
c3.metric("Cuối kỳ", f"{sv['Cuoi_ky']:.1f}")

st.metric("Điểm tổng kết", f"{sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# 8. Bieu do cot
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)
ax.grid(axis="y", linestyle="--", alpha=0.4)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 9. Thong tin nguoi tao
st.divider()
st.caption("Người tạo ứng dụng: [Huỳnh Tấn Khánh] | MSSV: [052208004285]")
