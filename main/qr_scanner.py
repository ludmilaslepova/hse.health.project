"""
Тут описан сценарий работы с внешним сервисом, который отдаёт название продукта по qr-коду. После этого, находим продукт в нашей БД.
"""


#### на клиенте (приложение)
 
QR_reader.onscan(handle_QR_scan)
 
def parse_QR_data(qr_data):
    return {
        'product_bar_id': qr_data.id
    }
 
async def get_product_data(data):
    return request.get('https://my-server-name.com/get_product_by_bar_id/{0}'.format(data.product_bar_id))
 
async def handle_QR_scan(qr_data):
    product = await get_product_data(parse_QR_data(qr_data))
 
 
#### на сервере
 
# обработка http запроса /get_product_by_bar_id
 
# достаём информацию о продукте из своей БД
def parse_external_product_data(data):
    Food
        .select()
        .where(data.name in Food.name)
 
# достаём точное название продукта из какой-то внешней БД, содержащей айдишники из QR кодов
async def get_external_product_data(product_bar_id):
    return parse_external_product_data(
        await request.get('https://some-external-service-product-database.com/{}'.format(product_bar_id)
    ))
 
# хэндлер запроса, который принимает на вход его единственный параметр
handle_qr_request(product_bar_id):
    return get_external_product_data(product_bar_id)