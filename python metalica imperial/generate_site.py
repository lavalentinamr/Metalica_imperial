import os
from string import Template

# Datos de productos simulados
products = [
    {'id': 1, 'name': 'Producto 1', 'price': 10.00, 'description': 'Descripción del producto 1', 'image': 'static/img/product1.jpg'},
    {'id': 2, 'name': 'Producto 2', 'price': 20.00, 'description': 'Descripción del producto 2', 'image': 'static/img/product1.jpg'},
    {'id': 3, 'name': 'Producto 3', 'price': 30.00, 'description': 'Descripción del producto 3', 'image': 'static/img/product1.jpg'}
]

# Función para generar la página principal
def generate_index(products):
    with open('templates/index.html', 'r') as f:
        template = Template(f.read())
    
    product_list = ''
    for product in products:
        product_list += f"""
        <div class="col-md-4">
            <div class="card mb-4">
                <img src="{product['image']}" class="card-img-top" alt="{product['name']}">
                <div class="card-body">
                    <h5 class="card-title">{product['name']}</h5>
                    <p class="card-text">{product['description']}</p>
                    <p class="card-text"><strong>${product['price']}</strong></p>
                    <a href="product{product['id']}.html" class="btn btn-primary">Ver Producto</a>
                </div>
            </div>
        </div>
        """
    
    # Renderizar la plantilla y escribir en un archivo
    rendered_page = template.substitute(products=product_list)
    with open('index.html', 'w') as f:
        f.write(rendered_page)

# Función para generar páginas de productos individuales
def generate_product_page(product):
    with open('templates/product.html', 'r') as f:
        template = Template(f.read())
    
    # Renderizar la plantilla del producto y escribir el archivo
    rendered_page = template.substitute(
        name=product['name'],
        description=product['description'],
        price=product['price'],
        image=product['image']
    )
    with open(f'product{product["id"]}.html', 'w') as f:
        f.write(rendered_page)

# Generar el sitio
def generate_site():
    generate_index(products)
    for product in products:
        generate_product_page(product)

if __name__ == '__main__':
    generate_site()
