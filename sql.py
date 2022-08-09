query_url = "SELECT url FROM urls WHERE type_url=%(type)s"
query_insert = "INSERT INTO urls (urls_id, url, type_url) VALUES (%s, %s, %s)"
arg_url_simple = {'type':'simpled'}
arg_url = 'http:stestste/test'
arg_url_top = {'type':'top'}

query_exists = "SELECT order_num, price_us, delivery_time, " \
               "price_rus FROM deliver WHERE num=%s"
query_update = "UPDATE deliver SET order_num=%s, price_us=%s, delivery_time=%s, price_rus=%s WHERE num=%s"
query_add = "INSERT INTO deliver (num, order_num, price_us, delivery_time, price_rus)" \
            " VALUES (%s, %s, %s, %s, %s)"

query_filter = "INSERT INTO filters (query_post, user_id) VALUES (%s, %s)"
query_filter_update = "UPDATE filters SET query_post = %s WHERE user_id = %s"
query_update_f = "UPDATE subscribers SET filters_id = %s WHERE personal_uid = %s"
query_get_filters = "SELECT query_post, last_post, user_id FROM filters"


"""CREATE TABLE deliver
(id serial PRIMARY KEY, 
 num INTEGER NOT NULL,
 order_num INTEGER NOT NULL, 
 price_us INTEGER NOT NULL,
 delivery_time DATE NOT NULL DEFAULT NOW(),
 price_rus INTEGER)"""