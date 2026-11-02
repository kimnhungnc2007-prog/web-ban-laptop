import streamlit as st
import random

# ================== CẤU HÌNH ==================
st.set_page_config(
    page_title="LAPTOP HUB",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background: #f4f6fb;
}

.hero {
    background: linear-gradient(120deg, #101b35, #2456a6);
    padding: 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 40px;
    font-weight: 800;
}

.product {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e5e9f0;
    min-height: 220px;
}

.price {
    color: #e65b25;
    font-size: 23px;
    font-weight: 800;
}

.tag {
    background: #eaf1ff;
    color: #2456a6;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)


# ================== DỮ LIỆU SẢN PHẨM ==================

PRODUCTS = [
    {
        "id": "L01",
        "name": "ASUS Vivobook 15",
        "brand": "ASUS",
        "price": 14990000,
        "cpu": "Intel Core i5",
        "ram": "16GB",
        "ssd": "512GB SSD",
        "gpu": "Intel Iris Xe",
        "group": "Kinh tế - Văn phòng",
        "desc": "Phù hợp học tập, Excel, PowerPoint và làm việc văn phòng."
    },
    {
        "id": "L02",
        "name": "Lenovo IdeaPad Slim 5",
        "brand": "Lenovo",
        "price": 17990000,
        "cpu": "AMD Ryzen 7",
        "ram": "16GB",
        "ssd": "512GB SSD",
        "gpu": "AMD Radeon",
        "group": "Kinh tế - Văn phòng",
        "desc": "Thiết kế gọn nhẹ, phù hợp phân tích dữ liệu và học tập."
    },
    {
        "id": "L03",
        "name": "Dell Inspiron 14",
        "brand": "Dell",
        "price": 18990000,
        "cpu": "Intel Core i5",
        "ram": "16GB",
        "ssd": "512GB SSD",
        "gpu": "Intel Iris Xe",
        "group": "Kinh tế - Văn phòng",
        "desc": "Phù hợp sinh viên, nhân viên văn phòng và công việc đa nhiệm."
    },
    {
        "id": "L04",
        "name": "ASUS TUF Gaming F15",
        "brand": "ASUS",
        "price": 23990000,
        "cpu": "Intel Core i7",
        "ram": "16GB",
        "ssd": "512GB SSD",
        "gpu": "NVIDIA RTX 4050",
        "group": "Kỹ thuật - Đồ họa",
        "desc": "GPU rời mạnh, phù hợp CAD, mô phỏng và đồ họa 3D."
    },
    {
        "id": "L05",
        "name": "Acer Nitro V 15",
        "brand": "Acer",
        "price": 21990000,
        "cpu": "Intel Core i5",
        "ram": "16GB",
        "ssd": "512GB SSD",
        "gpu": "NVIDIA RTX 4050",
        "group": "Kỹ thuật - Đồ họa",
        "desc": "Phù hợp lập trình, thiết kế và phần mềm kỹ thuật."
    },
    {
        "id": "L06",
        "name": "Lenovo LOQ 15",
        "brand": "Lenovo",
        "price": 24990000,
        "cpu": "Intel Core i7",
        "ram": "16GB",
        "ssd": "1TB SSD",
        "gpu": "NVIDIA RTX 4060",
        "group": "Kỹ thuật - Đồ họa",
        "desc": "Cấu hình mạnh, phù hợp dựng hình và render."
    },
    {
        "id": "L07",
        "name": "MacBook Air 13",
        "brand": "Apple",
        "price": 26990000,
        "cpu": "Apple M-series",
        "ram": "16GB",
        "ssd": "256GB SSD",
        "gpu": "GPU tích hợp",
        "group": "Kinh tế - Di chuyển",
        "desc": "Nhẹ, pin lâu, phù hợp học tập và di chuyển nhiều."
    },
    {
        "id": "L08",
        "name": "HP Pavilion 14",
        "brand": "HP",
        "price": 16990000,
        "cpu": "Intel Core i5",
        "ram": "16GB",
        "ssd": "512GB SSD",
        "gpu": "Intel Iris Xe",
        "group": "Văn phòng",
        "desc": "Nhỏ gọn, phù hợp Word, Excel, học online và làm việc."
    },
    {
        "id": "L09",
        "name": "ASUS ROG Zephyrus G14",
        "brand": "ASUS",
        "price": 39990000,
        "cpu": "AMD Ryzen 9",
        "ram": "32GB",
        "ssd": "1TB SSD",
        "gpu": "NVIDIA RTX 4060",
        "group": "Kỹ thuật - Cao cấp",
        "desc": "Hiệu năng cao, phù hợp kỹ thuật và sáng tạo nội dung."
    }
]


def money(value):
    return f"{value:,.0f}₫".replace(",", ".")


# ================== SESSION STATE ==================

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "orders" not in st.session_state:
    st.session_state.orders = []

if "prize" not in st.session_state:
    st.session_state.prize = None

if "coupon" not in st.session_state:
    st.session_state.coupon = None


# ================== MENU ==================

st.sidebar.markdown("# 💻 LAPTOP HUB")
st.sidebar.caption("Chọn đúng laptop – Mở tương lai")

page = st.sidebar.radio(
    "DANH MỤC",
    [
        "Trang chủ",
        "Cửa hàng",
        "Tư vấn chọn laptop",
        "Vòng quay may mắn",
        "Giỏ hàng",
        "Đơn hàng"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("### 📞 Hỗ trợ khách hàng")
st.sidebar.write("Hotline: 1900 6868")
st.sidebar.write("Email: support@laptophub.vn")
st.sidebar.caption("Giá sản phẩm là giá minh họa.")


# ==================================================
# TRANG CHỦ
# ==================================================

if page == "Trang chủ":

    st.markdown("""
    <div class="hero">
        <h1>💻 LAPTOP HUB</h1>
        <h3>CHỌN LAPTOP – MỞ TƯƠNG LAI</h3>
        <p>
        Khám phá thế giới công nghệ với những chiếc laptop
        phù hợp cho học tập, công việc và giải trí.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    c1.metric("Sản phẩm", "09+")
    c2.metric("Thương hiệu", "06")
    c3.metric("Ưu đãi", "Vòng quay may mắn")

    st.subheader("⭐ LAPTOP NỔI BẬT")

    cols = st.columns(3)

    for col, p in zip(cols, [PRODUCTS[1], PRODUCTS[4], PRODUCTS[6]]):

        with col:

            st.markdown(f"""
            <div class="product">
                <span class="tag">{p['brand']}</span>
                <h3>{p['name']}</h3>
                <div class="price">{money(p['price'])}</div>
                <p>{p['cpu']} · {p['ram']}</p>
                <p>{p['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "Thêm vào giỏ hàng",
                key=f"home_{p['id']}",
                use_container_width=True
            ):
                st.session_state.cart[p["id"]] = (
                    st.session_state.cart.get(p["id"], 0) + 1
                )
                st.success("Đã thêm vào giỏ hàng!")

    st.info(
        "💡 Chưa biết chọn laptop nào? "
        "Hãy sử dụng tính năng Tư vấn chọn laptop."
    )


# ==================================================
# CỬA HÀNG
# ==================================================

elif page == "Cửa hàng":

    st.title("🛍️ CỬA HÀNG LAPTOP")

    c1, c2, c3 = st.columns([2, 1, 1])

    keyword = c1.text_input(
        "Tìm kiếm laptop",
        placeholder="Nhập tên laptop..."
    )

    brands = ["Tất cả"] + sorted(
        set(p["brand"] for p in PRODUCTS)
    )

    brand = c2.selectbox("Thương hiệu", brands)

    price_filter = c3.selectbox(
        "Mức giá",
        [
            "Tất cả",
            "Dưới 18 triệu",
            "18–25 triệu",
            "Trên 25 triệu"
        ]
    )

    filtered = PRODUCTS.copy()

    if keyword:
        filtered = [
            p for p in filtered
            if keyword.lower() in (
                p["name"] + p["cpu"] + p["brand"]
            ).lower()
        ]

    if brand != "Tất cả":
        filtered = [
            p for p in filtered
            if p["brand"] == brand
        ]

    if price_filter == "Dưới 18 triệu":
        filtered = [
            p for p in filtered
            if p["price"] < 18000000
        ]

    elif price_filter == "18–25 triệu":
        filtered = [
            p for p in filtered
            if 18000000 <= p["price"] <= 25000000
        ]

    elif price_filter == "Trên 25 triệu":
        filtered = [
            p for p in filtered
            if p["price"] > 25000000
        ]

    st.write(f"Tìm thấy {len(filtered)} sản phẩm")

    if not filtered:
        st.warning("Không tìm thấy sản phẩm.")

    for i in range(0, len(filtered), 2):

        cols = st.columns(2)

        for col, p in zip(cols, filtered[i:i+2]):

            with col:

                st.markdown(f"""
                <div class="product">
                    <span class="tag">{p['brand']}</span>
                    <h3>{p['name']}</h3>
                    <div class="price">{money(p['price'])}</div>
                    <p><b>CPU:</b> {p['cpu']}</p>
                    <p><b>RAM:</b> {p['ram']}</p>
                    <p><b>Ổ cứng:</b> {p['ssd']}</p>
                    <p><b>Card đồ họa:</b> {p['gpu']}</p>
                    <p>{p['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

                qty = st.number_input(
                    "Số lượng",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key=f"qty_{p['id']}"
                )

                if st.button(
                    "➕ Thêm vào giỏ",
                    key=f"add_{p['id']}",
                    use_container_width=True
                ):

                    st.session_state.cart[p["id"]] = (
                        st.session_state.cart.get(p["id"], 0) + qty
                    )

                    st.success("Đã thêm sản phẩm!")


# ==================================================
# TƯ VẤN LAPTOP
# ==================================================

elif page == "Tư vấn chọn laptop":

    st.title("🎯 TƯ VẤN CHỌN LAPTOP")

    st.write(
        "Hãy cho LAPTOP HUB biết ngành học hoặc công việc "
        "của bạn để tìm chiếc laptop phù hợp."
    )

    field = st.selectbox(
        "Bạn thuộc nhóm nào?",
        [
            "Kinh tế / Marketing / Kế toán",
            "Kỹ thuật / Cơ khí / Xây dựng",
            "Công nghệ thông tin / Lập trình",
            "Thiết kế đồ họa / Dựng video",
            "Văn phòng / Di chuyển nhiều"
        ]
    )

    budget = st.selectbox(
        "Ngân sách dự kiến",
        [
            "Dưới 15 triệu",
            "15–20 triệu",
            "20–25 triệu",
            "25–35 triệu",
            "Trên 35 triệu"
        ]
    )

    priority = st.radio(
        "Bạn ưu tiên điều gì?",
        [
            "Nhẹ, pin lâu",
            "Cân bằng hiệu năng và di động",
            "Hiệu năng mạnh"
        ]
    )

    advice = {

        "Kinh tế / Marketing / Kế toán": {
            "desc": """
            - CPU: Intel Core i5 hoặc AMD Ryzen 5 trở lên.
            - RAM: Tối thiểu 16GB.
            - SSD: Từ 512GB.
            - Màn hình: 14–15.6 inch.
            - Ưu tiên pin tốt, bàn phím thoải mái.

            Phù hợp với Excel, PowerPoint, Word,
            phần mềm kế toán và phân tích dữ liệu.
            """,
            "ids": ["L01", "L02", "L03", "L07", "L08"]
        },

        "Kỹ thuật / Cơ khí / Xây dựng": {
            "desc": """
            - CPU: Core i7 hoặc Ryzen 7 trở lên.
            - RAM: 16GB–32GB.
            - SSD: Từ 512GB.
            - GPU: NVIDIA RTX rời nếu dùng CAD, Revit,
              SolidWorks hoặc mô phỏng 3D.

            Ưu tiên máy có khả năng tản nhiệt tốt.
            """,
            "ids": ["L04", "L05", "L06", "L09"]
        },

        "Công nghệ thông tin / Lập trình": {
            "desc": """
            - CPU: Core i5/i7 hoặc Ryzen 5/7.
            - RAM: Tối thiểu 16GB, nên cân nhắc 32GB.
            - SSD: 512GB–1TB.
            - Màn hình có độ phân giải tốt.

            Phù hợp lập trình, chạy IDE, máy ảo,
            cơ sở dữ liệu và Docker.
            """,
            "ids": ["L02", "L03", "L05", "L06", "L09"]
        },

        "Thiết kế đồ họa / Dựng video": {
            "desc": """
            - CPU: Core i7 hoặc Ryzen 7.
            - RAM: 16GB–32GB.
            - SSD: 1TB nếu lưu nhiều dự án.
            - GPU: NVIDIA RTX rời.
            - Màn hình ưu tiên độ chuẩn màu cao.

            Phù hợp Photoshop, Illustrator,
            Premiere và phần mềm 3D.
            """,
            "ids": ["L04", "L06", "L09"]
        },

        "Văn phòng / Di chuyển nhiều": {
            "desc": """
            - CPU: Core i5 hoặc Ryzen 5.
            - RAM: 16GB.
            - SSD: 512GB.
            - Trọng lượng lý tưởng: 1.2–1.5kg.
            - Ưu tiên pin lâu và thiết kế nhỏ gọn.

            Phù hợp Word, Excel, họp trực tuyến,
            học online và công việc hằng ngày.
            """,
            "ids": ["L02", "L03", "L07", "L08"]
        }
    }

    if st.button("✨ TÌM LAPTOP PHÙ HỢP", type="primary"):

        result = advice[field]

        st.success("Đã tìm được cấu hình phù hợp!")

        st.subheader("📌 CẤU HÌNH ĐỀ XUẤT")
        st.markdown(result["desc"])

        st.subheader("💻 SẢN PHẨM GỢI Ý")

        limits = {
            "Dưới 15 triệu": (0, 15000000),
            "15–20 triệu": (15000000, 20000000),
            "20–25 triệu": (20000000, 25000000),
            "25–35 triệu": (25000000, 35000000),
            "Trên 35 triệu": (35000000, 10**12)
        }

        low, high = limits[budget]

        picks = [
            p for p in PRODUCTS
            if p["id"] in result["ids"]
            and low <= p["price"] <= high
        ]

        if not picks:
            picks = sorted(
                [
                    p for p in PRODUCTS
                    if p["id"] in result["ids"]
                ],
                key=lambda p: abs(p["price"] - (low + high) / 2)
            )[:2]

            st.caption(
                "Chưa có mẫu đúng khoảng ngân sách. "
                "Đây là những mẫu gần ngân sách nhất."
            )

        for p in picks:

            with st.container(border=True):

                st.markdown(f"### {p['name']}")
                st.markdown(
                    f"<div class='price'>{money(p['price'])}</div>",
                    unsafe_allow_html=True
                )

                st.write(
                    f"{p['cpu']} | RAM {p['ram']} | "
                    f"{p['ssd']} | {p['gpu']}"
                )

                st.write(p["desc"])

                if st.button(
                    f"Thêm {p['name']} vào giỏ",
                    key=f"recommend_{p['id']}"
                ):

                    st.session_state.cart[p["id"]] = (
                        st.session_state.cart.get(p["id"], 0) + 1
                    )

                    st.success("Đã thêm vào giỏ hàng!")

    st.warning(
        "Lưu ý: Tư vấn mang tính tham khảo. "
        "Hãy kiểm tra yêu cầu phần mềm và cấu hình thực tế "
        "trước khi mua."
    )


# ==================================================
# VÒNG QUAY MAY MẮN
# ==================================================

elif page == "Vòng quay may mắn":

    st.title("🎡 VÒNG QUAY MAY MẮN")

    st.markdown("""
    <div class="hero">
        <h1>🍀 SPIN & WIN</h1>
        <h3>QUAY NGAY – NHẬN ƯU ĐÃI</h3>
        <p>May mắn có thể mang đến cho bạn những phần quà hấp dẫn!</p>
    </div>
    """, unsafe_allow_html=True)

    prizes = [
        ("Voucher 100.000₫", "Áp dụng đơn từ 10 triệu"),
        ("Voucher 200.000₫", "Áp dụng đơn từ 18 triệu"),
        ("Giảm giá 3%", "Tối đa 500.000₫"),
        ("Miễn phí giao hàng", "Theo khu vực hỗ trợ"),
        ("Tặng balo laptop", "Áp dụng cho một số mẫu"),
        ("Chúc bạn may mắn lần sau", "Hẹn gặp lại bạn!")
    ]

    if st.button(
        "🎯 QUAY NGAY",
        type="primary",
        use_container_width=True
    ):

        st.session_state.prize = random.choice(prizes)

    if st.session_state.prize:

        st.balloons()

        st.subheader(
            f"🎉 CHÚC MỪNG: {st.session_state.prize[0]}"
        )

        st.write(st.session_state.prize[1])

        st.session_state.coupon = st.session_state.prize[0]

    st.caption(
        "Đây là vòng quay mô phỏng ngẫu nhiên. "
        "Ưu đãi cần được cửa hàng xác nhận khi đặt hàng."
    )


# ==================================================
# GIỎ HÀNG
# ==================================================

elif page == "Giỏ hàng":

    st.title("🛒 GIỎ HÀNG")

    total = 0
    cart_items = []

    for pid, qty in list(st.session_state.cart.items()):

        product = next(
            (p for p in PRODUCTS if p["id"] == pid),
            None
        )

        if product:
            cart_items.append((product, qty))
            total += product["price"] * qty

    if not cart_items:

        st.info("Giỏ hàng của bạn đang trống.")

    else:

        for p, qty in cart_items:

            c1, c2, c3 = st.columns([3, 1, 1])

            c1.write(f"**{p['name']}**")
            c1.caption(money(p["price"]))

            new_qty = c2.number_input(
                "Số lượng",
                min_value=0,
                max_value=10,
                value=qty,
                key=f"cart_{p['id']}"
            )

            c3.write(money(p["price"] * qty))

            if new_qty != qty:

                if new_qty == 0:
                    st.session_state.cart.pop(p["id"], None)
                else:
                    st.session_state.cart[p["id"]] = new_qty

                st.rerun()

        st.divider()

        st.markdown(
            f"## Tổng tiền: <span style='color:#e65b25'>"
            f"{money(total)}</span>",
            unsafe_allow_html=True
        )

        if st.session_state.coupon:
            st.info(
                f"Ưu đãi đã nhận: {st.session_state.coupon}. "
                "Vui lòng xác nhận điều kiện với cửa hàng."
            )

        with st.form("checkout"):

            st.subheader("📦 THÔNG TIN ĐẶT HÀNG")

            name = st.text_input("Họ và tên")
            phone = st.text_input("Số điện thoại")
            email = st.text_input("Email")
            address = st.text_area("Địa chỉ nhận hàng")
            note = st.text_area("Ghi chú")

            submit = st.form_submit_button("XÁC NHẬN ĐẶT HÀNG")

            if submit:

                if not name.strip() or not phone.strip() or not address.strip():

                    st.error(
                        "Vui lòng nhập họ tên, số điện thoại "
                        "và địa chỉ."
                    )

                else:

                    st.session_state.orders.append({
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "address": address,
                        "items": [
                            (p["name"], qty)
                            for p, qty in cart_items
                        ],
                        "total": total,
                        "note": note
                    })

                    st.session_state.cart = {}

                    st.success(
                        "Đặt hàng thành công! "
                        "Cửa hàng sẽ liên hệ xác nhận."
                    )


# ==================================================
# ĐƠN HÀNG
# ==================================================

elif page == "Đơn hàng":

    st.title("📦 ĐƠN HÀNG CỦA BẠN")

    if not st.session_state.orders:

        st.info("Bạn chưa có đơn hàng.")

    else:

        for i, order in enumerate(
            reversed(st.session_state.orders), 1
        ):

            with st.expander(f"Đơn hàng #{i} - {order['name']}"):

                st.write("Số điện thoại:", order["phone"])
                st.write("Địa chỉ:", order["address"])

                st.write("Sản phẩm:")

                for name, qty in order["items"]:
                    st.write(f"- {name} x {qty}")

                st.write(
                    f"**Tổng tiền: {money(order['total'])}**"
                )

                st.write("Ghi chú:", order["note"])


# ==================================================
# CHÂN TRANG
# ==================================================

st.divider()

st.markdown(
    """
    <center>
    <h3>💻 LAPTOP HUB</h3>
    <p>Technology for your future.</p>
    <p>© 2026 LAPTOP HUB. All rights reserved.</p>
    </center>
    """,
    unsafe_allow_html=True
)
