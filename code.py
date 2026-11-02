import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventory Stock Analysis", page_icon="📦")
st.title("📦 Inventory Stock Analysis")

# Starting data (edit these to match your products)
if "products" not in st.session_state:
    st.session_state.products = {
        "Pen": 50,
        "Notebook": 8,
        "Marker": 5,
    }

products = st.session_state.products

menu = st.sidebar.radio(
    "Menu",
    ["View Products", "Add Product", "Update Stock", "Low Stock Alert", "Stock Summary"],
)

if menu == "View Products":
    st.subheader("All Products")
    if products:
        df = pd.DataFrame(list(products.items()), columns=["Product", "Stock"])
        st.table(df)
    else:
        st.info("No products yet.")

elif menu == "Add Product":
    st.subheader("Add Product")
    name = st.text_input("Product name").strip()
    qty = st.number_input("Quantity", min_value=0, step=1)
    if st.button("Add"):
        if not name:
            st.error("Please enter a product name.")
        elif name in products:
            st.warning("Product already exists. Use Update Stock.")
        else:
            products[name] = int(qty)
            st.success(f"Added {name} with stock {int(qty)}")

elif menu == "Update Stock":
    st.subheader("Update Stock")
    if products:
        name = st.selectbox("Product", list(products.keys()))
        qty = st.number_input("New quantity", min_value=0, step=1, value=products[name])
        if st.button("Update"):
            products[name] = int(qty)
            st.success(f"{name} updated to {int(qty)}")
    else:
        st.info("No products to update.")

elif menu == "Low Stock Alert":
    st.subheader("Low Stock Alert")
    limit = st.slider("Alert when stock is below", 1, 100, 10)
    low = {k: v for k, v in products.items() if v < limit}
    if low:
        st.warning("These items are running low:")
        st.table(pd.DataFrame(list(low.items()), columns=["Product", "Stock"]))
    else:
        st.success("All products have enough stock.")

elif menu == "Stock Summary":
    st.subheader("Stock Summary")
    if products:
        col1, col2 = st.columns(2)
        col1.metric("Total products", len(products))
        col2.metric("Total units", sum(products.values()))
        highest = max(products, key=products.get)
        lowest = min(products, key=products.get)
        st.write(f"Highest stock: **{highest}** ({products[highest]})")
        st.write(f"Lowest stock: **{lowest}** ({products[lowest]})")
        st.bar_chart(pd.DataFrame(list(products.items()), columns=["Product", "Stock"]).set_index("Product"))
    else:
        st.info("No data yet.")
