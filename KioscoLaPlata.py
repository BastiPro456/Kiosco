import pdf_presupuesto
producto = ["Coca Cola", "Asado 1kg", "Berenjena al Escaveche", "Galletas", "Alfajores"]
Efectivo = "Efectivo"
Transferencia = "Transferencia"
precio = [1500, 9000, 4600, 4000, 2000]
import time 
import streamlit as st
import calc



if "Ingresar" not in st.session_state:
      st.session_state["Ingresar"] = False
cliente = st.text_input("Ingrese su nombre: ")
contraseña = st.text_input("Ingrese su contraseña: ", type="password")
if st.button("Ingresar"):
    if cliente == "Bastian" and contraseña == "bastian19":
        st.session_state["Ingresar"] = True
        st.success("Bienvenido, {}".format(cliente))
        time.sleep(1)
        st.write("Accediendo al sistema...")
        time.sleep(1)
        st.write("Cargando datos...")
        time.sleep(1)
    else:
        st.error("Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
if st.session_state["Ingresar"]:
        st.write("¡Listo! Ahora puedes realizar tus operaciones.")
        numero = st.number_input("Ingrese el número de presupuesto: ", min_value=1, step=1)
        seleccion = st.selectbox("Seleccione su Producto: ", producto )
        cantidad = st.number_input("Ingrese la cantidad", min_value = 0, step = 1)
        pos = calc.buscar_posicion(producto, seleccion)
        precio = precio[pos]
        subtotal = precio*cantidad
        pago = st.radio("Su forma de pago", ["Efectivo", "Transferencia"])
        descuento = calc.aplicar_descuento(subtotal, pago)
        iva = calc.calcular_iva(descuento)
        total = descuento + iva
        if seleccion == "Coca Cola":
            st.write("Has seleccionado Coca-Cola. Precio: $1500")
        if seleccion == "Asado 1kg":
            st.write("Has seleccionado Asado 1kg. Precio: $9000")
        if seleccion == "Berenjena al Escaveche":
            st.write("Has seleccionado Berenjena al Escaveche. Precio: $4600")
        if seleccion == "Galletas":
            st.write("Has seleccionado Galletas. Precio: $4000")
        if seleccion == "Alfajores":
            st.write("Has seleccionado Alfajores. Precio: $4000")
        
        st.write("El precio por unidad es de: $", precio)
        st.write("El subtotal de su compra es: ${}".format(subtotal))
        st.write("Con descuento el precio de su compra es de: $", descuento)
        st.write("Mas el iva es de: $", iva)
        st.write(cliente, "El total para pagar es de: $", total)


        fecha = st.date_input("Ingrese la fecha: ", value=time.strftime("%Y-%m-%d"))

 
        archivo = pdf_presupuesto.armar_pdf(
            numero=numero, fecha=fecha, cliente=cliente, producto=producto,
            cantidad=cantidad, precio=precio, subtotal=subtotal,
            descuento=descuento, iva=iva, total=total)
 
        st.download_button("Descargar presupuesto (PDF)", archivo,
                        file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")
